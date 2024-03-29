from django.urls import path
from . import views
from .rest_views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    path('rest_booksinstances/', REST_list_books_instances.as_view()),
    path('rest_self_booksinstances/', REST_list_self_books_instances.as_view()),
    path('rest_self_requirements/', REST_list_self_requirements.as_view()),
    
    path('rest_authors/', REST_list_authors.as_view()),
    path('rest_books/', REST_list_books.as_view()),
    path('rest_book/<int:pk>/', REST_book_detail.as_view()),
    path('rest_author/<int:pk>/', REST_author_detail.as_view()),
    path('rest_author_protected/<int:pk>/', REST_author_detail_jwt_auth.as_view()),

    # path('api/register/', views.register_user, name='register_user'),
    # path('api/user/<int:pk>/', views.user_detail, name='user_detail'),

    path('requests/', RequestsAPIView.as_view(), name='requests'),
    path('requests/<int:pk>/', RequestDetailAPIView.as_view(), name='request-detail'),
]
