from django.contrib import admin
from .models import Tele, Post, Tag, Category
# Register your models here.
class TeleAdmin(admin.ModelAdmin):
    list_display = ('ag_port','number','depart','person','floor','number_110_frame','notes')
    search_fields = ('number','depart','person')

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
admin.site.register(Tele, TeleAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
