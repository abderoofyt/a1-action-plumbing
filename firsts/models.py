from django.db import models
from users.models import Profile

# Create your models here.
class Navbar(models.Model):
    Choices = [
        ("pricing", "Pricing"),
        ("services", "services"),
        ("services2", "services2"),
        ("portfolio", "gallery"),
        ("portfolio2", "gallery2"),
        ("About", "About"),
        ("team", "team"),
        ("testimonial", "testimonial"),
        ("contact", "contact"),
        ("counter", "counter"),
    ]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    category = models.TextField(choices=Choices, null=True, blank=True)
    
    order = models.IntegerField(null=True, blank=True, unique=True)
    nav = models.CharField(max_length=30, null=True, blank=True)
    details = models.CharField(max_length=300, null=True, blank=True)

    photo = models.ImageField(upload_to="photo/", null=True, blank=True)
    background = models.CharField(max_length=30, null=True, blank=True)
    background_image = models.ImageField(upload_to="photo/", null=True, blank=True)

    def __str__(self):
        return self.nav