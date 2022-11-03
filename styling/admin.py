from django.contrib import admin

# Register your models here.
from .models import Image, ImageAnimation, ImageFilter, Nav, Footer, Header

admin.site.register(Image)
admin.site.register(ImageAnimation)
admin.site.register(ImageFilter)

admin.site.register(Nav)
admin.site.register(Header)
admin.site.register(Footer)
