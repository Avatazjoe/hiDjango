"""hiDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf  import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from milyoncu.views import IndexView, ListView , SignUp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(pattern_name='milyoncu:index', permanent=False)),
    url(r'^milyoncu/', include('milyoncu.urls', namespace="milyoncu")),
    url('accounts/', include('django.contrib.auth.urls')),
    url('signup/', SignUp.as_view(), name='signup'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),


] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
