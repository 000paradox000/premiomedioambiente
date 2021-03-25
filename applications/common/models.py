from django.db import models


class BaseModelQuerySet(models.QuerySet):
    def activate(self):
        self.update(is_active=True)

    def inactivate(self):
        self.update(is_active=False)

    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db)

    def activate(self):
        self.get_queryset().activate()

    def inactivate(self):
        self.get_queryset().inactivate()

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()


class BaseModel(models.Model):
    is_active = models.BooleanField(verbose_name="Activo(a)", default=True, db_index=True, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    modification_date = models.DateTimeField(auto_now=True, editable=False, db_index=True)
    objects = BaseModelManager()

    def __str__(self):
        return "{pk}".format(pk=self.pk)

    class Meta:
        abstract = True
