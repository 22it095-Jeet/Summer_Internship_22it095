from django.contrib import admin
from .models import Blog,Author,userregister,imag,category,product

# Register your models here.

admin.site.register(Blog)
class author_(admin.ModelAdmin):
    list_display =['name','email']
    list_filter =['name','email']
    search_fields =['name','email']
    
admin.site.register(Author,author_)

class user_(admin.ModelAdmin):
    list_display = ['name','email','add','password']
    
admin.site.register(userregister,user_)

class image_(admin.ModelAdmin):
    list_display = ['image']
    
admin.site.register(imag,image_)

class cat_(admin.ModelAdmin):
    list_display=['name','image']
    
admin.site.register(category,cat_)

class pro_(admin.ModelAdmin):
    list_display=['id','name','description','image','category','qty','price']
    
admin.site.register(product,pro_)