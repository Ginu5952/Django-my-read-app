from django.contrib import admin
from .models import Book, Author, BookAuthor, Tag


class BookAdmin(admin.ModelAdmin):
 
    list_display = ('isbn', 'created_at','modified_at','title','get_authors', 'get_tags', 'publisher', 'published_date', 'lang', 'book_format')
    search_fields = ('title', 'isbn', 'publisher')
    list_filter = ('category', 'book_format', 'published_date')  


    def get_authors(self, obj):
        authors_info = obj.bookauthor_set.all()  # Query all BookAuthor instances related to the current Book
        return ", ".join([f"{author.author} ({author.get_role_display()})" for author in authors_info])
    get_authors.short_description = 'Authors & Roles'  # Set column header     

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'

admin.site.register(Book, BookAdmin)

admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Tag)


# In Django models, when you define a field with choices using the choices parameter, Django provides a convenient method to get the display value of the choice rather than its stored value.
# This method is called get_<field>_display(), where <field> is the name of your choice field.
