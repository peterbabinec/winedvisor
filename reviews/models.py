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
    color = models.CharField(max_length=16)

    def __str__(self):
        return '{0} {1}'.format(self.color, 'wine')


class User(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=254)

    def __str__(self):
        return '{0} {1}'.format(self.firstname, self.lastname)


class Review(models.Model):
    rating = models.IntegerField()
    body = models.TextField(max_length=500)
    wine = models.ForeignKey(Wine)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField('date published', null=True)

    def average_quality(self):
        qualities = map(lambda x: x.quality, self.wine_set.all())
        return np.mean(qualities)






