from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_prod =models.FloatField()
    def __str__(self):
        return f'{self.category}-{self.num_of_prod}'