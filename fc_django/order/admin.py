from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('fcuser', 'product') # 튜플로 인식하기 위해서 ',' 적어야됨.

admin.site.register(Order,OrderAdmin)
