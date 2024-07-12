from django.urls import path
from . import views

urlpatterns = [

    path('book/<isbn>', views.book_detail, name='book-detail')
]