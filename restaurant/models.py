from django.db import models

# Create your models here.
class Reserva (models.Model):
    nome = models.CharField(max_length=255)
    number_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not (1 <= self.number_guests <= 6):
            raise ValueError("A reserva maxima e 6.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class MenuItem (models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def save(self, *args, **kwargs):
        if not (1 <= self.inventory <= 5):
            raise ValueError("O estoque maxima e 5.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} : {self.price:.2f}'
    
#/class User(models.Model):
    #usernome = models.CharField(max_length=255)
    #email = models.EmailField()

