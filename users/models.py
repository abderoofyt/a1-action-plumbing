from logging import PlaceHolder
from unicodedata import category, name
from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static


class Profile(models.Model):
    # Choices = [
    #     ("green", "Green"),
    #     ("red", "Red"),
    # ]
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    # temp = models.TextField(choices=Choices)

    slug = models.SlugField(max_length=200, db_index=True)
    motto = models.CharField(max_length=100, null=True, blank=True)

    button =  models.CharField(max_length=30, null=True, blank=True)
    destination =  models.CharField(max_length=30, null=True, blank=True)
    
    year = models.IntegerField(null=True, blank=True)
    
    logo = models.ImageField(upload_to="logo/", null=True, blank=True)
    favicon = models.ImageField(upload_to="logo/", null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')
    
    def __str__(self):
        return self.slug

class Navbar(models.Model):
    Choices = [
        ("pricing", "Pricing"),
        ("services", "services"),
        ("services2", "services2"),
        ("portfolio", "gallery"),
        ("portfolio2", "gallery2"),
        ("about", "about"),
        ("team", "team"),
        ("testimonial", "testimonial"),
        ("contact", "contact"),
        ("counter", "counter"),
    ]
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True)
    category = models.TextField(choices=Choices, null=True, blank=True)
    
    nav = models.CharField(max_length=30, null=True, blank=True)
    details = models.CharField(max_length=300, null=True, blank=True)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)

    background_color = models.BooleanField()
    background_photo = models.ImageField(upload_to="photo/", null=True, blank=True)
    

    def __str__(self):
        return self.nav

class Service(models.Model):
    nav = models.CharField(max_length=30, null=True, blank=True)
    navbar = models.ForeignKey('Navbar', on_delete=models.CASCADE, null=True, blank=True)
    services = models.CharField(max_length=30, null=True, blank=True)
    details = models.CharField(max_length=300, null=True, blank=True)
    icon = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.services


class Gallery(models.Model):
    nav = models.CharField(max_length=30, null=True, blank=True)
    navbar = models.ForeignKey('Navbar', on_delete=models.CASCADE, null=True, blank=True)
    alt = models.CharField(max_length=30)
    filter = models.ForeignKey('Filter', on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)

    def __str__(self):
        return self.alt

class Testimonial(models.Model):
    nav = models.CharField(max_length=30, null=True, blank=True)
    navbar = models.ForeignKey('Navbar', on_delete=models.CASCADE, null=True, blank=True)
    person = models.CharField(max_length=30)
    quote = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)
    title = models.CharField(max_length=30, null=True, blank=True)


    def __str__(self):
        return self.person

class Counter(models.Model):
    nav = models.CharField(max_length=30, null=True, blank=True)
    navbar = models.ForeignKey('Navbar', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Pricing(models.Model):
    nav = models.CharField(max_length=30, null=True, blank=True)
    navbar = models.ForeignKey('Navbar', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    features = models.BooleanField()
    name = models.CharField(max_length=20, null=True, blank=True)
    featured = models.BooleanField()
    price = models.CharField(max_length=20, null=True, blank=True)
    saving = models.CharField(max_length=20, null=True, blank=True)
    payment = models.CharField(max_length=20, null=True, blank=True)

    item_amount = models.IntegerField(null=True, blank=True)
    item_quantity = models.CharField(max_length=10, null=True, blank=True)
    item_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        elif self.title:
            return self.title
        else:
            return self.price

class Order(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    payment = models.CharField(max_length=20, null=True, blank=True)

    item_amount = models.IntegerField(null=True, blank=True)
    item_quantity = models.CharField(max_length=10, null=True, blank=True)
    item_name = models.CharField(max_length=30, null=True, blank=True)

    amount = models.IntegerField(default=1, null=True, blank=True)
    contact_info = models.CharField(max_length=30, null=True, blank=True)
    message = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        elif self.title:
            return self.title
        else:
            return self.price

class Icon(models.Model):
    icon = models.CharField(max_length=30)
    icons = models.CharField(max_length=30)
    
    fav = models.CharField(max_length=30)
    shortcut = models.CharField(max_length=30)
    
    def __str__(self):
        return self.icon

class Filter(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Social(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    link = models.CharField(max_length=300, null=True, blank=True)
    icon = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.icon


class Friend_Request(models.Model):
    #received
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE
        )
    #requested
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE
    )
