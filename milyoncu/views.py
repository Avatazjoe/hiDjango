from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, ListView , DetailView
from .models import Product, Category
# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    queryset = Product.objects.order_by('?')[0:4]

class SweatbandsView(IndexView):
    template_name = "sweatbands.html"
    queryset = Product.objects.all().filter(category_id='1')

class HeadbandsView(IndexView):
    template_name = "headbands.html"
    queryset = Product.objects.all().filter(category_id='2')

class BandanasView(IndexView):
    template_name = "bandanas.html"
    queryset = Product.objects.all().filter(category_id='3')

class BalloonsView(IndexView):
    template_name = "balloons.html"
    queryset = Product.objects.all().filter(category_id='4')

class TableCoversView(IndexView):
    template_name = "tablecovers.html"
    queryset = Product.objects.all().filter(category_id='5')

class CoastersView(IndexView):
    template_name = "coasters.html"
    queryset = Product.objects.all().filter(category_id='6')

class CartView(IndexView):
    template_name = "cart.html"
    #queryset = Product.objects.all().filter(category_id='')

class AllProducts(IndexView):
    template_name = "allproducts.html"
    queryset = Product.objects.all()

class Preview(DetailView):
    template_name = "preview.html"


    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(Product, slug=self.kwargs.get("slug"))





