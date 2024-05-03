from django.urls import path
from .views import FormatJson

urlpatterns = [
    path('format/', FormatJson.as_view(), name='format_json'),
]
