from django.contrib import admin

from .models import Collection, Asset

# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
  list_display = ('title_text','author_text','description_text')

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Asset)

