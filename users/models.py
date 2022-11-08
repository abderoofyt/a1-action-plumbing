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

    slug = models.SlugField(max_length=200, db_index=True)
    motto = models.CharField(max_length=100, null=True, blank=True)

    header = models.ImageField(upload_to="photo/", null=True, blank=True)

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

class Order(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    payment = models.CharField(max_length=20, null=True, blank=True)

    item_amount = models.IntegerField(null=True, blank=True)
    item_quantity = models.CharField(max_length=10, null=True, blank=True)
    item_name = models.CharField(max_length=30, null=True, blank=True)

    amount = models.IntegerField(default=1)
    contact_info = models.CharField(max_length=30)
    message = models.CharField(max_length=30)

    def __str__(self):
        if self.name:
            return self.name
        elif self.title:
            return self.title
        else:
            return self.price

class Icon(models.Model):
    user = models.ManyToManyField(User)
    icon = models.CharField(max_length=30)
    icons = models.CharField(max_length=30)
    
    fav = models.CharField(max_length=30)
    shortcut = models.CharField(max_length=30)
    
    def __str__(self):
        return self.icon

class Filter(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Social(models.Model):
    user = models.ManyToManyField(User)
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
