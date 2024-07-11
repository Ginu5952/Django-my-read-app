from django.contrib import admin
from .models import Reader, NIC


admin.site.register(NIC)

class ReaderAdmin(admin.ModelAdmin):
  
  list_display = ('title','get_uppercase_username')


  def get_uppercase_username(self, obj):
      return obj.username.upper()
  get_uppercase_username.short_description = 'Reader Username (Uppercase)'

admin.site.register(Reader,ReaderAdmin)  

 

