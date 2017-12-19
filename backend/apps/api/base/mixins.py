import hashlib

from rest_framework_extensions.etag.mixins import ListETAGMixin


class UpdatedAtListETAGMixin(ListETAGMixin):
    def list_etag_func(self, *args, **kwargs):
        qs = self.get_queryset()
        count = qs.count()

        last_update = None
        if count:
            last_update = qs.latest('updated_at').updated_at

        etag_base_str = str(count) + str(last_update)
        etag = hashlib.md5(etag_base_str.encode('utf-8')).hexdigest()
        return etag
