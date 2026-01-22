# listings/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden

from .models import Listing, Category
from .forms import ListingForm, ListingSearchForm


def index(request):
    """Trang chủ - hiển thị tin mới nhất (chỉ tin đã duyệt)"""
    listings = Listing.objects.filter(status='approved').order_by('-created_at')[:6]
    categories = Category.objects.all()
    
    context = {
        'listings': listings,
        'categories': categories,
    }
    return render(request, 'listings/index.html', context)


def listing_detail(request, listing_id):
    """Xem chi tiết tin đăng"""
    listing = get_object_or_404(Listing, pk=listing_id)
    
    # Chỉ cho xem tin đã duyệt, hoặc chủ tin, hoặc admin
    if listing.status != 'approved':
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Tin này chưa được duyệt")
        if listing.owner != request.user and not request.user.is_staff:
            return HttpResponseForbidden("Tin này chưa được duyệt")
    
    # Tin liên quan (cùng loại nhà)
    related_listings = Listing.objects.filter(
        category=listing.category,
        status='approved'
    ).exclude(pk=listing_id)[:3]
    
    context = {
        'listing': listing,
        'related_listings': related_listings,
    }
    return render(request, 'listings/listing_detail.html', context)


def listing_search(request):
    """Tìm kiếm và lọc tin đăng"""
    form = ListingSearchForm(request.GET)
    listings = Listing.objects.filter(status='approved')
    
    if form.is_valid():
        # Tìm theo từ khóa
        keyword = form.cleaned_data.get('keyword')
        if keyword:
            listings = listings.filter(
                Q(title__icontains=keyword) | 
                Q(address__icontains=keyword) |
                Q(description__icontains=keyword)
            )
        
        # Lọc theo loại hình (Bán/Thuê)
        listing_type = form.cleaned_data.get('listing_type')
        if listing_type:
            listings = listings.filter(listing_type=listing_type)
        
        # Lọc theo danh mục
        category = form.cleaned_data.get('category')
        if category:
            listings = listings.filter(category=category)
        
        # Lọc theo khoảng giá
        price_range = form.cleaned_data.get('price_range')
        if price_range:
            if '-' in price_range:
                parts = price_range.split('-')
                if parts[0] and parts[1]:
                    listings = listings.filter(price__gte=int(parts[0]), price__lte=int(parts[1]))
                elif parts[0]:
                    listings = listings.filter(price__gte=int(parts[0]))
                elif parts[1]:
                    listings = listings.filter(price__lte=int(parts[1]))
        
        # Lọc theo diện tích
        area_range = form.cleaned_data.get('area_range')
        if area_range:
            if '-' in area_range:
                parts = area_range.split('-')
                if parts[0] and parts[1]:
                    listings = listings.filter(area__gte=int(parts[0]), area__lte=int(parts[1]))
                elif parts[0]:
                    listings = listings.filter(area__gte=int(parts[0]))
                elif parts[1]:
                    listings = listings.filter(area__lte=int(parts[1]))
        
        # Sắp xếp
        sort_by = form.cleaned_data.get('sort_by')
        if sort_by:
            listings = listings.order_by(sort_by)
    
    # Phân trang
    paginator = Paginator(listings, 9)  # 9 tin mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'page_obj': page_obj,
        'total_count': listings.count(),
    }
    return render(request, 'listings/listing_search.html', context)


# ==================== CRUD CHO AGENT ====================

@login_required
def listing_create(request):
    """Tạo tin đăng mới (chỉ Agent)"""
    # Kiểm tra quyền
    if not hasattr(request.user, 'profile') or not request.user.profile.is_agent():
        messages.error(request, 'Bạn cần đăng ký làm Người đăng tin để sử dụng chức năng này.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.status = 'pending'  # Chờ duyệt
            listing.save()
            messages.success(request, 'Tin đăng đã được tạo và đang chờ duyệt!')
            return redirect('my_listings')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        form = ListingForm()
    
    context = {
        'form': form,
        'title': 'Đăng tin mới',
    }
    return render(request, 'listings/listing_form.html', context)


@login_required
def listing_update(request, listing_id):
    """Chỉnh sửa tin đăng"""
    listing = get_object_or_404(Listing, pk=listing_id)
    
    # Kiểm tra quyền: chỉ chủ tin hoặc admin mới được sửa
    if listing.owner != request.user and not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền chỉnh sửa tin này.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            updated_listing = form.save(commit=False)
            # Nếu là chủ tin sửa, đưa về trạng thái chờ duyệt
            if not request.user.is_staff:
                updated_listing.status = 'pending'
            updated_listing.save()
            messages.success(request, 'Tin đăng đã được cập nhật!')
            return redirect('listing_detail', listing_id=listing.id)
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        form = ListingForm(instance=listing)
    
    context = {
        'form': form,
        'listing': listing,
        'title': 'Chỉnh sửa tin đăng',
    }
    return render(request, 'listings/listing_form.html', context)


@login_required
def listing_delete(request, listing_id):
    """Xóa tin đăng"""
    listing = get_object_or_404(Listing, pk=listing_id)
    
    # Kiểm tra quyền
    if listing.owner != request.user and not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền xóa tin này.')
        return redirect('home')
    
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Tin đăng đã được xóa!')
        return redirect('my_listings')
    
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing_confirm_delete.html', context)


@login_required
def my_listings(request):
    """Danh sách tin đăng của tôi"""
    listings = Listing.objects.filter(owner=request.user).order_by('-created_at')
    
    # Lọc theo trạng thái
    status_filter = request.GET.get('status')
    if status_filter:
        listings = listings.filter(status=status_filter)
    
    # Phân trang
    paginator = Paginator(listings, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Đếm số tin theo trạng thái
    status_counts = {
        'all': Listing.objects.filter(owner=request.user).count(),
        'pending': Listing.objects.filter(owner=request.user, status='pending').count(),
        'approved': Listing.objects.filter(owner=request.user, status='approved').count(),
        'rejected': Listing.objects.filter(owner=request.user, status='rejected').count(),
    }
    
    context = {
        'page_obj': page_obj,
        'status_filter': status_filter,
        'status_counts': status_counts,
    }
    return render(request, 'listings/my_listings.html', context)


# ==================== ĐẶT LỊCH XEM NHÀ ====================

from .models import Appointment
from .forms import AppointmentForm

@login_required
def appointment_create(request, listing_id):
    """Đặt lịch xem nhà"""
    listing = get_object_or_404(Listing, pk=listing_id, status='approved')
    
    # Không thể đặt lịch cho tin của chính mình
    if listing.owner == request.user:
        messages.error(request, 'Bạn không thể đặt lịch xem nhà cho tin của chính mình.')
        return redirect('listing_detail', listing_id=listing_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.listing = listing
            appointment.customer = request.user
            appointment.status = 'pending'
            appointment.save()
            messages.success(request, 'Yêu cầu đặt lịch xem nhà đã được gửi! Vui lòng chờ xác nhận.')
            return redirect('my_appointments')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        # Pre-fill từ profile nếu có
        initial_data = {}
        if hasattr(request.user, 'profile'):
            initial_data['customer_name'] = request.user.get_full_name() or request.user.username
            initial_data['customer_phone'] = request.user.profile.phone
            initial_data['customer_email'] = request.user.email
        form = AppointmentForm(initial=initial_data)
    
    context = {
        'form': form,
        'listing': listing,
    }
    return render(request, 'listings/appointment_form.html', context)


@login_required
def my_appointments(request):
    """Danh sách lịch hẹn của khách hàng"""
    appointments = Appointment.objects.filter(customer=request.user).order_by('-created_at')
    
    # Lọc theo trạng thái
    status_filter = request.GET.get('status')
    if status_filter:
        appointments = appointments.filter(status=status_filter)
    
    # Đếm theo trạng thái
    status_counts = {
        'all': Appointment.objects.filter(customer=request.user).count(),
        'pending': Appointment.objects.filter(customer=request.user, status='pending').count(),
        'confirmed': Appointment.objects.filter(customer=request.user, status='confirmed').count(),
        'completed': Appointment.objects.filter(customer=request.user, status='completed').count(),
        'cancelled': Appointment.objects.filter(customer=request.user, status='cancelled').count(),
    }
    
    context = {
        'appointments': appointments,
        'status_filter': status_filter,
        'status_counts': status_counts,
    }
    return render(request, 'listings/my_appointments.html', context)


@login_required
def cancel_appointment(request, appointment_id):
    """Khách hủy lịch hẹn"""
    appointment = get_object_or_404(Appointment, pk=appointment_id, customer=request.user)
    
    if appointment.status not in ['pending', 'confirmed']:
        messages.error(request, 'Không thể hủy lịch hẹn này.')
        return redirect('my_appointments')
    
    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, 'Đã hủy lịch hẹn.')
    
    return redirect('my_appointments')


# ==================== QUẢN LÝ LỊCH HẸN CHO AGENT ====================

@login_required
def agent_appointments(request):
    """Danh sách lịch hẹn cho người đăng tin (Agent)"""
    if not hasattr(request.user, 'profile') or not request.user.profile.is_agent():
        messages.error(request, 'Bạn không có quyền truy cập trang này.')
        return redirect('home')
    
    # Lấy tất cả lịch hẹn của các tin do agent này đăng
    appointments = Appointment.objects.filter(
        listing__owner=request.user
    ).order_by('-created_at')
    
    # Lọc theo trạng thái
    status_filter = request.GET.get('status')
    if status_filter:
        appointments = appointments.filter(status=status_filter)
    
    # Đếm theo trạng thái
    base_qs = Appointment.objects.filter(listing__owner=request.user)
    status_counts = {
        'all': base_qs.count(),
        'pending': base_qs.filter(status='pending').count(),
        'confirmed': base_qs.filter(status='confirmed').count(),
        'completed': base_qs.filter(status='completed').count(),
        'cancelled': base_qs.filter(status='cancelled').count(),
    }
    
    context = {
        'appointments': appointments,
        'status_filter': status_filter,
        'status_counts': status_counts,
    }
    return render(request, 'listings/agent_appointments.html', context)


@login_required
def update_appointment_status(request, appointment_id, new_status):
    """Agent cập nhật trạng thái lịch hẹn"""
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    
    # Kiểm tra quyền: chỉ chủ tin mới được cập nhật
    if appointment.listing.owner != request.user:
        messages.error(request, 'Bạn không có quyền thực hiện hành động này.')
        return redirect('agent_appointments')
    
    valid_transitions = {
        'pending': ['confirmed', 'cancelled'],
        'confirmed': ['completed', 'cancelled'],
    }
    
    if appointment.status in valid_transitions and new_status in valid_transitions.get(appointment.status, []):
        appointment.status = new_status
        appointment.save()
        
        status_messages = {
            'confirmed': 'Đã xác nhận lịch hẹn.',
            'completed': 'Đã đánh dấu hoàn thành.',
            'cancelled': 'Đã hủy lịch hẹn.',
        }
        messages.success(request, status_messages.get(new_status, 'Đã cập nhật trạng thái.'))
    else:
        messages.error(request, 'Không thể thực hiện thay đổi trạng thái này.')
    
    return redirect('agent_appointments')


# ==================== ADMIN DUYỆT TIN ====================

@login_required
def admin_pending_listings(request):
    """Trang duyệt tin cho Admin"""
    if not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền truy cập trang này.')
        return redirect('home')
    
    listings = Listing.objects.filter(status='pending').order_by('created_at')
    
    # Phân trang
    paginator = Paginator(listings, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Đếm tổng số tin theo trạng thái
    status_counts = {
        'pending': Listing.objects.filter(status='pending').count(),
        'approved': Listing.objects.filter(status='approved').count(),
        'rejected': Listing.objects.filter(status='rejected').count(),
    }
    
    context = {
        'page_obj': page_obj,
        'status_counts': status_counts,
    }
    return render(request, 'listings/admin_pending_listings.html', context)


@login_required
def admin_approve_listing(request, listing_id):
    """Admin duyệt tin"""
    if not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền thực hiện hành động này.')
        return redirect('home')
    
    listing = get_object_or_404(Listing, pk=listing_id)
    
    if request.method == 'POST':
        listing.status = 'approved'
        listing.save()
        messages.success(request, f'Đã duyệt tin: {listing.title}')
    
    return redirect('admin_pending_listings')


@login_required
def admin_reject_listing(request, listing_id):
    """Admin từ chối tin"""
    if not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền thực hiện hành động này.')
        return redirect('home')
    
    listing = get_object_or_404(Listing, pk=listing_id)
    
    if request.method == 'POST':
        listing.status = 'rejected'
        listing.save()
        messages.success(request, f'Đã từ chối tin: {listing.title}')
    
    return redirect('admin_pending_listings')


# ==================== THỐNG KÊ BÁO CÁO ====================

from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import json

@login_required
def statistics(request):
    """Trang thống kê báo cáo"""
    if not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền truy cập trang này.')
        return redirect('home')
    
    # === BIỂU ĐỒ 1: Số tin đăng theo tháng (6 tháng gần nhất) ===
    six_months_ago = datetime.now() - timedelta(days=180)
    listings_by_month = (
        Listing.objects
        .filter(created_at__gte=six_months_ago)
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    
    # Chuẩn bị data cho Chart.js
    months_labels = []
    months_data = []
    for item in listings_by_month:
        if item['month']:
            months_labels.append(item['month'].strftime('%m/%Y'))
            months_data.append(item['count'])
    
    # === BIỂU ĐỒ 2: Tỷ lệ Bán vs Thuê ===
    listings_by_type = (
        Listing.objects
        .values('listing_type')
        .annotate(count=Count('id'))
    )
    
    type_labels = []
    type_data = []
    type_colors = []
    for item in listings_by_type:
        if item['listing_type'] == 'sale':
            type_labels.append('Nhà đất bán')
            type_colors.append('#dc3545')  # Red
        else:
            type_labels.append('Nhà đất cho thuê')
            type_colors.append('#17a2b8')  # Cyan
        type_data.append(item['count'])
    
    # === BẢNG: Thống kê theo danh mục ===
    categories_stats = (
        Category.objects
        .annotate(
            total=Count('listing'),
            approved=Count('listing', filter=Q(listing__status='approved')),
            pending=Count('listing', filter=Q(listing__status='pending')),
        )
        .order_by('-total')
    )
    
    # === THỐNG KÊ TỔNG QUAN ===
    total_stats = {
        'total_listings': Listing.objects.count(),
        'approved_listings': Listing.objects.filter(status='approved').count(),
        'pending_listings': Listing.objects.filter(status='pending').count(),
        'total_users': User.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'pending_appointments': Appointment.objects.filter(status='pending').count(),
    }
    
    context = {
        'months_labels': json.dumps(months_labels),
        'months_data': json.dumps(months_data),
        'type_labels': json.dumps(type_labels),
        'type_data': json.dumps(type_data),
        'type_colors': json.dumps(type_colors),
        'categories_stats': categories_stats,
        'total_stats': total_stats,
    }
    return render(request, 'listings/statistics.html', context)
