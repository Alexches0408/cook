from django.urls import path
from .views import DishesList, CreateDish, ProductList

app_name = 'menu'

urlpatterns = [
    path('', DishesList.as_view(), name='dishes'),
    path('add/', CreateDish.as_view(), name='add_dish'),
    path('products/', ProductList.as_view(), name='products')
]