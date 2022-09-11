from django.forms import ModelForm, TextInput
from app.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Task'})
        }