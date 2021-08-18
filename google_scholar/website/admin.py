from django.contrib import admin
from .models import Organisation, Scholar, Paper

# Register your models here.

admin.site.register(Scholar)
admin.site.register(Organisation)
admin.site.register(Paper)
