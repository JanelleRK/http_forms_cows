from django.db import models

# Create your models here.
class CowsayTextInput(models.Model):
    cowsay_input = models.CharField(max_length=100)

    def __str__(self):
        return self.cowsay_input


