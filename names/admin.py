from django.contrib import admin

from .models import Man, Woman


class ManAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ['name']


class WomanAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ['name']


admin.site.register(Man, ManAdmin)
admin.site.register(Woman, WomanAdmin)
