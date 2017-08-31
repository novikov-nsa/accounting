from django.db import models

# Create your models here.

class Operations(models.Model):
    accountDt = models.CharField(max_length=200)
    segmentDt1 = models.CharField(max_length=200)
    segmentDt2 = models.CharField(max_length=200)
    segmentDt3 = models.CharField(max_length=200)
    segmentDt4 = models.CharField(max_length=200)
    segmentDt5 = models.CharField(max_length=200)
    segmentDt6 = models.CharField(max_length=200)
    segmentDt7 = models.CharField(max_length=200)
    segmentDt8 = models.CharField(max_length=200)
    segmentDt9 = models.CharField(max_length=200)
    segmentDt10 = models.CharField(max_length=200)
    accountKt = models.CharField(max_length=200)
    segmentKt2 = models.CharField(max_length=200)
    segmentKt3 = models.CharField(max_length=200)
    segmentKt4 = models.CharField(max_length=200)
    segmentKt5 = models.CharField(max_length=200)
    segmentKt6 = models.CharField(max_length=200)
    segmentKt7 = models.CharField(max_length=200)
    segmentKt8 = models.CharField(max_length=200)
    segmentKt9 = models.CharField(max_length=200)
    segmentKt10 = models.CharField(max_length=200)
    sumOperaton = models.FloatField()

