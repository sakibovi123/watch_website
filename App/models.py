from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class MoreImage(models.Model):
    images = models.ImageField(upload_to="images/")


class Size(models.Model):
    size_title = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.size_title


class ColorModel(models.Model):
    color_title = models.CharField(max_length=255)
    color_img = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.color_title


class WatchModel(models.Model):
    watch_name = models.CharField(max_field=255)
    watch_image = models.ImageField(upload_to="images/")
    more_images = models.ManyToManyField(MoreImage)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)