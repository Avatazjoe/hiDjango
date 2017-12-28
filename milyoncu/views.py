from django.shortcuts import render,get_object_or_404 ,redirect, reverse
from django.views.generic import TemplateView, ListView , DetailView
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from milyoncu.forms import ProductForm
from django.template.defaultfilters import slugify

def post_new(request):
    form = ProductForm()
    #return render(request, 'edit.html', {'form': form})
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.POST['name']
            post.description = request.POST['description']
            post.price = request.POST['price']
            post.size = request.POST['size']
            post.category.id = request.POST['category']
            post.logo = request.FILES['logo']

            post.save()
            return redirect('milyoncu:preview', slug= slugify(post.name))

    else:
        form = ProductForm()
        return render(request, 'edit.html', {'form': form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

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


