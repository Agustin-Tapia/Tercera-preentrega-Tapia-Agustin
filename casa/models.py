from django.db import models


class Silla(models.Model):
    precio_silla = models.IntegerField()
    cantidad_silla = models.IntegerField()
    def __str__(self):
        return f"{self.id} - $ precio:{self.precio_silla} - cantidad:{self.cantidad_silla}"

class Sillon(models.Model):
    precio_sillon = models.IntegerField()
    cantidad_sillon = models.IntegerField()
    def __str__(self):
        return f"{self.id} - $ precio:{self.precio_sillon} - cantidad:{self.cantidad_sillon}"


class Mesa(models.Model): 
    precio_mesa = models.IntegerField()
    cantidad_mesa = models.IntegerField()
    def __str__(self):
        return f"{self.id} - $ precio:{self.precio_mesa} - cantidad:{self.cantidad_mesa}"