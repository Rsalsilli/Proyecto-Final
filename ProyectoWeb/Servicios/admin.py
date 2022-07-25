from django.contrib import admin
from .models import Streamers, Categorias
# Register your models here.


class StreamersAdmin(admin.ModelAdmin):
    list_display = ("nombre","followers")

admin.site.register(Categorias)
admin.site.register(Streamers,StreamersAdmin)




