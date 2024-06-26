from django.contrib import admin

from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'phone', 'mostrar',
    ordering = 'id',
    #list_filter = 'create_data',
    search_fields = 'id', 'nome', 'sobrenome',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'nome', 'sobrenome', 'mostrar',
    list_display_links = 'id', 'phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = 'id',