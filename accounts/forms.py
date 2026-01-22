# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    """Form đăng ký tài khoản mới"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email của bạn'
        })
    )
    
    role = forms.ChoiceField(
        choices=[('customer', 'Khách hàng'), ('agent', 'Người đăng tin')],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Bạn là"
    )
    
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Số điện thoại'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Thêm class Bootstrap cho các trường
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Tên đăng nhập'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mật khẩu'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Xác nhận mật khẩu'
        })
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Cập nhật profile
            user.profile.role = self.cleaned_data['role']
            user.profile.phone = self.cleaned_data.get('phone', '')
            user.profile.save()
        return user


class UserLoginForm(AuthenticationForm):
    """Form đăng nhập"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tên đăng nhập'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mật khẩu'
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Ghi nhớ đăng nhập"
    )


class UserUpdateForm(forms.ModelForm):
    """Form cập nhật thông tin User"""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """Form cập nhật Profile"""
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'avatar']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CustomPasswordResetForm(PasswordResetForm):
    """Form quên mật khẩu"""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nhập email đã đăng ký'
        })
    )


class CustomSetPasswordForm(SetPasswordForm):
    """Form đặt mật khẩu mới"""
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mật khẩu mới'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Xác nhận mật khẩu mới'
        })
    )
