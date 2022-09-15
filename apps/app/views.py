from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView, View
from django.urls import reverse_lazy
from apps.app.models import Todo
from apps.app.forms import TodoForm

class HomeView(TemplateView):
    template_name = "app/home.html"


class TodoView(CreateView, ListView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/list.html'
    success_url = reverse_lazy('todos')


class TodoComplete(View):
    def get(self, *args, **kwargs):
        obj = Todo.objects.filter(pk=kwargs['pk'])[0]
        if obj.is_active:
            print('task complete')
            obj.is_active = False
            obj.save()
            return redirect('todos')
        else:
            print('task incomplete')
            obj.is_active = True
            obj.save()
            return redirect('todos')

