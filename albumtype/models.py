from django.db import models

# Create your models here.


class Albumtype (models.Model):
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

