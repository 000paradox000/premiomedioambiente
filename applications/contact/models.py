from django.db import models
from applications.common.models import BaseModel


class contact_us_model(BaseModel):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    email = models.EmailField(verbose_name="Correo electrónico")
    message = models.TextField(verbose_name="Mensaje")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "contáctenos"
        verbose_name = "contáctenos"
        ordering = ['name']
