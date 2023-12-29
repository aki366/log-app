from django.contrib import admin
from .models import Careerlog, Language, Technology, Category

class CareerlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'execution_date', 'timestamp')  # リストで表示するフィールド
    list_filter = ['execution_date']                         # フィルター項目
    search_fields = ['title', 'description']                 # 検索可能なフィールド

admin.site.register(Careerlog, CareerlogAdmin)
admin.site.register(Language)
admin.site.register(Technology)
admin.site.register(Category)
