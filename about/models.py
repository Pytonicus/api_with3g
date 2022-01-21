from django.db import models

class About(models.Model):
    """ Modelo de datos personales """

    bio = models.TextField(verbose_name="Extracto personal")
    name = models.CharField(max_length=200, verbose_name="Nombre y apellidos")
    country = models.CharField(max_length=100, verbose_name="Pais")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    phone = models.CharField(max_length=200, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")
    github = models.URLField(verbose_name="Github")
    linkedin = models.URLField(verbose_name="LinkedIn")

    def __str__(self):
        return self.name

class TechType(models.Model):
    """ Modelo para tipos de tecnologías """

    name = models.CharField(max_length=100, verbose_name="Tipo de tecnología")

    def __str__(self):
        return self.name

class Tech(models.Model):
    """ Modelo de tecnologías que manejo """

    STARS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ] 

    name = models.CharField(max_length=200, verbose_name="Tecnología")
    logo = models.ImageField(upload_to="tecnologias/", verbose_name="Logo")
    type = models.ForeignKey(TechType, on_delete=models.CASCADE, verbose_name="Tipo")
    time = models.DateField(verbose_name="Experiencia")
    level = models.CharField(max_length=100, choices=STARS, verbose_name="Nivel")
    profesional_use = models.BooleanField(verbose_name="Uso profesional", default=False)

    def __str__(self):
        return self.name