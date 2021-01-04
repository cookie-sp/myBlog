from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 表头
    list_display = ("title","author","abstract","visited")
    # 搜索
    search_fields = ("title","author","abstract","visited","content","created_at")
    # 筛选
    list_filter = list_display

admin.site.register(Article,ArticleAdmin)