from django.contrib import admin

# Register your models here.
# listings/models.py
from django.db import models
from django.utils.timezone import now

# Bảng 1: Danh mục (Ví dụ: Nhà bán, Nhà thuê, Căn hộ...)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    
    def __str__(self):
        return self.name

# Bảng 2: Tin rao bất động sản
class Listing(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Loại nhà")
    price = models.IntegerField(verbose_name="Giá (VNĐ)")
    address = models.CharField(max_length=300, verbose_name="Địa chỉ")
    area = models.IntegerField(verbose_name="Diện tích (m2)")
    description = models.TextField(blank=True, verbose_name="Mô tả chi tiết")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Ảnh chính")
    created_at = models.DateTimeField(default=now, verbose_name="Ngày đăng")

    def __str__(self):
        return self.title