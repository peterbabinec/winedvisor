from django.db import models
import numpy as np


class Wine(models.Model):
    fixed_acidity = models.FloatField()
    volatile_acidity = models.FloatField()
    citric_acid = models.FloatField()
    residual_sugar = models.FloatField()
    chlorides = models.FloatField()
    free_sulfur_dioxide = models.FloatField()
    total_sulfur_dioxide = models.FloatField()
    density = models.FloatField()
    ph = models.FloatField()
    sulphates = models.FloatField()
    alcohol = models.FloatField()
    quality = models.FloatField()
    color = models.CharField(max_length=16)

    def average_quality(self):
        qualities = map(lambda x: x.quality, self.wine_set.all())
        return np.mean(qualities)


    def __unicode__(self):
        return '{0} {1}'.format(self.color, 'wine')

