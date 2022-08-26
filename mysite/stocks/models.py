from django.db import models


class Stock(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=200)
    isDraw = models.BooleanField(default=False)
