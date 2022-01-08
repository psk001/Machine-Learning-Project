from django.urls import path 
from .views import AuthorView

app_name="mlapi"

urlpatterns = [
    path('authors/', AuthorView.as_view()),
]