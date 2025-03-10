from django.urls import path
from .views import ProductList, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('list/', ProductList.as_view(), name='list'),
]