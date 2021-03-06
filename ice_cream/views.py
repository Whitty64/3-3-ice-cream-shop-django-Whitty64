from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Menu




class HomePageView(ListView):
    template_name = 'home.html'
    model = Menu

class MenuListView(ListView):
    template_name = 'menu_list.html'
    model = Menu

    def get_queryset(self):
        if 'available' in self.kwargs:
            return Menu.objects.filter(available=self.kwargs['available'])
        else:
            return Menu.objects.filter(featured=True)


class NewIceCreateView(CreateView):
    model = Menu
    template_name = 'flavor_new.html'
    fields = ['flavor', 'base', 'model_pic', 'description']


class IceCreamDetailView(DetailView):
    model = Menu
    template_name = 'ice_cream_detail.html'

class IceCreamDeleteView(DeleteView):
    model = Menu
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class IceCreamUpdateView(UpdateView):
    model = Menu
    template_name = 'edit.html'
    success_url = reverse_lazy('home')
    fields = ['flavor', 'base', 'model_pic', 'description', 'date_churned', 'available']








# Create your views here.
