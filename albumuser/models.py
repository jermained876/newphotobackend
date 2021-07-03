from django.db import models
from album.models import Album
from django.contrib.auth.models import User
# Create your models here.


class Albumuser(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=250)
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE, related_name='albumuser_album')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,  related_name='albumuser_user')

    def __str__(self):
        return str(self.slug)

    