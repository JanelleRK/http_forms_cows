from django.db import models

# Create your models here.
class CowsayText(models.Model):
    cowsay_text = models.TextField()