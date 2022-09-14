from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    dec = models.TextField(max_length=100)
    # price = models.DecimalField(max_digits=5)
    def get_discount(self):
        return 13

    def __str__(self):
        return self.name