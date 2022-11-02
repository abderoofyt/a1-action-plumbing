from django.db import models
from firsts.models import Navbar

# Create your models here.
class Image(models.Model):
    navbar_id = models.ForeignKey(Navbar, on_delete=models.CASCADE)
    image_style = models.CharField(max_length=200)
    image_animation = models.CharField(max_length=200, null=True, blank=True)
    border_radius = models.IntegerField(null=True, blank=True)

class ImageAnimation(models.Model):
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, blank=True, related_name='nav_ref')
    Choices = [
        ("overlay", "overlay"),
        ("middle", "middle"),
        ("polaroid", "polaroid"),
        ("slide right", "slide right"),
        ("slide left", "slide left"),
        ("slide up", "slide up"),
        ("slide down", "slide down"),
    ]
    animation = models.TextField(choices=Choices, null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)

class ImageFilter(models.Model):
    Choices = [
        ("blur", "blur"),
        ("brightness", "brightness"),
        ("contrast", "contrast"),
        ("grayscale", "grayscale"),
        ("invert", "invert"),
        ("opacity", "opacity"),
        ("saturate", "saturate"),
        ("sepia", "sepia"),
        ("hue-rotate", "hue-rotate"),
        ("drop-shadow", "drop-shadow"),
    ]
    animation = models.TextField(choices=Choices, null=True, blank=True)
    value = models.CharField(max_length=30, null=True, blank=True, )
