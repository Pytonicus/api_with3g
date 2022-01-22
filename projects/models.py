from django.db import models
from about.models import Tech 


class Project(models.Model):
    """ Modelo para proyectos personales """

    name = models.CharField(max_length=150, verbose_name="Nombre del proyecto")
    description = models.TextField(verbose_name="Descripción del proyecto")
    logo = models.ImageField(upload_to="proyectos/", verbose_name="Logo proyecto")
    technologies = models.ManyToManyField(Tech, verbose_name="Tecnologías")
    url = models.URLField(verbose_name="Enlace al proyecto", blank=True)
    screenshot = models.ImageField(upload_to="pantalla_proyectos/", verbose_name="Captura proyecto") 

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["name"]

    def __str__(self):
        return self.name 

        