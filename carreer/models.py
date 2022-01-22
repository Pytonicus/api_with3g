from django.db import models
from about.models import Tech


class Carreer(models.Model):
    """ Modelo de carrera profesional """

    job = models.CharField(max_length=150, verbose_name="Puesto")
    company = models.CharField(max_length=150, verbose_name="Compañía")
    logo_company = models.ImageField(upload_to="companies/", verbose_name="Logo de empresa")
    period_start = models.DateField(verbose_name="Fecha inicio")
    period_end = models.DateField(verbose_name="Fecha fin")
    description = models.TextField(verbose_name="Descripción")
    technologies = models.ManyToManyField(Tech, verbose_name="Tecnologías")

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Puestos de trabajo"
        ordering = ["-period_end"]

    def __str__(self):
        return self.job 