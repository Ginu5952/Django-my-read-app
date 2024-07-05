from django.contrib import admin
from .models import Book, Author, BookAuthor, Tag


class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = (BookAuthorInline,)
    list_display = ('isbn', 'title', 'publisher', 'published_date', 'lang', 'book_format')
    search_fields = ('title', 'isbn', 'publisher')
    list_filter = ('category', 'book_format', 'published_date')    

#class AuthorAdmin(admin.ModelAdmin):
 #   inlines = (BookAuthorInline,)
  #  list_display = ('first_name', 'last_name')
   # search_fields = ('first_name', 'last_name')

#class TagAdmin(admin.ModelAdmin):
 #   list_display = ('name',)
  #  search_fields = ('name',)    


admin.site.register(Book, BookAdmin)
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(Tag, TagAdmin)
#admin.site.register(BookAuthor)    

#admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Tag)


# Register your models here.
