from django.contrib.auth.management.commands import createsuperuser


# Fake validate_password
createsuperuser.validate_password = lambda x, y: None


class Command(createsuperuser.Command):
    pass
