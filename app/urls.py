from django.urls import path
from .views import HomeView, AboutView, TodoView, TodoComplete

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('todos/', TodoView.as_view(), name='todos'),
    path('todos/<pk>/complete/', TodoComplete.as_view(), name='todos-complete'),
]