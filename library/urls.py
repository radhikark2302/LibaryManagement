"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# library/urls.py
from django.contrib import admin
from django.urls import path, include
from bookstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookstore.urls')),
     path('api/books', views.add_book, name='add_book'),
    path('api/books', views.list_books, name='list_books'),
    path('api/books/<int:book_id>', views.update_book, name='update_book'),
    path('api/books/<int:book_id>', views.delete_book, name='delete_book'),
    path('api/borrow', views.borrow_book, name='borrow_book'),
    path('api/return/<int:borrow_id>', views.return_book, name='return_book'),
]


