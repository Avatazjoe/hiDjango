from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView
from .models import Product, Category
# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    queryset = Product.objects.all()



class SweatbandsView(IndexView):
    template_name = "sweatbands.html"
    queryset = Product.objects.all()[0:4]


class HeadbandsView(IndexView):
    template_name = "headbands.html"
    queryset = Product.objects.all()[4:8]


class BandanasView(IndexView):
    template_name = "bandanas.html"
    queryset = Product.objects.all()[8:12]


class BalloonsView(IndexView):
    template_name = "balloons.html"
    queryset = Product.objects.all()[12:16]

class TableCoversView(IndexView):
    template_name = "tablecovers.html"
    queryset = Product.objects.all()[16:20]

class CoastersView(IndexView):
    template_name = "coasters.html"
    queryset = Product.objects.all()[20:24]

class CartView(IndexView):
    template_name = "cart.html"
    queryset = Product.objects.all()


