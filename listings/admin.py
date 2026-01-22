# listings/admin.py
from django.contrib import admin
from .models import Category, Listing, Appointment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'listing_type', 'category', 'price', 'status', 'owner', 'created_at')
    list_filter = ('listing_type', 'status', 'category', 'created_at')
    search_fields = ('title', 'address', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'listing_type', 'category', 'status')
        }),
        ('Chi tiết', {
            'fields': ('price', 'address', 'area', 'bedrooms', 'bathrooms', 'description')
        }),
        ('Hình ảnh', {
            'fields': ('photo',)
        }),
        ('Thông tin hệ thống', {
            'fields': ('owner', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
    
    actions = ['approve_listings', 'reject_listings']
    
    @admin.action(description='Duyệt các tin đã chọn')
    def approve_listings(self, request, queryset):
        count = queryset.update(status='approved')
        self.message_user(request, f'Đã duyệt {count} tin đăng.')
    
    @admin.action(description='Từ chối các tin đã chọn')
    def reject_listings(self, request, queryset):
        count = queryset.update(status='rejected')
        self.message_user(request, f'Đã từ chối {count} tin đăng.')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'customer_name', 'customer_phone', 
                    'appointment_date', 'appointment_time', 'status', 'created_at')
    list_filter = ('status', 'appointment_date', 'created_at')
    search_fields = ('customer_name', 'customer_phone', 'customer_email', 'listing__title')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'appointment_date'
    
    fieldsets = (
        ('Thông tin lịch hẹn', {
            'fields': ('listing', 'customer', 'status')
        }),
        ('Thông tin khách hàng', {
            'fields': ('customer_name', 'customer_phone', 'customer_email')
        }),
        ('Thời gian', {
            'fields': ('appointment_date', 'appointment_time')
        }),
        ('Ghi chú', {
            'fields': ('note', 'agent_note'),
            'classes': ('collapse',)
        }),
        ('Hệ thống', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['confirm_appointments', 'complete_appointments', 'cancel_appointments']
    
    @admin.action(description='Xác nhận các lịch hẹn đã chọn')
    def confirm_appointments(self, request, queryset):
        count = queryset.filter(status='pending').update(status='confirmed')
        self.message_user(request, f'Đã xác nhận {count} lịch hẹn.')
    
    @admin.action(description='Đánh dấu hoàn thành')
    def complete_appointments(self, request, queryset):
        count = queryset.filter(status='confirmed').update(status='completed')
        self.message_user(request, f'Đã đánh dấu hoàn thành {count} lịch hẹn.')
    
    @admin.action(description='Hủy các lịch hẹn đã chọn')
    def cancel_appointments(self, request, queryset):
        count = queryset.exclude(status__in=['completed', 'cancelled']).update(status='cancelled')
        self.message_user(request, f'Đã hủy {count} lịch hẹn.')
