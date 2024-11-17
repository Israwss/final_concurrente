from django.db import models

class Supercomputer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cores = models.IntegerField()
    ram = models.IntegerField()
    storage = models.FloatField()
    teraflops = models.FloatField()
    operating_system = models.CharField(max_length=100)

    def __str__(self):
        return self.name