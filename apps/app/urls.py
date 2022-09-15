from django.urls import path
from apps.app.views import HomeView, TodoView, TodoComplete

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('todos/', TodoView.as_view(), name='todos'),
    path('todos/<pk>/complete/', TodoComplete.as_view(), name='todos-complete'),
]