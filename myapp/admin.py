from django.contrib import admin
from .models import Careerlog, Category, Language, Technology

class CareerlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'execution_date', 'timestamp')  # リストで表示するフィールド
    list_filter = ['execution_date']                         # フィルター項目
    search_fields = ['title', 'description']                 # 検索可能なフィールド

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name in ['categories', 'languages', 'technologies']:
            # 新しいCareerlogを追加する場合はNone
            obj_id = request.resolver_match.kwargs.get('object_id')
            if obj_id:
                # 既存のCareerlogを編集する場合
                kwargs["queryset"] = db_field.related_model.objects.filter(careerlog__id=obj_id)
            else:
                # 新しいCareerlogを追加する場合
                kwargs["queryset"] = db_field.related_model.objects.none()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Careerlog, CareerlogAdmin)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Technology)
