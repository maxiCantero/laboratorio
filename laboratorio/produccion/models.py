from django.db import models

# Create your models here.
class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Linea(models.Model):
    ESTADO_CHOICES = [
        ('Stock', 'Stock'),
        ('Activa', 'Activa'),
        ('Pendiente', 'Pendiente'),
        ('Baja', 'Baja'),
    ]
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    numero_de_serie = models.CharField(max_length=100)
    numero_de_telefono = models.CharField(max_length=100)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=20)

    def __str__(self):
        return self.numero_de_serie
            
class TipoDeEquipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Baja', 'Baja'),
    ]
    tipodeEquipo = models.ForeignKey(TipoDeEquipo, on_delete=models.CASCADE)
    numero_de_serie = models.CharField(max_length=100)
    imei = models.CharField(max_length=100)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE, null= True, blank=True, related_name='equipos')
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=20)

    def __str__(self):
        return self.numero_de_serie
    
    def save(self, *args, **kwargs):
        # Si no se ha asignado una línea, establece el estado a "Inactivo"
        if self.linea is None:
            self.estado = 'Inactivo'

        # Comprueba si la Linea ha cambiado
        if self.pk:
            original_equipo = Equipo.objects.get(pk=self.pk)
            if original_equipo.linea != self.linea:
                # Si la Linea ha pasado de tener una Linea asignada a no tenerla, establece el estado a "Inactivo"
                if original_equipo.linea is not None and self.linea is None:
                    self.estado = 'Inactivo'

        super(Equipo, self).save(*args, **kwargs)
    
