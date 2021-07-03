from django.db import models
from django.contrib.auth.models import User
from accesstype.models import Accesstype
# Create your models here.


class Useraccess(models.Model):
    slug = models.SlugField(null=True, blank=True, max_length=250)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    role = models.ForeignKey(Accesstype, null=True, blank=True, on_delete=models.CASCADE, related_name='useraccess')
