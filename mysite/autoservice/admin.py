from django.contrib import admin

from .models import Automobilio_modelis, Automobilis, Paslauga, Uzsakymas, Uzsakymo_eilute

admin.site.register(Automobilio_modelis)
admin.site.register(Automobilis)
admin.site.register(Paslauga)
admin.site.register(Uzsakymas)
admin.site.register(Uzsakymo_eilute)

