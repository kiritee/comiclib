from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Publisher)
admin.site.register(Person)
admin.site.register(Character)
admin.site.register(Comic)
admin.site.register(Collection)
admin.site.register(Reading_Order)
