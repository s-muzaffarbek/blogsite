from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import News,Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['id', 'title', 'created', 'updated', 'is_published', 'get_image']
    list_display_links = ['id', 'title', 'created']
    list_editable = ['is_published']
    list_filter = ['is_published', 'category']
    search_fields = ['title']
    fields = ['title', 'description', 'category', 'get_image', 'image', 'is_published', 'views', 'created', 'updated']
    readonly_fields = ['get_image', 'views', 'created', 'updated']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return "Rasm qo`yilmagan"
    get_image.short_description = 'Rasm'

admin.site.site_title = 'Yangiliklarni boshqarish'
admin.site.site_header = 'Yangiliklarni boshqarish'