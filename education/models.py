from django.db import models

class Education(models.Model):
    """ Modelo Educación """

    title = models.CharField(max_length=150, verbose_name="Título")
    center = models.CharField(max_length=150, verbose_name="Centro")
    logo = models.ImageField(upload_to="centro/", verbose_name="Logotipo")
    date = models.DateField(verbose_name="Fecha de finalización")
    description = models.TextField(verbose_name="Descripción")

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Formación reglada"
        verbose_name_plural="Formaciones regladas"
        ordering = ["-date", ]

    def __str__(self):
        return self.title 


class Certificate(models.Model):
    """ Modelo Certificados """

    title = models.CharField(max_length=150, verbose_name="Título")
    center = models.CharField(max_length=150, verbose_name="Centro")
    logo = models.ImageField(upload_to="centro/", verbose_name="Logotipo")
    date = models.DateField(verbose_name="Fecha de finalización")
    link = models.URLField(verbose_name="Enlace", blank=True)

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Certificado formativo"
        verbose_name_plural="Certificados formativos"
        ordering = ["-date", ]

    def __str__(self):
        return self.title 