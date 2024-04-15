from django.contrib import admin
from django.urls import path

from myapp.views import scrape, clear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape, name='scrape'),
    path('delete/', clear, name='clear'),
]
