from django.contrib import admin
from django.utils.html import format_html
from .models import Article, ArticleCategory, ArticleTag


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'article_count', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
    def article_count(self, obj):
        return obj.articles.count()
    article_count.short_description = 'Số bài viết'


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'article_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    filter_horizontal = ('articles',)
    
    def article_count(self, obj):
        return obj.articles.count()
    article_count.short_description = 'Số bài viết'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'author', 
        'category', 
        'status', 
        'is_featured',
        'views_count', 
        'published_at_display',
        'thumbnail_preview'
    )
    list_filter = ('status', 'category', 'is_featured', 'created_at', 'published_at')
    list_editable = ('status', 'is_featured')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    readonly_fields = ('views_count', 'created_at', 'updated_at', 'image_preview')
    raw_id_fields = ['author']
    autocomplete_fields = ['category']
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'slug', 'category', 'author')
        }),
        ('Nội dung', {
            'fields': ('excerpt', 'content')
        }),
        ('Hình ảnh', {
            'fields': ('featured_image', 'image_preview', 'image_caption')
        }),
        ('Trạng thái & SEO', {
            'fields': ('status', 'is_featured', 'meta_description')
        }),
        ('Thống kê & Thời gian', {
            'fields': ('views_count', 'published_at', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def thumbnail_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 4px;"/>',
                obj.featured_image.url
            )
        return "Chưa có ảnh"
    thumbnail_preview.short_description = 'Ảnh'
    
    def image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px;"/>',
                obj.featured_image.url
            )
        return "Chưa có ảnh"
    image_preview.short_description = 'Xem trước ảnh'
    
    def published_at_display(self, obj):
        if obj.published_at:
            return obj.published_at.strftime('%d/%m/%Y %H:%M')
        return '-'
    published_at_display.short_description = 'Ngày xuất bản'
    
    def save_model(self, request, obj, form, change):
        # Tự động set author khi tạo mới
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)
    
    actions = ['publish_articles', 'unpublish_articles', 'mark_featured']
    
    @admin.action(description='Xuất bản bài viết đã chọn')
    def publish_articles(self, request, queryset):
        from django.utils.timezone import now
        count = queryset.update(status='published', published_at=now())
        self.message_user(request, f'Đã xuất bản {count} bài viết.')
    
    @admin.action(description='Chuyển về bản nháp')
    def unpublish_articles(self, request, queryset):
        count = queryset.update(status='draft')
        self.message_user(request, f'Đã chuyển {count} bài viết về bản nháp.')
    
    @admin.action(description='Đánh dấu nổi bật')
    def mark_featured(self, request, queryset):
        count = queryset.update(is_featured=True)
        self.message_user(request, f'Đã đánh dấu {count} bài viết nổi bật.')
