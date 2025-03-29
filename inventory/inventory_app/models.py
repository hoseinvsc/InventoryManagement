from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام دسته‌بندی")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام محصول")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    quantity = models.IntegerField(default=0, verbose_name="موجودی")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    def __str__(self):
        return self.name
