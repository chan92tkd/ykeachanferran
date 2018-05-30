from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items/$', views.items, name='items'),
    url(r'^items/(?P<category>[a-z]{3,5})/$', views.items, name='items'),
    url(r'^item/(?P<item_number>.*)/$', views.product, name='product'),
    url(r'^shoppingcart/$', views.shoppingcart, name='shoppingcart'),
    url(r'^buy/success/$', views.buy_success, name='buy'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^process/$', views.process, name='process'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^register/$', views.register, name='register')
]
