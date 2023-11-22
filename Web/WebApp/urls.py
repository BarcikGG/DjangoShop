from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/add/', views.add_product, name='add_product'),
    path('catalog/view/<int:product_id>/', views.view_product, name='view_product'),
    path('catalog/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('catalog/contact/', views.contact, name='contact'),
    # path('api/', views.api, name='api'),
    # path('api/edit/<int:product_id>/', views.edit_APIproduct, name='edit_APIproduct'),
    # path('api/add/<int:product_id>/', views.add_APIproduct, name='add_APIproduct'),
    # path('api/delete/<int:product_id>/', views.delete_APIproduct, name='delete_APIproduct'),
    # path('api/view/<int:product_id>/', views.view_APIproduct, name='view_APIproduct'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('categories/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:tag_id>/', views.tag_detail, name='tag_detail'),
]
