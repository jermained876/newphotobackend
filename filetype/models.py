from django.db import models

# Create your models here.


class Filetype (models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)