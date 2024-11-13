from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.Name + " :- "+self.email
