from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils.timezone import now
import uuid


class ArticleCategory(models.Model):
    """Danh mục bài viết"""
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Mô tả")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Danh mục tin tức"
        verbose_name_plural = "Danh mục tin tức"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    """Bài viết tin tức"""
    STATUS_CHOICES = (
        ('draft', 'Bản nháp'),
        ('published', 'Đã xuất bản'),
    )
    
    title = models.CharField(max_length=255, verbose_name="Tiêu đề")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.ForeignKey(
        ArticleCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='articles',
        verbose_name="Danh mục"
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='articles',
        verbose_name="Tác giả"
    )
    
    # Nội dung
    excerpt = models.TextField(
        max_length=500, 
        verbose_name="Tóm tắt",
        help_text="Mô tả ngắn gọn về bài viết (hiển thị trong danh sách)"
    )
    content = models.TextField(verbose_name="Nội dung")
    
    # Hình ảnh
    featured_image = models.ImageField(
        upload_to='news/images/%Y/%m/', 
        verbose_name="Ảnh đại diện",
        help_text="Ảnh hiển thị trong danh sách và đầu bài viết"
    )
    image_caption = models.CharField(
        max_length=255, 
        blank=True, 
        verbose_name="Chú thích ảnh"
    )
    
    # Trạng thái và thời gian
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='draft',
        verbose_name="Trạng thái"
    )
    is_featured = models.BooleanField(
        default=False, 
        verbose_name="Bài viết nổi bật"
    )
    
    # SEO
    meta_description = models.CharField(
        max_length=160, 
        blank=True, 
        verbose_name="Meta Description",
        help_text="Mô tả cho SEO (tối đa 160 ký tự)"
    )
    
    # Thống kê
    views_count = models.PositiveIntegerField(default=0, verbose_name="Lượt xem")
    
    # Thời gian
    created_at = models.DateTimeField(default=now, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật lần cuối")
    published_at = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name="Ngày xuất bản"
    )
    
    class Meta:
        verbose_name = "Bài viết"
        verbose_name_plural = "Bài viết"
        ordering = ['-published_at', '-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Tạo slug từ title + uuid ngắn để đảm bảo unique
            base_slug = slugify(self.title)
            unique_id = str(uuid.uuid4())[:8]
            self.slug = f"{base_slug}-{unique_id}"
        
        # Tự động set published_at khi publish
        if self.status == 'published' and not self.published_at:
            self.published_at = now()
            
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})
    
    def get_reading_time(self):
        """Ước tính thời gian đọc (200 từ/phút)"""
        word_count = len(self.content.split())
        minutes = max(1, round(word_count / 200))
        return minutes
    
    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    """Tag cho bài viết"""
    name = models.CharField(max_length=50, verbose_name="Tên tag")
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    articles = models.ManyToManyField(
        Article, 
        related_name='tags',
        blank=True,
        verbose_name="Bài viết"
    )
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
