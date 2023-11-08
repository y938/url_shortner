from django.urls import path
from .views import url_shortner


urlpatterns = [
    path('', url_shortner, name="shorten_url")
]



