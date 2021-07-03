from django.db import models
from albumtype.models import Albumtype
from albumaccess.models import Albumaccess

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    type = models.ForeignKey(Albumtype, null=True, blank=True, on_delete=models.CASCADE, related_name='album_type')
    access = models.ForeignKey(Albumaccess, null=True, blank=True, on_delete=models.CASCADE, related_name='album_access')

    def __str__(self):
        return str(self.name)