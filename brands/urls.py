from django.urls import path
from . import views

urlpatterns = [ 
    path('brands/list/', views.brand_list, name='brand_list'),
]
