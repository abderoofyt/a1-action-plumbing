from django.contrib import admin

# Register your models here.
from .models import Image, ImageAnimation, ImageFilter

admin.site.register(Image)
admin.site.register(ImageAnimation)
admin.site.register(ImageFilter)
