from django.db import models


class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active_on=True)

    def get_index_objects(self):
        return self.get_queryset().filter(is_show_on_index=True)
