from django.contrib import admin
from .models import MyRead, StatusPercent

class ReadAdmin(admin.ModelAdmin):
 
    list_display = ('book_isbn', 'created_at','modified_at','get_uppercase_username','percentage_read', 'start_read_date', 'end_read_date')
 

    def get_uppercase_username(self, obj):
        return obj.reader_username.username.upper()
    get_uppercase_username.short_description = 'Reader Username (Uppercase)'

    
admin.site.register(MyRead,ReadAdmin)
admin.site.register(StatusPercent)
# Register your models here.
