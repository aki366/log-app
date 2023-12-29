from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Careerlog, Category, Language, Technology

class CareerlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'execution_date', 'timestamp')  # リストで表示するフィールド
    list_filter = ['execution_date']                         # フィルター項目
    search_fields = ['title', 'description']                 # 検索可能なフィールド

    # カテゴリ、言語、技術を検索機能付きの選択フォームに設定
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name in ['categories', 'languages', 'technologies']:
            kwargs['widget'] = FilteredSelectMultiple(
                verbose_name=db_field.verbose_name,
                is_stacked=False
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    # FilteredSelectMultipleウィジェット用のCSSとJavaScriptを追加
    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)

# カテゴリ、言語、技術の各モデルを管理サイトに登録
admin.site.register(Careerlog, CareerlogAdmin)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Technology)
