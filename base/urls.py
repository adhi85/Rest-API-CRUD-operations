from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-list/', views.bookList, name='book-list'),
    path('book-view/<int:pk>', views.bookView, name='book-view'),

    path('book-create/', views.bookCreate, name='book-create'),
    path('book-update/<int:pk>', views.bookUpdate, name='book-update'),
    path('book-delete/<int:pk>', views.bookDelete, name='book-delete'),

]
