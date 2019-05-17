from django.views.generic import ListView, CreateView, DetailView
from .models import Menu




class HomePageView(ListView):
    template_name = 'home.html'
    model = Menu

class MenuListView(ListView):
    template_name = 'menu_list.html'
    model = Menu

    queryset = Menu.objects.filter(featured=True)

    def get_queryset(self):
        if 'available' in self.kwargs:
            return Menu.objects.filter(available=self.kwargs['available'])
        else:
            return Menu.objects.all()


class NewIceCreateView(CreateView):
    model = Menu
    template_name = 'flavor_new.html'
    fields = ['flavor', 'base', 'available', 'featured', 'date_churned']


class IceCreamDetailView(DetailView):
    model = Menu
    template_name = 'ice_cream_detail.html'



# Create your views here.
