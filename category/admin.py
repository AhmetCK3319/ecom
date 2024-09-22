from django.contrib import admin
from .models import Category,SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # slug alanının otomatik olarak dolmasını sağlar
    prepopulated_fields = {"slug": ("category_name",)}

    # her zamanki iş
    list_display = (
        "category_name",
        "slug",
        "image_tag",
    )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    # slug alanının otomatik olarak dolmasını sağlar
    prepopulated_fields = {"sub_slug": ("sub_category_name",)}

    # her zamanki iş
    list_display = (
        "sub_category_name",
        "sub_slug",
        "sub_image_tag",
    )