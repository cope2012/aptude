from django.db import models
from model_utils.models import TimeStampedModel


class Iris(TimeStampedModel):
    file = models.CharField(max_length=50, blank=False, null=False)
    sepal_length = models.FloatField(blank=False, default=0)
    sepal_width = models.FloatField(blank=False, default=0)
    petal_length = models.FloatField(blank=False, default=0)
    petal_width = models.FloatField(blank=False, default=0)
    species = models.CharField(max_length=50, blank=False, default='unknown')
