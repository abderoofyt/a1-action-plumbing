from django.contrib import admin
from .models import About, Counter, Gallery, Navbar, Pricing, Service, Testimonial

class HomeAdmin(admin.ModelAdmin):
    list_display = ('services', 'icon',)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'price')

admin.site.register(About)
admin.site.register(Gallery)
admin.site.register(Navbar)
admin.site.register(Pricing, PriceAdmin)

admin.site.register(Service, HomeAdmin)

admin.site.register(Testimonial)