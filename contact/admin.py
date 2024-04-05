from django.contrib import admin

from contact.models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'phone',
    ordering = 'id',
    #list_filter = 'create_data',
    search_fields = 'id', 'nome', 'sobrenome',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'nome', 'sobrenome',
    list_display_links = 'id', 'phone',