from django.db import models


class BaseColor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    medium = models.CharField(max_length=15)
    number = models.IntegerField()
    image_filename = models.CharField(max_length=250)
    # viewbox_coordinates = CharField(max_length=150)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200, blank=True)
    medium = models.CharField(max_length=15)
    number = models.IntegerField()
    image_filename = models.CharField(max_length=250)
    '''
    !!!!!!!!!!!!! - FIX THIS - !!!!!!!!!!!!!!!
    ingredient = models.ForeignKey(Color, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''

    def __str__(self):
        if self.name:
            return self.name
        else:
            return '!!!!! - Ingredients|List - !!!!!'
