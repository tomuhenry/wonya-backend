from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.site_header = "Wonya Admin Area"
admin.site.site_title = "Wonya Admin Area"
admin.site.index_title = "Welcome to Wonya admin area"

admin.site.register(CustomUser, UserAdmin)
