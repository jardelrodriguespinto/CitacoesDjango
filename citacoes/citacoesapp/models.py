from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from datetime import datetime

class Citacoes(models.Model):
    citacao = models.CharField(max_length=5000)
    autor = models.CharField(max_length=200)
    data_da_publicacao = models.DateTimeField(default=datetime.now, blank=True)