from django.shortcuts import render

# Create your views here.


class AlbumType (models.Model):
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)