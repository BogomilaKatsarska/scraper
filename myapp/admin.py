from django.contrib import admin
from myapp.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass
