from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price') # 튜플로 인식하기 위해서 ',' 적어야됨.

admin.site.register(Product,ProductAdmin)

