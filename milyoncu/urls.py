from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^sweatbands/', SweatbandsView.as_view(), name='sweatbands'),

    url(r'^headbands/', HeadbandsView.as_view(), name='headbands'),

    url(r'^bandanas/', BandanasView.as_view(), name='bandanas'),

    url(r'^balloons/', BalloonsView.as_view(), name='balloons'),

    url(r'^tablecovers/', TableCoversView.as_view(), name='tablecovers'),

    url(r'^coasters/', CoastersView.as_view(), name='coasters'),

    url(r'^cart/', CartView.as_view(), name='cart'),


]

