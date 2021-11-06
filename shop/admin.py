from django.contrib import admin
from .models import Parts, Printer, Filament

admin.site.register(Parts)
admin.site.register(Printer)
admin.site.register(Filament)

