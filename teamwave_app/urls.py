from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('limit',views.limit_data,name='limit'),
    path('search',views.search_data,name='search'),
    path('page',views.page_data,name='page'),
]
