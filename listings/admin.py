# listings/admin.py
from django.contrib import admin
# Chú ý dòng dưới: Chúng ta IMPORT từ file models, không viết class mới
from .models import Category, Listing 

admin.site.register(Category)
admin.site.register(Listing)