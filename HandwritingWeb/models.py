import uuid

from django.db import models


class PhotoOfNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    photo = models.ImageField(null=True, blank=True, upload_to='photoNumber/')
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=200, default='')
