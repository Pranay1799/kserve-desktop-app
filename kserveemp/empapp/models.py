from django.db import models

# Create your models here.

class Sentiment(models.Model):

    sentiment = models.CharField(max_length=200, default="")
    emp_id = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.sentiment