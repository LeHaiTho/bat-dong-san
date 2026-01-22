# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """Mở rộng User với thông tin bổ sung và phân quyền"""
    
    ROLE_CHOICES = (
        ('customer', 'Khách hàng'),
        ('agent', 'Người đăng tin'),
        ('admin', 'Quản trị viên'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer', verbose_name="Vai trò")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Số điện thoại")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Ảnh đại diện")
    address = models.CharField(max_length=255, blank=True, verbose_name="Địa chỉ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    
    class Meta:
        verbose_name = "Hồ sơ người dùng"
        verbose_name_plural = "Hồ sơ người dùng"
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    def is_agent(self):
        """Kiểm tra có phải người đăng tin không"""
        return self.role in ['agent', 'admin']
    
    def is_admin(self):
        """Kiểm tra có phải admin không"""
        return self.role == 'admin'


# Signal: Tự động tạo UserProfile khi tạo User mới
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
