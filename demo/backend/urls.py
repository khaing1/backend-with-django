from django.conf.urls import url
from  backend import views



urlpatterns=[

  url(r'^restaurant/(?P<township_id>[0-9]+)$',views.restaurant_list),
  url(r'^restaurant/menu/(?P<pk>[0-9]+)$',views.restaurant_detail)
]