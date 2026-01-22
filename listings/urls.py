# listings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Public views
    path('', views.index, name='home'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('search/', views.listing_search, name='listing_search'),
    
    # Agent CRUD views
    path('listing/create/', views.listing_create, name='listing_create'),
    path('listing/<int:listing_id>/edit/', views.listing_update, name='listing_update'),
    path('listing/<int:listing_id>/delete/', views.listing_delete, name='listing_delete'),
    path('my-listings/', views.my_listings, name='my_listings'),
    
    # Appointment (Đặt lịch xem nhà) - Khách hàng
    path('listing/<int:listing_id>/book/', views.appointment_create, name='appointment_create'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('appointment/<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),
    
    # Appointment - Agent quản lý
    path('agent/appointments/', views.agent_appointments, name='agent_appointments'),
    path('appointment/<int:appointment_id>/status/<str:new_status>/', 
         views.update_appointment_status, name='update_appointment_status'),
    
    # Admin duyệt tin
    path('admin-panel/pending/', views.admin_pending_listings, name='admin_pending_listings'),
    path('admin-panel/approve/<int:listing_id>/', views.admin_approve_listing, name='admin_approve_listing'),
    path('admin-panel/reject/<int:listing_id>/', views.admin_reject_listing, name='admin_reject_listing'),
    
    # Thống kê
    path('statistics/', views.statistics, name='statistics'),
]
