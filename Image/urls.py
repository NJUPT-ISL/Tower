from django.urls import path
from Image import views

app_name = 'Image'
urlpatterns = [
    path('', views.ListView.as_view()),
]
