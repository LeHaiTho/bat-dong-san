# listings/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from .validators import validate_image
# Bảng 1: Danh mục (Chỉ lưu loại nhà)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    
    class Meta:
        verbose_name = "Danh mục"
        verbose_name_plural = "Danh mục"
    
    def __str__(self):
        return self.name


# Bảng 2: Tin rao bất động sản
class Listing(models.Model):
    TYPE_CHOICES = (
        ('sale', 'Nhà đất bán'),
        ('rent', 'Nhà đất cho thuê'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Chờ duyệt'),
        ('approved', 'Đã duyệt'),
        ('rejected', 'Từ chối'),
    )

    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    listing_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='sale', verbose_name="Hình thức")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Loại nhà")
    price = models.BigIntegerField(verbose_name="Giá (VNĐ)")
    address = models.CharField(max_length=300, verbose_name="Địa chỉ")
    area = models.IntegerField(verbose_name="Diện tích (m2)")
    bedrooms = models.IntegerField(default=0, verbose_name="Số phòng ngủ")
    bathrooms = models.IntegerField(default=0, verbose_name="Số phòng tắm")
    description = models.TextField(blank=True, verbose_name="Mô tả chi tiết")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Ảnh chính")
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', 
                              verbose_name="Người đăng", null=True, blank=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='approved', verbose_name="Trạng thái")
    
    created_at = models.DateTimeField(default=now, verbose_name="Ngày đăng")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật lần cuối")

    class Meta:
        verbose_name = "Tin đăng"
        verbose_name_plural = "Tin đăng"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_listing_type_display()}] {self.title}"
    
    def get_price_display(self):
        if self.price >= 1000000000:
            return f"{self.price / 1000000000:.1f} tỷ"
        elif self.price >= 1000000:
            return f"{self.price / 1000000:.0f} triệu"
        else:
            return f"{self.price:,} VNĐ"


# Bảng 3: Đặt lịch xem nhà
class Appointment(models.Model):
    """Lịch hẹn xem nhà giữa khách hàng và người đăng tin"""
    
    STATUS_CHOICES = (
        ('pending', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('completed', 'Đã hoàn thành'),
        ('cancelled', 'Đã hủy'),
    )
    
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, 
                                related_name='appointments', verbose_name="Tin đăng")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, 
                                 related_name='customer_appointments', verbose_name="Khách hàng")
    
    # Thông tin liên hệ
    customer_name = models.CharField(max_length=100, verbose_name="Họ tên")
    customer_phone = models.CharField(max_length=15, verbose_name="Số điện thoại")
    customer_email = models.EmailField(blank=True, verbose_name="Email")
    
    # Thời gian hẹn
    appointment_date = models.DateField(verbose_name="Ngày xem")
    appointment_time = models.TimeField(verbose_name="Giờ xem")
    
    # Ghi chú
    note = models.TextField(blank=True, verbose_name="Ghi chú của khách")
    agent_note = models.TextField(blank=True, verbose_name="Ghi chú của người đăng")
    
    # Trạng thái
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, 
                              default='pending', verbose_name="Trạng thái")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
    
    class Meta:
        verbose_name = "Lịch hẹn xem nhà"
        verbose_name_plural = "Lịch hẹn xem nhà"
        ordering = ['-appointment_date', '-appointment_time']
    
    def __str__(self):
        return f"{self.customer_name} - {self.listing.title} ({self.appointment_date})"
    
    def get_agent(self):
        return self.listing.owner
