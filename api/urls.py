from django.urls import path
from .views import sentimentAnalyzer
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'

urlpatterns = [
    path('', sentimentAnalyzer , name = 'home')
]