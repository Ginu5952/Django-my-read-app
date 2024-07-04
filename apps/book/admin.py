from django.contrib import admin
from .models import Book, Author, BookAuthor, Tag

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Tag)


# Register your models here.
