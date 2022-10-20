from typing import Counter
from django.contrib import admin

# Register your models here.
from .models import Filter, Order, Counter, Gallery, Icon, Navbar, Pricing, Profile, Service, Social, Testimonial

admin.site.register(Filter)
admin.site.register(Gallery)
admin.site.register(Icon)
admin.site.register(Navbar)
admin.site.register(Profile)
admin.site.register(Pricing)
admin.site.register(Service)
admin.site.register(Social)
admin.site.register(Counter)
admin.site.register(Order)
admin.site.register(Testimonial)

