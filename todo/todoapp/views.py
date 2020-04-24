from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = "list.html"
    model = TodoModel


class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel


class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')  # 入力を受け取るためのfieldを指定 名前は合わせる
    success_url = reverse_lazy('list')  # create後の遷移先のurlを指定 


class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = TodoModel
    success_url = reverse_lazy('list')  # delete後の遷移先のurlを指定 


class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')  # 入力を受け取るためのfieldを指定 名前は合わせる
    success_url = reverse_lazy('list')  # delete後の遷移先のurlを指定 