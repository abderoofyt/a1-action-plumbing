from django.db import models
from firsts.models import Navbar
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    user = models.ManyToManyField(User)
    navbar_id = models.ForeignKey(Navbar, on_delete=models.CASCADE)
    image_style = models.CharField(max_length=200)
    image_animation = models.CharField(max_length=200, null=True, blank=True)
    border_radius = models.IntegerField(null=True, blank=True)

class ImageAnimation(models.Model):
    user = models.ManyToManyField(User)
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
    user = models.ManyToManyField(User)
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


class Header(models.Model):
    user = models.ManyToManyField(User)

    title_size = models.IntegerField(default=70, null=True, blank=True)
    title_color = models.CharField(max_length=35, null=True, blank=True)
    title_hover_color = models.CharField(max_length=20, null=True, blank=True)
    title_stroke = models.IntegerField(default=70, null=True, blank=True)
    title_stroke_color = models.CharField(max_length=35, null=True, blank=True)
    title_style = models.CharField(max_length=20, null=True, blank=True)
    title_animation = models.CharField(max_length=20, null=True, blank=True)

    motto_size = models.IntegerField(default=20, null=True, blank=True)
    motto_color = models.CharField(max_length=20, null=True, blank=True)
    motto_hover_color = models.CharField(max_length=20, null=True, blank=True)
    motto_stroke = models.IntegerField(default=70, null=True, blank=True)
    motto_stroke_color = models.CharField(max_length=35, null=True, blank=True)
    motto_style = models.CharField(max_length=20, null=True, blank=True)
    motto_animation = models.CharField(max_length=20, null=True, blank=True)

    header_color = models.CharField(max_length=20, null=True, blank=True)
    header_hover_color = models.CharField(max_length=20, null=True, blank=True)
    header_stroke = models.IntegerField(default=70, null=True, blank=True)
    heaer_stroke_color = models.CharField(max_length=35, null=True, blank=True)
    header_style = models.CharField(max_length=20, null=True, blank=True)
    header_animation = models.CharField(max_length=20, null=True, blank=True)

    text_color = models.CharField(max_length=20, null=True, blank=True)
    text_hover_color = models.CharField(max_length=20, null=True, blank=True)
    text_stroke = models.IntegerField(default=70, null=True, blank=True)
    text_stroke_color = models.CharField(max_length=35, null=True, blank=True)
    text_style = models.CharField(max_length=20, null=True, blank=True)
    text_animation = models.CharField(max_length=20, null=True, blank=True)

class Nav(models.Model):
    user = models.ManyToManyField(User)
    Choices = [
        ("top", "top"),
        ("fixed-top", "fixed-top"),
        ("fixed-bottom", "fixed-bottom"),
    ]
    color = models.CharField(max_length=20, null=True, blank=True)
    bg_color = models.CharField(max_length=20, null=True, blank=True)
    hover_color = models.CharField(max_length=20, null=True, blank=True)
    hover_bg_color = models.CharField(max_length=20, null=True, blank=True)

    direction = models.TextField(choices=Choices)
    style = models.CharField(max_length=20, null=True, blank=True)

class Footer(models.Model):
    user = models.ManyToManyField(User)
    color = models.CharField(max_length=20, null=True, blank=True)
    bg_color = models.CharField(max_length=20, null=True, blank=True)
    link_color = models.CharField(max_length=20, null=True, blank=True)
    link_hover_color = models.CharField(max_length=20, null=True, blank=True)

    direction = models.CharField(max_length=20, null=True, blank=True)
    style = models.CharField(max_length=20, null=True, blank=True)