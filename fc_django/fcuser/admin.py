from django.contrib import admin
from .models import Fcuser

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',) # 튜플로 인식하기 위해서 ',' 적어야됨.

admin.site.register(Fcuser,FcuserAdmin)
