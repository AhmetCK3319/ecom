from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    cat_image = models.ImageField(upload_to="photos/categories", blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("products_by_category", args=[self.slug])

    def image_tag(self):
        if self.cat_image:
            return mark_safe(f'<img src="{self.cat_image.url}" height="50"/>')
        else:
            return ""

    image_tag.short_description = "Image"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=50, unique=True)
    sub_slug = models.SlugField(max_length=100, unique=True)
    sub_description = models.TextField(max_length=255)
    sub_cat_image = models.ImageField(upload_to="photos/categories", blank=True)

    class Meta:
        verbose_name = "subcategory"
        verbose_name_plural = "subcategories"
    def __str__(self):
        return self.sub_category_name

    def get_absolute_url(self):
        return reverse("products_by_category", args=[self.sub_slug])

    def sub_image_tag(self):
        if self.sub_cat_image:
            return mark_safe(f'<img src="{self.sub_cat_image.url}" height="50"/>')
        else:
            return ""

    sub_image_tag.short_description = "Image"