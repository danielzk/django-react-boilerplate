import csv
from os import path

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models.fields.related import ForeignKey, ManyToManyField

# TODO: Write tests


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_path')

    # pylint: disable=too-many-locals,too-many-branches,too-many-statements
    @transaction.atomic
    def handle(self, *args, **options):
        csv_path = options['csv_path']
        verbosity = options['verbosity']

        with open(csv_path) as file:
            filename = path.basename(file.name)
            app, model = filename.split('.')[:-1]
            new_objs_count = updated_objs_count = 0

            try:
                # pylint: disable=invalid-name
                Model = apps.get_model(app, model)
            except LookupError:
                raise CommandError('Model {} does not exist'.format(model))

            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                qs = None

                # Filter by translation
                if model.lower().endswith('translation'):
                    language_code = row['language_code']

                    master_codename = row.get('master__codename', None)
                    master_pk = row.get('master', None)
                    if not master_codename and not master_pk:
                        raise CommandError('master__codename or master is required')

                    qs = Model.objects.filter(language_code=language_code)
                    if master_codename:
                        qs = qs.filter(master__codename=master_codename)
                    else:
                        qs = qs.filter(master__pk=master_pk)
                # Filter by pk
                elif Model._meta.pk.name in reader.fieldnames:
                    qs = Model.objects.get(pk=row[Model._meta.pk.name])
                # Filter by codename
                elif 'codename' in reader.fieldnames:
                    qs = Model.objects.filter(codename=row['codename'])

                obj = Model()
                if qs is not None and qs.exists():
                    obj = qs.first()

                m2m_data = {}

                for fieldname in reader.fieldnames:
                    value = row[fieldname]

                    # FK codename
                    if fieldname.endswith('__codename'):
                        fieldname = fieldname.replace('__codename', '_id')
                        if not value:
                            value = None
                        else:
                            RelModel = obj._meta.get_field(fieldname).rel.to  # pylint: disable=invalid-name
                            rel_obj = RelModel.objects.get(codename=value.strip())
                            value = rel_obj.pk
                    # FK
                    elif isinstance(obj._meta.get_field(fieldname), ForeignKey):
                        if not value:
                            value = None
                        else:
                            RelModel = obj._meta.get_field(fieldname).rel.to  # pylint: disable=invalid-name
                            value = RelModel.objects.get(pk=value.strip())
                    # M2M
                    elif (fieldname.endswith('__codenames') or
                          isinstance(obj._meta.get_field(fieldname), ManyToManyField)):
                        m2m_data[fieldname] = value
                        continue
                    # Empty and nullable
                    elif not value and obj._meta.get_field(fieldname).null:
                        value = None

                    setattr(obj, fieldname, value)

                if obj.pk:
                    updated_objs_count += 1
                else:
                    new_objs_count += 1

                obj.save()

                if m2m_data:
                    for fieldname, values in m2m_data.items():
                        values = values.replace(' ', '').split(',')
                        if not any(values):
                            values = []

                        if fieldname.endswith('__codenames'):
                            fieldname = fieldname.replace('__codenames', '')
                            pks = []
                            for codename in values:
                                # pylint: disable=invalid-name
                                RelModel = obj._meta.get_field(fieldname).rel.to
                                pk = RelModel.objects.get(codename=codename).pk
                                pks.append(pk)
                        else:
                            pks = values

                        field = getattr(obj, fieldname)
                        field.set(pks)

        if verbosity:
            msg = '{} items created'.format(new_objs_count)
            self.stdout.write(self.style.SUCCESS(msg))

            msg = '{} items updated'.format(updated_objs_count)
            self.stdout.write(self.style.SUCCESS(msg))
