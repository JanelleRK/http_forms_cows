from django.db import models

# Create your models here.
class TextLine(models.Model):
    text_line = models.CharField(max_length=100)