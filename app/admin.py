from django.contrib import admin
from .models import *

admin.site.register(Categories)
admin.site.register(customers)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','product_image']



