"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views 
from Bookstore1 import views as v2
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.basepage, name='basepage'), 
path('',views.landpage,name='landpage'),
 path('book', views.programming_books_view, name='programming_books'),
path('booklist/', views.booklist, name='booklist'), 
path('categorybook/', views.categorybook, name='categorybook'), 
path('details/', views.details, name='details'),
 path('cart/', views.cart, name='cart'),
 path('proBook/', views.cart, name='cart'),
 path('hero/', v2.hero, name='hero'),
path('AllBooks/',v2.programming_books_view , name='AllBooks'),
path('Blog/',v2.Blog , name='Blog'),
path('about/',v2.about , name='about'),
path('favorites/',v2.favorites,name ='favorites'),
path("detail/<str:book_id>/", v2.book_detail, name="detail"),

 path("wishlist/add/<str:book_id>/", v2.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/", v2.wishlist_view, name="favorites"),
    path("wishlist/remove/<str:book_id>/", v2.remove_from_wishlist, name="remove_from_wishlist"),


     path('auth_login/', v2.auth_login, name='auth_login'),
       path('auth_reg/',v2.auth_reg,name='auth_reg'),
      path('logout/', v2.custom_logout, name='logout'),
   
]
