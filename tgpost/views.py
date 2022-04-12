from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import TgModel


class TgList(ListView):
    template_name = 'list.html'
    model = TgModel

class TgDetail(DetailView):
    template_name = 'detail.html'
    model = TgModel

class TgCreate(CreateView):
    template_name = 'create.html'
    model = TgModel
    fields = ('title','content','category')
    success_url = reverse_lazy('list')

class TgDelete(DeleteView):
    template_name = 'delete.html'
    model = TgModel
    success_url = reverse_lazy('list')

class TgUpdate(UpdateView):
    template_name='update.html'
    model=TgModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')