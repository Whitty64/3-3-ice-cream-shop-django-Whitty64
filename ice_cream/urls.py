from django.urls import path
from .views import HomePageView, MenuListView, NewIceCreateView, IceCreamDetailView, IceCreamDeleteView,\
    IceCreamUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/<int:pk>/', IceCreamDetailView.as_view(), name='ice_cream_detail'),
    path('flavor/new', NewIceCreateView.as_view(), name='flavor_new'),
    path('menu/featured', MenuListView.as_view(), name='featured_menu_list'),
    path('menu/<available>', MenuListView.as_view(), name='available_menu_list'),
    path('delete/<int:pk>/', IceCreamDeleteView.as_view(), name='delete_flavor'),
    path('edit/<int:pk>/', IceCreamUpdateView.as_view(), name='edit_flavor'),

]