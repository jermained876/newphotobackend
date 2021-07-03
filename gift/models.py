from django.db import models
from album.models import Album
from django.contrib.auth.models import User


# Create your models here.


class Gift(models.Model):

    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.album)

