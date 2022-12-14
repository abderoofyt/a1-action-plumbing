from django.db import models

from firsts.models import Navbar
from users.models import Filter, Profile
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    user = models.ManyToManyField(User)
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True, blank=True)
    services = models.CharField(max_length=30)
    details = models.CharField(max_length=300, null=True, blank=True)
    icon = models.CharField(max_length=30, null=True, blank=True)

class About(models.Model):
    user = models.ManyToManyField(User)
    background = models.CharField(max_length=30)
    background_image = models.ImageField(upload_to="photo/", null=True, blank=True)


class Gallery(models.Model):
    user = models.ManyToManyField(User)
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True, blank=True)
    alt = models.CharField(max_length=30)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)

    def __str__(self):
        return self.alt

class Testimonial(models.Model):
    user = models.ManyToManyField(User)
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True, blank=True)
    person = models.CharField(max_length=30)
    quote = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)
    title = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.person

class Counter(models.Model):
    user = models.ManyToManyField(User)
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Pricing(models.Model):
    user = models.ManyToManyField(User)
    Choices = [
        ("cash", "cash/card"),
        ("oo", "one off"),
        ("w", "weekly"),
        ("o3m", "over 3 months"),
        ("o6m", "over 6 months"),
        ("ay", "over a year"),
    ]
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    features = models.BooleanField()
    name = models.CharField(max_length=20, null=True, blank=True)
    featured = models.BooleanField()
    price = models.CharField(max_length=20)
    saving = models.CharField(max_length=20, null=True, blank=True)

    payment_style = models.TextField(choices=Choices)

    item_amount = models.IntegerField(null=True, blank=True)
    item_quantity = models.CharField(max_length=10, null=True, blank=True)
    item_name = models.CharField(max_length=30, null=True, blank=True)