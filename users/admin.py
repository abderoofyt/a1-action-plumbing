from typing import Counter
from django.contrib import admin

# Register your models here.
from .models import Filter, Order, Icon,  Profile, Social

admin.site.register(Filter)
admin.site.register(Icon)
admin.site.register(Profile)
admin.site.register(Social)
admin.site.register(Order)

