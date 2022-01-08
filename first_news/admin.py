from django.contrib import admin
from .models import Article,Comment  # 追加
from import_export import resources  # 追加
from import_export.admin import ImportExportModelAdmin  # 追加
from import_export.fields import Field # 追加

class ArticleCsv(resources.ModelResource):
   created_at = Field(attribute='created_at',column_name='日にち')
   title = Field(attribute='title',column_name='商品名')
   content = Field(attribute='content',column_name='ロス量')
   # django-import-exportのModel設定
   class Meta:
      model = Article
       # Controls if the import should skip unchanged records. Default value is False
      skip_unchanged = True
      use_bulk = True

@admin.register(Article)
# ImportExportModelAdminを継承したAdminクラスを作成する
class ArtilceAdmin(ImportExportModelAdmin):
   ordering = ['created_at']
   list_display = ('created_at','title','content')
   # resource_classにModelResourceを継承したクラス設定
   resource_class = ArticleCsv
   
#admin.site.register()
