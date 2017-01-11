from django.db import models

class Departement(models.Model):
    name = models.CharField(max_length=150, default='name of departement')
    description = models.CharField(default='what the departement is about',
                                   max_length=250)

    def __str__(self):
        return self.name
