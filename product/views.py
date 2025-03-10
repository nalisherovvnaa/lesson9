from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class ProductList(LoginRequiredMixin, View):
    login_url = 'account:login'
    def get(self, request):
        t = request.GET.get('t')
        user = request.user
        if t:
            page_obj = Product.objects.filter(Q(name__icontains=t) | Q(price__icontains=t))
        else:
            products = Product.objects.all()
            paginator = Paginator(products, 2)  # Show 25 contacts per page.
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
        return render(request, 'list.html', {'page_obj': page_obj, 'user': user})


# class ProductList(View):
    # def get(self, request):
    #     t = request.GET.get('t')
    #     products = Product.objects.annotate(SearchVector('description', 'name'))(search=t) if t else Product.objects.all()
    #     return render(request, 'list.html', {'products': products})


# class SearchList(View):
#     def get(self, request):
#         t = request.GET.get('t')
#         products = Product.objects.filter(name__icontains=t)
#         return render(request, 'search.html', {'products': products})


def home_page(request):
    return render(request, 'home.html')