# listings/forms.py
from django import forms
from .models import Listing, Category
from .validators import validate_image, ALLOWED_IMAGE_EXTENSIONS, MAX_FILE_SIZE


class ListingForm(forms.ModelForm):
    """Form để Agent đăng/sửa tin BĐS"""
    
    class Meta:
        model = Listing
        fields = [
            'title', 'listing_type', 'category', 'price', 
            'address', 'area', 'bedrooms', 'bathrooms', 
            'description', 'photo'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tiêu đề tin đăng'
            }),
            'listing_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập giá (VNĐ)'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập địa chỉ chi tiết'
            }),
            'area': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Diện tích (m²)'
            }),
            'bedrooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'bathrooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Mô tả chi tiết về bất động sản...'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/jpeg,image/png,image/webp,image/gif',
                'id': 'photo-input',
                'onchange': 'previewImage(this)'
            }),
        }
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            # Chỉ validate nếu là file mới upload (không phải file cũ)
            if hasattr(photo, 'size'):
                validate_image(photo)
        return photo
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError("Giá không được âm")
        return price
    
    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area and area <= 0:
            raise forms.ValidationError("Diện tích phải lớn hơn 0")
        return area


class ListingSearchForm(forms.Form):
    """Form tìm kiếm và lọc tin đăng"""
    
    SORT_CHOICES = (
        ('-created_at', 'Mới nhất'),
        ('created_at', 'Cũ nhất'),
        ('price', 'Giá thấp → cao'),
        ('-price', 'Giá cao → thấp'),
        ('-area', 'Diện tích lớn → nhỏ'),
        ('area', 'Diện tích nhỏ → lớn'),
    )
    
    PRICE_RANGE_CHOICES = (
        ('', 'Tất cả mức giá'),
        ('0-500000000', 'Dưới 500 triệu'),
        ('500000000-1000000000', '500 triệu - 1 tỷ'),
        ('1000000000-2000000000', '1 - 2 tỷ'),
        ('2000000000-5000000000', '2 - 5 tỷ'),
        ('5000000000-10000000000', '5 - 10 tỷ'),
        ('10000000000-', 'Trên 10 tỷ'),
    )
    
    AREA_RANGE_CHOICES = (
        ('', 'Tất cả diện tích'),
        ('0-30', 'Dưới 30 m²'),
        ('30-50', '30 - 50 m²'),
        ('50-80', '50 - 80 m²'),
        ('80-100', '80 - 100 m²'),
        ('100-200', '100 - 200 m²'),
        ('200-', 'Trên 200 m²'),
    )
    
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tìm theo tiêu đề, địa chỉ...'
        })
    )
    
    listing_type = forms.ChoiceField(
        required=False,
        choices=[('', 'Tất cả')] + list(Listing.TYPE_CHOICES),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    category = forms.ModelChoiceField(
        required=False,
        queryset=Category.objects.all(),
        empty_label="Tất cả loại nhà",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    price_range = forms.ChoiceField(
        required=False,
        choices=PRICE_RANGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    area_range = forms.ChoiceField(
        required=False,
        choices=AREA_RANGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    sort_by = forms.ChoiceField(
        required=False,
        choices=SORT_CHOICES,
        initial='-created_at',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class AppointmentForm(forms.ModelForm):
    """Form đặt lịch xem nhà"""
    
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        label="Ngày muốn xem"
    )
    
    appointment_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        }),
        label="Giờ muốn xem"
    )
    
    class Meta:
        from .models import Appointment
        model = Appointment
        fields = ['customer_name', 'customer_phone', 'customer_email', 
                  'appointment_date', 'appointment_time', 'note']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Họ và tên của bạn'
            }),
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Số điện thoại liên hệ'
            }),
            'customer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email (không bắt buộc)'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ghi chú thêm (không bắt buộc)'
            }),
        }
    
    def clean_appointment_date(self):
        from datetime import date
        appointment_date = self.cleaned_data.get('appointment_date')
        if appointment_date and appointment_date < date.today():
            raise forms.ValidationError("Ngày xem không thể là ngày trong quá khứ")
        return appointment_date
