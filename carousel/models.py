from django.db import models

# Create your models here.


class Carousel(models.Model):
    asset_id = models.CharField(null=True, blank=True, max_length=400)
    bytes = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.CharField(null=True, blank=True, max_length=250)
    etag = models.CharField(null=True, blank=True, max_length=250)
    format = models.CharField(null=True, blank=True, max_length=250)
    height = models.IntegerField(null=True, blank=True, default=0)
    original_filename = models.CharField(null=True, blank=True, max_length=250)
    public_id = models.CharField(null=True, blank=True, max_length=250)
    resource_type = models.CharField(null=True, blank=True, max_length=250)
    secure_url = models.CharField(null=True, blank=True, max_length=250)
    signature = models.CharField(null=True, blank=True, max_length=250)
    url = models.CharField(null=True, blank=True, max_length=250)
    width = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.asset_id)+'-carousel'