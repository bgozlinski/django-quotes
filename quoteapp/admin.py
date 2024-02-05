from django.contrib import admin
from quoteapp.models import Author, Quote


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['get_full_name']

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    get_full_name.short_description = 'Author'


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'quote_text']

    def get_full_name(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'

    get_full_name.short_description = 'Author'
