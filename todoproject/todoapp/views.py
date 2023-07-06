from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import todo
from .forms import todo_form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TodoList(ListView):
    model = todo
    template_name = 'home.html'
    context_object_name = 'key'


class TodoDetail(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 'task'


class TodoUpdate(UpdateView):
    model = todo
    template_name = 'updat.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('TodoDetail', kwargs={'pk': self.object.id})


class TodoDelete(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('TodoList')


# Create your views here.
def home(request):
    var = todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = todo(name=name, priority=priority, date=date)
        task.save()

    return render(request, "home.html", {'key': var})


def delete(request, todo_id):
    var2 = todo.objects.get(id=todo_id)
    if request.method == 'POST':
        var2.delete()
    else:
        var2.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, do_id):
    var3 = todo.objects.get(id=do_id)
    new1 = todo_form(request.POST or None, instance=var3)
    if new1.is_valid():
        new1.save()
        return redirect('/')
    return render(request, 'update.html', {'new1': new1, 'var3': var3})
