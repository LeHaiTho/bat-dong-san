# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from .forms import (
    UserRegisterForm, 
    UserLoginForm, 
    UserUpdateForm, 
    ProfileUpdateForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm
)


def register(request):
    """Đăng ký tài khoản mới"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tài khoản {username} đã được tạo thành công! Hãy đăng nhập.')
            return redirect('login')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin đăng ký.')
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    """Đăng nhập"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Nếu không tick "ghi nhớ", session hết hạn khi đóng trình duyệt
                if not remember_me:
                    request.session.set_expiry(0)
                
                messages.success(request, f'Chào mừng {username} đã quay trở lại!')
                
                # Redirect về trang trước đó nếu có
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    """Đăng xuất"""
    logout(request)
    messages.info(request, 'Bạn đã đăng xuất thành công.')
    return redirect('home')


@login_required
def profile(request):
    """Xem và chỉnh sửa hồ sơ cá nhân"""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
        )
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Hồ sơ của bạn đã được cập nhật!')
            return redirect('profile')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile.html', context)


# Password Reset Views với template tùy chỉnh
class CustomPasswordResetView(PasswordResetView):
    """Trang nhập email để reset mật khẩu"""
    template_name = 'accounts/password_reset.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """Thông báo đã gửi email"""
    template_name = 'accounts/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """Trang đặt mật khẩu mới"""
    template_name = 'accounts/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """Thông báo đổi mật khẩu thành công"""
    template_name = 'accounts/password_reset_complete.html'
