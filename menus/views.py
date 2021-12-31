from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import  MenuForm, MaterialFormSet
from .models import Menu, Material

'''トップページ'''
class IndexView(ListView):
    template_name = 'menus/index.html'
    model = Menu

class MenuMaterialCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menus/menu_material_create.html'
    success_url = reverse_lazy('menus:menu_material_create')

    def get_context_data(self, **kwargs):
        context = super(MenuMaterialCreateView, self).get_context_data(**kwargs)
        context['inlines'] = MaterialFormSet()
        return context

class MenuDetailView(TemplateView):
    template_name = 'menus/menu_post.html'