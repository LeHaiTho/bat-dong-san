# BÁO CÁO CUỐI KỲ

## ĐỀ TÀI: WEBSITE BẤT ĐỘNG SẢN SỬ DỤNG DJANGO FRAMEWORK

---

## MỤC LỤC

1. [Giới thiệu đề tài](#1-giới-thiệu-đề-tài)
2. [Phân tích bài toán](#2-phân-tích-bài-toán)
3. [Giải pháp kỹ thuật](#3-giải-pháp-kỹ-thuật)
4. [Thiết kế cơ sở dữ liệu](#4-thiết-kế-cơ-sở-dữ-liệu)
5. [Thiết kế giao diện](#5-thiết-kế-giao-diện)
6. [Kiểm thử hệ thống](#6-kiểm-thử-hệ-thống)
7. [Kết luận và hướng phát triển](#7-kết-luận-và-hướng-phát-triển)

---

## 1. GIỚI THIỆU ĐỀ TÀI

### 1.1. Lý do chọn đề tài

Thị trường bất động sản Việt Nam đang phát triển mạnh mẽ với nhu cầu mua bán, cho thuê nhà đất ngày càng tăng cao. Tuy nhiên, việc tìm kiếm thông tin bất động sản phù hợp vẫn còn gặp nhiều khó khăn:

- Thông tin phân tán trên nhiều nền tảng khác nhau
- Khó khăn trong việc kết nối giữa người mua và người bán
- Thiếu công cụ quản lý tin đăng hiệu quả cho môi giới
- Quy trình đặt lịch xem nhà thủ công, mất thời gian

Xuất phát từ thực tế trên, đề tài "Website Bất Động Sản sử dụng Django Framework" được thực hiện nhằm xây dựng một nền tảng trực tuyến toàn diện, giúp kết nối người mua, người bán và môi giới bất động sản một cách hiệu quả.

### 1.2. Mục tiêu đề tài

**Mục tiêu tổng quát:**
Xây dựng website bất động sản với đầy đủ chức năng quản lý, đăng tin, tìm kiếm và đặt lịch xem nhà.

**Mục tiêu cụ thể:**
- Xây dựng hệ thống xác thực và phân quyền người dùng (Customer, Agent, Admin)
- Phát triển chức năng CRUD cho tin đăng bất động sản
- Tích hợp tìm kiếm, lọc và sắp xếp nâng cao
- Xây dựng quy trình duyệt tin và đặt lịch xem nhà
- Phát triển dashboard thống kê cho quản trị viên
- Xây dựng module tin tức bất động sản
- Đảm bảo an toàn khi upload file/ảnh

### 1.3. Phạm vi đề tài

**Đối tượng sử dụng:**
- Khách hàng (Customer): Người tìm kiếm bất động sản
- Môi giới (Agent): Người đăng tin bất động sản
- Quản trị viên (Admin): Người quản lý hệ thống

**Phạm vi chức năng:**
- Quản lý người dùng và phân quyền
- Quản lý tin đăng bất động sản
- Tìm kiếm và lọc tin đăng
- Đặt lịch xem nhà
- Duyệt tin đăng
- Thống kê báo cáo
- Quản lý tin tức

---

## 2. PHÂN TÍCH BÀI TOÁN

### 2.1. Khảo sát hiện trạng

**Các website bất động sản hiện có:**
- Batdongsan.com.vn: Nền tảng lớn nhất Việt Nam
- Chotot.com: Đa dạng loại tin đăng
- Muaban.net: Giao diện đơn giản

**Ưu điểm cần học hỏi:**
- Giao diện thân thiện, dễ sử dụng
- Bộ lọc tìm kiếm đa dạng
- Hệ thống xác thực tin đăng

**Hạn chế cần khắc phục:**
- Quy trình đặt lịch xem nhà chưa tự động
- Thiếu dashboard thống kê cho môi giới
- Module tin tức chưa được tích hợp chặt chẽ

### 2.2. Yêu cầu chức năng

#### 2.2.1. Nhóm chức năng xác thực và phân quyền

| STT | Chức năng | Mô tả |
|-----|-----------|-------|
| 1 | Đăng ký tài khoản | Người dùng tạo tài khoản mới với vai trò Customer hoặc Agent |
| 2 | Đăng nhập | Xác thực người dùng bằng username/password |
| 3 | Đăng xuất | Kết thúc phiên làm việc |
| 4 | Quên mật khẩu | Gửi email reset password |
| 5 | Cập nhật hồ sơ | Thay đổi thông tin cá nhân, avatar |
| 6 | Phân quyền | Kiểm soát truy cập theo vai trò |

#### 2.2.2. Nhóm chức năng quản lý tin đăng

| STT | Chức năng | Mô tả |
|-----|-----------|-------|
| 1 | Xem danh sách tin | Hiển thị các tin đăng đã duyệt |
| 2 | Xem chi tiết tin | Thông tin đầy đủ của tin đăng |
| 3 | Đăng tin mới | Agent tạo tin đăng bất động sản |
| 4 | Sửa tin đăng | Agent chỉnh sửa tin của mình |
| 5 | Xóa tin đăng | Agent xóa tin không còn nhu cầu |
| 6 | Quản lý tin cá nhân | Agent xem danh sách tin đã đăng |

#### 2.2.3. Nhóm chức năng tìm kiếm

| STT | Chức năng | Mô tả |
|-----|-----------|-------|
| 1 | Tìm theo từ khóa | Tìm trong tiêu đề, địa chỉ, mô tả |
| 2 | Lọc theo loại | Bán hoặc Cho thuê |
| 3 | Lọc theo danh mục | Căn hộ, Nhà riêng, Đất nền... |
| 4 | Lọc theo giá | Khoảng giá min-max |
| 5 | Lọc theo diện tích | Khoảng diện tích min-max |
| 6 | Sắp xếp | Mới nhất, Giá, Diện tích |
| 7 | Phân trang | Hiển thị 12 tin/trang |

#### 2.2.4. Nhóm chức năng nghiệp vụ

| STT | Chức năng | Mô tả |
|-----|-----------|-------|
| 1 | Đặt lịch xem nhà | Customer đặt lịch hẹn với Agent |
| 2 | Quản lý lịch hẹn | Customer xem lịch hẹn của mình |
| 3 | Xử lý lịch hẹn | Agent xác nhận/từ chối/hoàn thành |
| 4 | Duyệt tin đăng | Admin phê duyệt/từ chối tin mới |
| 5 | Quản lý tin chờ duyệt | Admin xem danh sách tin pending |

#### 2.2.5. Nhóm chức năng thống kê

| STT | Chức năng | Mô tả |
|-----|-----------|-------|
| 1 | Thống kê tin theo tháng | Biểu đồ cột số tin đăng theo tháng |
| 2 | Thống kê theo danh mục | Biểu đồ tròn phân bổ theo loại BĐS |
| 3 | Bảng tổng hợp | Tổng số tin, user, lịch hẹn |

#### 2.2.6. Nhóm chức năng tin tức

| STT | Chức năng | Mô tả |
|-----|-----------|-------|
| 1 | Xem danh sách tin tức | Hiển thị bài viết đã xuất bản |
| 2 | Xem chi tiết bài viết | Nội dung đầy đủ, bài liên quan |
| 3 | Quản lý bài viết | Admin CRUD bài viết |
| 4 | Quản lý danh mục | Admin CRUD danh mục tin tức |
| 5 | Tìm kiếm bài viết | Tìm theo từ khóa |
| 6 | Lọc theo danh mục/tag | Phân loại bài viết |

### 2.3. Yêu cầu phi chức năng

**Hiệu năng:**
- Thời gian tải trang < 3 giây
- Hỗ trợ 100 người dùng đồng thời

**Bảo mật:**
- Mã hóa mật khẩu (Django password hasher)
- Bảo vệ CSRF token
- Xác thực quyền truy cập
- Kiểm tra file upload (kích thước ≤ 5MB, định dạng ảnh)

**Khả dụng:**
- Giao diện responsive (desktop, tablet, mobile)
- Tương thích các trình duyệt phổ biến

### 2.4. Biểu đồ Use Case

#### 2.4.1. Use Case tổng quan

```
                    ┌─────────────────────────────────────────┐
                    │           HỆ THỐNG BẤT ĐỘNG SẢN         │
                    └─────────────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│   CUSTOMER    │               │     AGENT     │               │     ADMIN     │
├───────────────┤               ├───────────────┤               ├───────────────┤
│ - Đăng ký     │               │ - Đăng ký     │               │ - Quản lý user│
│ - Đăng nhập   │               │ - Đăng nhập   │               │ - Duyệt tin   │
│ - Tìm kiếm    │               │ - Đăng tin    │               │ - Thống kê    │
│ - Xem tin     │               │ - Sửa/Xóa tin │               │ - Quản lý     │
│ - Đặt lịch    │               │ - Xử lý hẹn   │               │   tin tức     │
│ - Xem tin tức │               │ - Xem tin tức │               │ - Toàn quyền  │
└───────────────┘               └───────────────┘               └───────────────┘
```

#### 2.4.2. Use Case quản lý tin đăng

```
                        ┌─────────────┐
                        │    AGENT    │
                        └──────┬──────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       │           │           │           │           │
       ▼           ▼           ▼           ▼           ▼
   ┌───────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐
   │Đăng   │  │Xem tin │  │Sửa tin │  │Xóa tin │  │Xem lịch│
   │tin mới│  │đã đăng │  │đăng    │  │đăng    │  │hẹn     │
   └───────┘  └────────┘  └────────┘  └────────┘  └────────┘
```

#### 2.4.3. Use Case đặt lịch xem nhà

```
┌──────────┐                                      ┌──────────┐
│ CUSTOMER │                                      │  AGENT   │
└────┬─────┘                                      └────┬─────┘
     │                                                 │
     │ 1. Xem tin đăng                                 │
     │ ──────────────────►                             │
     │                                                 │
     │ 2. Đặt lịch xem nhà                            │
     │ ──────────────────►                             │
     │                    ┌────────────┐               │
     │                    │  PENDING   │               │
     │                    └─────┬──────┘               │
     │                          │                      │
     │                          │ 3. Xác nhận/Từ chối  │
     │                          │ ◄────────────────────│
     │                          ▼                      │
     │                    ┌────────────┐               │
     │                    │ CONFIRMED/ │               │
     │                    │ CANCELLED  │               │
     │                    └─────┬──────┘               │
     │                          │                      │
     │                          │ 4. Hoàn thành        │
     │                          │ ◄────────────────────│
     │                          ▼                      │
     │                    ┌────────────┐               │
     │                    │ COMPLETED  │               │
     │                    └────────────┘               │
```

---

## 3. GIẢI PHÁP KỸ THUẬT

### 3.1. Kiến trúc hệ thống

#### 3.1.1. Kiến trúc tổng quan

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   Browser   │  │   Mobile    │  │   Tablet    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/HTTPS
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Django Templates                         │   │
│  │  (HTML + Bootstrap 5 + JavaScript + Chart.js)           │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       BUSINESS LAYER                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   accounts  │  │  listings   │  │    news     │             │
│  │    (app)    │  │    (app)    │  │    (app)    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Django Framework                      │   │
│  │         (Views, Forms, Validators, Decorators)          │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Django ORM                            │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    SQLite Database                       │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

#### 3.1.2. Cấu trúc thư mục dự án

```
BatDongSan/
├── core/                       # Project configuration
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                   # Authentication app
│   ├── models.py              # UserProfile model
│   ├── views.py               # Auth views
│   ├── forms.py               # Registration, Login forms
│   ├── urls.py
│   ├── admin.py
│   └── templates/accounts/
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       └── password_reset*.html
│
├── listings/                   # Real estate app
│   ├── models.py              # Category, Listing, Appointment
│   ├── views.py               # CRUD, Search, Statistics
│   ├── forms.py               # ListingForm, SearchForm
│   ├── validators.py          # File upload validators
│   ├── urls.py
│   ├── admin.py
│   └── templates/listings/
│       ├── index.html
│       ├── listing_detail.html
│       ├── listing_form.html
│       ├── listing_search.html
│       ├── my_listings.html
│       ├── appointment_form.html
│       ├── my_appointments.html
│       ├── agent_appointments.html
│       ├── admin_pending.html
│       └── statistics.html
│
├── news/                       # News app
│   ├── models.py              # Article, Category, Tag
│   ├── views.py               # List, Detail views
│   ├── urls.py
│   ├── admin.py
│   └── templates/news/
│       ├── news_list.html
│       ├── news_detail.html
│       ├── news_category.html
│       └── news_tag.html
│
├── templates/                  # Shared templates
│   └── base.html              # Base template
│
├── media/                      # Uploaded files
│   ├── avatars/
│   ├── photos/
│   └── news/images/
│
├── manage.py
├── db.sqlite3
├── README.md
└── REPORT.md
```

### 3.2. Công nghệ sử dụng

| Thành phần | Công nghệ | Phiên bản | Mục đích |
|------------|-----------|-----------|----------|
| Backend Framework | Django | 5.2.10 | Xử lý logic, routing, ORM |
| Database | SQLite | 3 | Lưu trữ dữ liệu |
| Frontend Framework | Bootstrap | 5.3.0 | Giao diện responsive |
| JavaScript Library | Chart.js | 4.x | Biểu đồ thống kê |
| Icon Library | Font Awesome | 6.0.0 | Icons |
| Image Processing | Pillow | Latest | Xử lý upload ảnh |
| Language | Python | 3.10+ | Ngôn ngữ lập trình |

### 3.3. Mô hình MVC trong Django (MVT)

Django sử dụng mô hình MVT (Model-View-Template):

```
┌─────────────┐     Request     ┌─────────────┐
│   Browser   │ ──────────────► │    URLs     │
└─────────────┘                 └──────┬──────┘
      ▲                                │
      │                                ▼
      │                         ┌─────────────┐
      │                         │    View     │
      │                         └──────┬──────┘
      │                                │
      │         ┌──────────────────────┼──────────────────────┐
      │         │                      │                      │
      │         ▼                      ▼                      ▼
      │   ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
      │   │   Model     │       │   Forms     │       │  Template   │
      │   │   (ORM)     │       │(Validation) │       │   (HTML)    │
      │   └──────┬──────┘       └─────────────┘       └──────┬──────┘
      │          │                                           │
      │          ▼                                           │
      │   ┌─────────────┐                                    │
      │   │  Database   │                                    │
      │   └─────────────┘                                    │
      │                                                      │
      └──────────────────────── Response ────────────────────┘
```

### 3.4. Hệ thống phân quyền

#### 3.4.1. Các vai trò và quyền hạn

| Vai trò | Quyền hạn |
|---------|-----------|
| **Customer** | Xem tin đăng, tìm kiếm, đặt lịch xem nhà, quản lý lịch hẹn cá nhân, xem tin tức |
| **Agent** | Toàn bộ quyền Customer + Đăng tin, sửa/xóa tin của mình, xử lý lịch hẹn khách hàng |
| **Admin** | Toàn quyền + Duyệt tin đăng, xem thống kê, quản lý tin tức, truy cập Django Admin |

#### 3.4.2. Cài đặt phân quyền trong code

```python
# accounts/models.py
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('customer', 'Khách hàng'),
        ('agent', 'Môi giới'),
        ('admin', 'Quản trị viên'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def is_customer(self):
        return self.role == 'customer'
    
    def is_agent(self):
        return self.role == 'agent'
    
    def is_admin(self):
        return self.role == 'admin' or self.user.is_staff
```

#### 3.4.3. Decorator kiểm tra quyền

```python
# listings/views.py
from django.contrib.auth.decorators import login_required, user_passes_test

def is_agent(user):
    return hasattr(user, 'profile') and user.profile.is_agent()

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_agent)
def listing_create(request):
    # Chỉ Agent mới được đăng tin
    ...

@login_required
@user_passes_test(is_admin)
def statistics(request):
    # Chỉ Admin mới xem thống kê
    ...
```

### 3.5. Xử lý upload file an toàn

#### 3.5.1. Validators

```python
# listings/validators.py
from django.core.exceptions import ValidationError

ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def validate_file_extension(value):
    import magic
    file_mime_type = magic.from_buffer(value.read(1024), mime=True)
    value.seek(0)
    if file_mime_type not in ALLOWED_IMAGE_TYPES:
        raise ValidationError('Chỉ chấp nhận file ảnh (JPEG, PNG, GIF, WebP)')

def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError('Kích thước file không được vượt quá 5MB')
```

#### 3.5.2. Cấu hình Django settings

```python
# core/settings.py
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
```

---

## 4. THIẾT KẾ CƠ SỞ DỮ LIỆU

### 4.1. Sơ đồ ERD (Entity Relationship Diagram)

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│      User       │       │   UserProfile   │       │    Category     │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ PK: id          │◄──────│ FK: user_id     │       │ PK: id          │
│ username        │  1:1  │ role            │       │ name            │
│ email           │       │ avatar          │       │ slug            │
│ password        │       │ phone           │       └────────┬────────┘
│ first_name      │       └─────────────────┘                │
│ last_name       │                                          │ 1:N
│ is_staff        │       ┌─────────────────┐                │
└────────┬────────┘       │     Listing     │◄───────────────┘
         │                ├─────────────────┤
         │                │ PK: id          │
         │ 1:N            │ FK: category_id │
         │                │ FK: owner_id    │◄───────────────┐
         │                │ title           │                │
         │                │ description     │                │
         │                │ price           │                │
         │                │ area            │                │
         │                │ address         │                │
         │                │ bedrooms        │                │
         │                │ bathrooms       │                │
         │                │ listing_type    │                │
         │                │ status          │                │
         │                │ photo           │                │
         │                │ created_at      │                │
         │                │ updated_at      │                │
         │                └────────┬────────┘                │
         │                         │                         │
         │                         │ 1:N                     │
         │                         ▼                         │
         │                ┌─────────────────┐                │
         │                │   Appointment   │                │
         │                ├─────────────────┤                │
         │                │ PK: id          │                │
         └───────────────►│ FK: listing_id  │                │
              1:N         │ FK: customer_id │────────────────┘
                          │ customer_name   │
                          │ customer_phone  │
                          │ customer_email  │
                          │ appointment_date│
                          │ appointment_time│
                          │ note            │
                          │ agent_note      │
                          │ status          │
                          │ created_at      │
                          │ updated_at      │
                          └─────────────────┘

┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ ArticleCategory │       │     Article     │       │   ArticleTag    │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ PK: id          │◄──────│ FK: category_id │       │ PK: id          │
│ name            │  1:N  │ FK: author_id   │       │ name            │
│ slug            │       │ PK: id          │       │ slug            │
│ description     │       │ title           │       └────────┬────────┘
└─────────────────┘       │ slug            │                │
                          │ excerpt         │                │ M:N
                          │ content         │◄───────────────┘
                          │ featured_image  │
                          │ image_caption   │
                          │ status          │
                          │ is_featured     │
                          │ views_count     │
                          │ meta_description│
                          │ created_at      │
                          │ updated_at      │
                          │ published_at    │
                          └─────────────────┘
```

### 4.2. Chi tiết các bảng dữ liệu

#### 4.2.1. Bảng UserProfile

| Trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|--------|--------------|-----------|-------|
| id | AutoField | PK | Khóa chính |
| user_id | ForeignKey | FK, Unique | Liên kết User |
| role | CharField(10) | choices | customer/agent/admin |
| avatar | ImageField | nullable | Ảnh đại diện |
| phone | CharField(20) | nullable | Số điện thoại |

#### 4.2.2. Bảng Category (Danh mục BĐS)

| Trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|--------|--------------|-----------|-------|
| id | AutoField | PK | Khóa chính |
| name | CharField(100) | required | Tên danh mục |
| slug | SlugField(100) | unique | URL-friendly name |

#### 4.2.3. Bảng Listing (Tin đăng BĐS)

| Trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|--------|--------------|-----------|-------|
| id | AutoField | PK | Khóa chính |
| category_id | ForeignKey | FK | Danh mục |
| owner_id | ForeignKey | FK, nullable | Người đăng |
| title | CharField(200) | required | Tiêu đề |
| description | TextField | nullable | Mô tả chi tiết |
| price | BigIntegerField | required | Giá (VNĐ) |
| area | DecimalField | required | Diện tích (m²) |
| address | CharField(255) | required | Địa chỉ |
| bedrooms | IntegerField | default=0 | Số phòng ngủ |
| bathrooms | IntegerField | default=0 | Số phòng tắm |
| listing_type | CharField(10) | choices | sale/rent |
| status | CharField(10) | choices | pending/approved/rejected |
| photo | ImageField | required | Ảnh đại diện |
| created_at | DateTimeField | auto | Ngày tạo |
| updated_at | DateTimeField | auto | Ngày cập nhật |

#### 4.2.4. Bảng Appointment (Lịch hẹn)

| Trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|--------|--------------|-----------|-------|
| id | AutoField | PK | Khóa chính |
| listing_id | ForeignKey | FK | Tin đăng |
| customer_id | ForeignKey | FK | Khách hàng |
| customer_name | CharField(100) | required | Tên khách |
| customer_phone | CharField(20) | required | SĐT khách |
| customer_email | EmailField | nullable | Email khách |
| appointment_date | DateField | required | Ngày hẹn |
| appointment_time | TimeField | required | Giờ hẹn |
| note | TextField | nullable | Ghi chú khách |
| agent_note | TextField | nullable | Ghi chú Agent |
| status | CharField(10) | choices | pending/confirmed/completed/cancelled |
| created_at | DateTimeField | auto | Ngày tạo |
| updated_at | DateTimeField | auto | Ngày cập nhật |

#### 4.2.5. Bảng Article (Bài viết tin tức)

| Trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|--------|--------------|-----------|-------|
| id | AutoField | PK | Khóa chính |
| category_id | ForeignKey | FK, nullable | Danh mục |
| author_id | ForeignKey | FK | Tác giả |
| title | CharField(255) | required | Tiêu đề |
| slug | SlugField(255) | unique | URL slug |
| excerpt | TextField(500) | required | Tóm tắt |
| content | TextField | required | Nội dung |
| featured_image | ImageField | required | Ảnh đại diện |
| image_caption | CharField(255) | nullable | Chú thích ảnh |
| status | CharField(10) | choices | draft/published |
| is_featured | BooleanField | default=False | Nổi bật |
| views_count | PositiveIntegerField | default=0 | Lượt xem |
| meta_description | CharField(160) | nullable | SEO description |
| created_at | DateTimeField | auto | Ngày tạo |
| updated_at | DateTimeField | auto | Ngày cập nhật |
| published_at | DateTimeField | nullable | Ngày xuất bản |

### 4.3. Các trạng thái và workflow

#### 4.3.1. Trạng thái tin đăng (Listing Status)

```
                    ┌─────────────┐
                    │   PENDING   │ ◄── Agent đăng tin mới
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               │               ▼
    ┌─────────────┐        │        ┌─────────────┐
    │  APPROVED   │        │        │  REJECTED   │
    │ (Hiển thị)  │        │        │(Không hiện) │
    └─────────────┘        │        └─────────────┘
                           │
                           ▼
                    Admin duyệt tin
```

#### 4.3.2. Trạng thái lịch hẹn (Appointment Status)

```
┌─────────────┐     Agent xác nhận      ┌─────────────┐
│   PENDING   │ ──────────────────────► │  CONFIRMED  │
│ (Chờ duyệt) │                         │ (Đã xác nhận)│
└──────┬──────┘                         └──────┬──────┘
       │                                       │
       │ Agent từ chối                         │ Hoàn thành xem nhà
       ▼                                       ▼
┌─────────────┐                         ┌─────────────┐
│  CANCELLED  │                         │  COMPLETED  │
│  (Đã hủy)   │                         │(Đã hoàn thành)│
└─────────────┘                         └─────────────┘
```

---

## 5. THIẾT KẾ GIAO DIỆN

### 5.1. Cấu trúc Layout chung

#### 5.1.1. Base Template

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <!-- Bootstrap 5, Font Awesome -->
</head>
<body>
    <!-- NAVBAR (sticky-top) -->
    <nav class="navbar navbar-dark bg-dark sticky-top">
        - Logo
        - Menu: Trang chủ | Nhà đất bán | Nhà đất cho thuê | Tin tức
        - User dropdown (nếu đăng nhập)
        - Nút Đăng nhập/Đăng ký (nếu chưa)
    </nav>
    
    <!-- MAIN CONTENT -->
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <!-- FOOTER -->
    <footer class="footer">
        Copyright info
    </footer>
</body>
</html>
```

#### 5.1.2. CSS Layout (Flexbox để footer luôn ở dưới)

```css
body { 
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
main { flex: 1 0 auto; }
.footer { flex-shrink: 0; margin-top: auto; }
```

### 5.2. Các màn hình chính

#### 5.2.1. Trang chủ (index.html)

```
┌────────────────────────────────────────────────────────────┐
│                        NAVBAR                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              HERO BANNER / SEARCH BOX                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
│  TIN ĐĂNG MỚI NHẤT                                        │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │  Card   │  │  Card   │  │  Card   │  │  Card   │       │
│  │ Listing │  │ Listing │  │ Listing │  │ Listing │       │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │
│                                                            │
│  DANH MỤC BẤT ĐỘNG SẢN                                    │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐       │
│  │Căn hộ │ │Nhà phố│ │Biệt thự│ │Đất nền│ │Văn phòng│     │
│  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘       │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                        FOOTER                              │
└────────────────────────────────────────────────────────────┘
```

#### 5.2.2. Trang tìm kiếm (listing_search.html)

```
┌────────────────────────────────────────────────────────────┐
│                        NAVBAR                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────────────┐  ┌─────────────────────────────────┐│
│  │   SIDEBAR FILTER │  │        KẾT QUẢ TÌM KIẾM        ││
│  │                  │  │                                 ││
│  │ Từ khóa: [____]  │  │ Sắp xếp: [Mới nhất ▼]          ││
│  │                  │  │                                 ││
│  │ Loại:            │  │ ┌─────────┐ ┌─────────┐        ││
│  │ ○ Bán  ○ Thuê    │  │ │  Card   │ │  Card   │        ││
│  │                  │  │ │ Listing │ │ Listing │        ││
│  │ Danh mục:        │  │ └─────────┘ └─────────┘        ││
│  │ [Tất cả     ▼]   │  │                                 ││
│  │                  │  │ ┌─────────┐ ┌─────────┐        ││
│  │ Giá (triệu):     │  │ │  Card   │ │  Card   │        ││
│  │ [min] - [max]    │  │ │ Listing │ │ Listing │        ││
│  │                  │  │ └─────────┘ └─────────┘        ││
│  │ Diện tích (m²):  │  │                                 ││
│  │ [min] - [max]    │  │ « 1 2 3 4 5 »                  ││
│  │                  │  │                                 ││
│  │ [🔍 Tìm kiếm]    │  └─────────────────────────────────┘│
│  └──────────────────┘                                     │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                        FOOTER                              │
└────────────────────────────────────────────────────────────┘
```

#### 5.2.3. Trang chi tiết tin đăng (listing_detail.html)

```
┌────────────────────────────────────────────────────────────┐
│                        NAVBAR                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Breadcrumb: Trang chủ > Nhà đất bán > Chi tiết           │
│                                                            │
│  ┌────────────────────────────┐  ┌───────────────────────┐│
│  │                            │  │   THÔNG TIN LIÊN HỆ   ││
│  │      ẢNH BẤT ĐỘNG SẢN      │  │                       ││
│  │                            │  │  ┌───┐ Nguyễn Văn A   ││
│  │       [Badge: BÁN]         │  │  │ 👤│ Môi giới        ││
│  │                            │  │  └───┘                ││
│  └────────────────────────────┘  │                       ││
│                                  │  📞 0901234567        ││
│  ┌────────────────────────────┐  │                       ││
│  │ TIÊU ĐỀ TIN ĐĂNG           │  │  [Đặt lịch xem nhà]   ││
│  │ 💰 5.2 tỷ                  │  │                       ││
│  │ 📍 Quận 1, TP.HCM          │  │  Đăng: 20/01/2026     ││
│  │                            │  └───────────────────────┘│
│  │ ┌────┐ ┌────┐ ┌────┐       │                          │
│  │ │80m²│ │3 PN│ │2 WC│       │                          │
│  │ └────┘ └────┘ └────┘       │                          │
│  └────────────────────────────┘                          │
│                                                            │
│  ┌────────────────────────────────────────────────────────┐│
│  │ MÔ TẢ CHI TIẾT                                        ││
│  │ Lorem ipsum dolor sit amet...                         ││
│  └────────────────────────────────────────────────────────┘│
│                                                            │
│  TIN ĐĂNG LIÊN QUAN                                       │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                   │
│  │  Card   │  │  Card   │  │  Card   │                   │
│  └─────────┘  └─────────┘  └─────────┘                   │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                        FOOTER                              │
└────────────────────────────────────────────────────────────┘
```

#### 5.2.4. Form đặt lịch xem nhà (appointment_form.html)

```
┌────────────────────────────────────────────────────────────┐
│                        NAVBAR                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌─────────────────────────┐  ┌───────────────────────────┐│
│  │    FORM ĐẶT LỊCH       │  │  THÔNG TIN BẤT ĐỘNG SẢN   ││
│  │                         │  │                           ││
│  │  Họ và tên: [_______]   │  │  ┌─────────────────────┐  ││
│  │                         │  │  │       ẢNH           │  ││
│  │  Số điện thoại: [____]  │  │  └─────────────────────┘  ││
│  │                         │  │                           ││
│  │  Email: [___________]   │  │  Tiêu đề tin đăng         ││
│  │                         │  │  💰 Giá: 5.2 tỷ           ││
│  │  Ngày xem: [📅_______]  │  │  📍 Địa chỉ              ││
│  │                         │  │  80m² | 3 PN | 2 WC       ││
│  │  Giờ xem: [🕐_______]   │  │                           ││
│  │                         │  │  👤 Người đăng: ABC       ││
│  │  Ghi chú:               │  └───────────────────────────┘│
│  │  [________________]     │                              │
│  │  [________________]     │                              │
│  │                         │                              │
│  │  [    Đặt lịch    ]     │                              │
│  └─────────────────────────┘                              │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                        FOOTER                              │
└────────────────────────────────────────────────────────────┘
```

#### 5.2.5. Trang thống kê Admin (statistics.html)

```
┌────────────────────────────────────────────────────────────┐
│                        NAVBAR                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  📊 DASHBOARD THỐNG KÊ                                    │
│                                                            │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐          │
│  │  150   │  │   45   │  │   89   │  │   12   │          │
│  │Tin đăng│  │  Users │  │Lịch hẹn│  │Chờ duyệt│          │
│  └────────┘  └────────┘  └────────┘  └────────┘          │
│                                                            │
│  ┌─────────────────────────┐  ┌─────────────────────────┐ │
│  │ BIỂU ĐỒ TIN THEO THÁNG  │  │ BIỂU ĐỒ THEO DANH MỤC  │ │
│  │                         │  │                         │ │
│  │   ▓▓                    │  │        ┌───┐            │ │
│  │   ▓▓  ▓▓                │  │    ┌───┤   │            │ │
│  │   ▓▓  ▓▓  ▓▓            │  │    │   │   ├───┐        │ │
│  │  ────────────           │  │    └───┴───┴───┘        │ │
│  │  T1 T2 T3 T4            │  │  Căn hộ Nhà Đất         │ │
│  └─────────────────────────┘  └─────────────────────────┘ │
│                                                            │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ BẢNG THỐNG KÊ CHI TIẾT                              │  │
│  │                                                      │  │
│  │ Danh mục      | Số tin | Tỷ lệ                      │  │
│  │ ──────────────|────────|────────                    │  │
│  │ Căn hộ        |   45   |  30%                       │  │
│  │ Nhà riêng     |   38   |  25%                       │  │
│  │ Đất nền       |   67   |  45%                       │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                        FOOTER                              │
└────────────────────────────────────────────────────────────┘
```

#### 5.2.6. Trang chi tiết tin tức (news_detail.html)

```
┌────────────────────────────────────────────────────────────┐
│                        NAVBAR                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌────────────────────────────────────────────────────────┐│
│  │              TIÊU ĐỀ BÀI VIẾT LỚN                      ││
│  │              (Font Lexend, 40px)                       ││
│  └────────────────────────────────────────────────────────┘│
│                                                            │
│  ┌───┐ Được đăng bởi Admin                                │
│  │👤 │ Cập nhật: 20/01/2026 • Đọc trong 5 phút            │
│  └───┘                                                    │
│                                                            │
│  ┌─────────────────────────────┐  ┌──────────────────────┐│
│  │                             │  │ BÀI VIẾT XEM NHIỀU   ││
│  │      ẢNH ĐẠI DIỆN          │  │                      ││
│  │      (Featured Image)       │  │ 1. Tiêu đề bài 1    ││
│  │                             │  │ 2. Tiêu đề bài 2    ││
│  └─────────────────────────────┘  │ 3. Tiêu đề bài 3    ││
│                                   │ 4. Tiêu đề bài 4    ││
│  ┌─────────────────────────────┐  │ 5. Tiêu đề bài 5    ││
│  │ TÓM TẮT BÀI VIẾT           │  └──────────────────────┘│
│  │ (Excerpt - highlight box)   │                         │
│  └─────────────────────────────┘                         │
│                                                            │
│  NỘI DUNG BÀI VIẾT                                        │
│  Lorem ipsum dolor sit amet, consectetur adipiscing...    │
│                                                            │
│  Tags: [Thị trường] [Cần Thơ] [Đầu tư]                   │
│                                                            │
│  Chia sẻ: [f] [in] [🐦] [🔗]                             │
│                                                            │
│  ──────────────────────────────────────────────────────   │
│                                                            │
│  BÀI VIẾT LIÊN QUAN                                       │
│  ┌─────────────────┐  ┌─────────────────┐                │
│  │ [Ảnh] Tiêu đề   │  │ [Ảnh] Tiêu đề   │                │
│  │ Tóm tắt...      │  │ Tóm tắt...      │                │
│  └─────────────────┘  └─────────────────┘                │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                        FOOTER                              │
└────────────────────────────────────────────────────────────┘
```

### 5.3. Responsive Design

Website sử dụng Bootstrap 5 grid system để đảm bảo hiển thị tốt trên mọi thiết bị:

| Breakpoint | Màn hình | Số cột grid |
|------------|----------|-------------|
| xs | < 576px | 1 cột (mobile) |
| sm | ≥ 576px | 1-2 cột |
| md | ≥ 768px | 2-3 cột (tablet) |
| lg | ≥ 992px | 3-4 cột (desktop) |
| xl | ≥ 1200px | 4 cột (large desktop) |

---

## 6. KIỂM THỬ HỆ THỐNG

### 6.1. Kiểm thử chức năng (Functional Testing)

#### 6.1.1. Test Case Module Xác thực

| TC ID | Mô tả | Input | Expected Output | Kết quả |
|-------|-------|-------|-----------------|---------|
| TC_AUTH_01 | Đăng ký tài khoản hợp lệ | Username, email, password hợp lệ | Tạo user thành công, redirect home | ✅ Pass |
| TC_AUTH_02 | Đăng ký với email đã tồn tại | Email đã có trong DB | Hiện thông báo lỗi | ✅ Pass |
| TC_AUTH_03 | Đăng nhập đúng | Username, password đúng | Redirect trang chủ | ✅ Pass |
| TC_AUTH_04 | Đăng nhập sai password | Password sai | Hiện thông báo lỗi | ✅ Pass |
| TC_AUTH_05 | Đăng xuất | Click logout | Session bị hủy, redirect home | ✅ Pass |
| TC_AUTH_06 | Reset password | Email hợp lệ | Gửi email reset (console) | ✅ Pass |

#### 6.1.2. Test Case Module Tin đăng

| TC ID | Mô tả | Input | Expected Output | Kết quả |
|-------|-------|-------|-----------------|---------|
| TC_LIST_01 | Agent đăng tin mới | Form hợp lệ + ảnh | Tin tạo với status pending | ✅ Pass |
| TC_LIST_02 | Customer đăng tin | Truy cập /listings/create/ | Redirect hoặc 403 | ✅ Pass |
| TC_LIST_03 | Xem danh sách tin | Truy cập trang chủ | Chỉ hiện tin approved | ✅ Pass |
| TC_LIST_04 | Tìm kiếm theo từ khóa | Keyword "Quận 1" | Kết quả chứa "Quận 1" | ✅ Pass |
| TC_LIST_05 | Lọc theo giá | Min=1tỷ, Max=5tỷ | Tin trong khoảng giá | ✅ Pass |
| TC_LIST_06 | Sắp xếp theo giá | Sort=price_asc | Giá tăng dần | ✅ Pass |
| TC_LIST_07 | Phân trang | Page 2 | Hiện tin 13-24 | ✅ Pass |
| TC_LIST_08 | Agent sửa tin của mình | Form edit | Cập nhật thành công | ✅ Pass |
| TC_LIST_09 | Agent sửa tin người khác | Truy cập edit URL | 403 Forbidden | ✅ Pass |
| TC_LIST_10 | Agent xóa tin | Confirm delete | Tin bị xóa | ✅ Pass |

#### 6.1.3. Test Case Module Lịch hẹn

| TC ID | Mô tả | Input | Expected Output | Kết quả |
|-------|-------|-------|-----------------|---------|
| TC_APT_01 | Customer đặt lịch | Form hợp lệ | Tạo appointment pending | ✅ Pass |
| TC_APT_02 | Đặt lịch ngày quá khứ | Date < today | Validation error | ✅ Pass |
| TC_APT_03 | Customer xem lịch hẹn | Truy cập my-appointments | Hiện danh sách | ✅ Pass |
| TC_APT_04 | Agent xác nhận hẹn | Click Confirm | Status → confirmed | ✅ Pass |
| TC_APT_05 | Agent từ chối hẹn | Click Cancel | Status → cancelled | ✅ Pass |
| TC_APT_06 | Agent hoàn thành | Click Complete | Status → completed | ✅ Pass |

#### 6.1.4. Test Case Module Admin

| TC ID | Mô tả | Input | Expected Output | Kết quả |
|-------|-------|-------|-----------------|---------|
| TC_ADM_01 | Admin xem tin chờ duyệt | Truy cập pending | Danh sách tin pending | ✅ Pass |
| TC_ADM_02 | Admin duyệt tin | Click Approve | Status → approved | ✅ Pass |
| TC_ADM_03 | Admin từ chối tin | Click Reject | Status → rejected | ✅ Pass |
| TC_ADM_04 | Xem thống kê | Truy cập statistics | Hiện biểu đồ, bảng | ✅ Pass |
| TC_ADM_05 | Customer truy cập thống kê | URL /statistics/ | 403 hoặc redirect | ✅ Pass |

#### 6.1.5. Test Case Module Tin tức

| TC ID | Mô tả | Input | Expected Output | Kết quả |
|-------|-------|-------|-----------------|---------|
| TC_NEWS_01 | Xem danh sách tin tức | Truy cập /tin-tuc/ | Hiện bài published | ✅ Pass |
| TC_NEWS_02 | Xem chi tiết bài viết | Click vào bài | Hiện nội dung đầy đủ | ✅ Pass |
| TC_NEWS_03 | Tăng lượt xem | Truy cập chi tiết | views_count += 1 | ✅ Pass |
| TC_NEWS_04 | Lọc theo danh mục | Click category | Bài trong danh mục | ✅ Pass |
| TC_NEWS_05 | Tìm kiếm bài viết | Keyword search | Kết quả phù hợp | ✅ Pass |

#### 6.1.6. Test Case Upload ảnh

| TC ID | Mô tả | Input | Expected Output | Kết quả |
|-------|-------|-------|-----------------|---------|
| TC_UP_01 | Upload ảnh JPEG hợp lệ | File .jpg < 5MB | Upload thành công | ✅ Pass |
| TC_UP_02 | Upload ảnh PNG hợp lệ | File .png < 5MB | Upload thành công | ✅ Pass |
| TC_UP_03 | Upload file > 5MB | File 10MB | Validation error | ✅ Pass |
| TC_UP_04 | Upload file không phải ảnh | File .pdf | Validation error | ✅ Pass |
| TC_UP_05 | Preview ảnh trước upload | Chọn file | Hiện preview | ✅ Pass |

### 6.2. Kiểm thử giao diện (UI Testing)

| TC ID | Mô tả | Kết quả |
|-------|-------|---------|
| TC_UI_01 | Navbar hiển thị đúng menu theo role | ✅ Pass |
| TC_UI_02 | Footer luôn ở dưới khi ít nội dung | ✅ Pass |
| TC_UI_03 | Responsive trên mobile (375px) | ✅ Pass |
| TC_UI_04 | Responsive trên tablet (768px) | ✅ Pass |
| TC_UI_05 | Biểu đồ Chart.js render đúng | ✅ Pass |
| TC_UI_06 | Sticky sidebar không đè navbar | ✅ Pass |
| TC_UI_07 | Form validation hiện lỗi inline | ✅ Pass |
| TC_UI_08 | Message flash hiển thị đúng | ✅ Pass |

### 6.3. Kiểm thử bảo mật (Security Testing)

| TC ID | Mô tả | Kết quả |
|-------|-------|---------|
| TC_SEC_01 | CSRF token được kiểm tra | ✅ Pass |
| TC_SEC_02 | Password được hash (không plain text) | ✅ Pass |
| TC_SEC_03 | Unauthorized access bị chặn | ✅ Pass |
| TC_SEC_04 | SQL Injection (ORM tự escape) | ✅ Pass |
| TC_SEC_05 | XSS (template auto-escape) | ✅ Pass |

### 6.4. Kết quả kiểm thử

| Module | Tổng TC | Pass | Fail | Tỷ lệ |
|--------|---------|------|------|-------|
| Xác thực | 6 | 6 | 0 | 100% |
| Tin đăng | 10 | 10 | 0 | 100% |
| Lịch hẹn | 6 | 6 | 0 | 100% |
| Admin | 5 | 5 | 0 | 100% |
| Tin tức | 5 | 5 | 0 | 100% |
| Upload | 5 | 5 | 0 | 100% |
| UI | 8 | 8 | 0 | 100% |
| Security | 5 | 5 | 0 | 100% |
| **TỔNG** | **50** | **50** | **0** | **100%** |

---

## 7. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

### 7.1. Kết quả đạt được

Đề tài đã hoàn thành đầy đủ các mục tiêu đề ra:

**Về chức năng:**

| STT | Yêu cầu | Trạng thái |
|-----|---------|------------|
| 1 | Xác thực & phân quyền (đăng ký, đăng nhập, quên MK, 3 roles) | ✅ Hoàn thành |
| 2 | CRUD tin đăng + tìm kiếm/lọc/sắp xếp/phân trang | ✅ Hoàn thành |
| 3 | Nghiệp vụ duyệt tin (pending/approved/rejected) | ✅ Hoàn thành |
| 4 | Nghiệp vụ đặt lịch (pending/confirmed/completed/cancelled) | ✅ Hoàn thành |
| 5 | Thống kê với 2 biểu đồ + bảng tổng hợp | ✅ Hoàn thành |
| 6 | Upload ảnh an toàn (giới hạn 5MB, kiểm tra định dạng) | ✅ Hoàn thành |
| 7 | Module tin tức với CRUD, danh mục, tags | ✅ Hoàn thành |

**Về kỹ thuật:**
- Áp dụng mô hình MVT của Django
- Sử dụng Django ORM để tương tác database
- Tích hợp Bootstrap 5 cho giao diện responsive
- Sử dụng Chart.js cho biểu đồ thống kê
- Triển khai phân quyền dựa trên role

**Về giao diện:**
- Thiết kế hiện đại, thân thiện người dùng
- Tương thích đa thiết bị (responsive)
- Tham khảo giao diện từ batdongsan.com.vn

### 7.2. Hạn chế

- Chưa triển khai trên môi trường production
- Chưa có tính năng chat realtime giữa customer và agent
- Chưa hỗ trợ multiple images cho tin đăng
- Chưa có tính năng thông báo qua email/SMS
- Chưa tích hợp bản đồ Google Maps
- Chưa có tính năng so sánh tin đăng

### 7.3. Hướng phát triển

**Ngắn hạn (1-3 tháng):**
1. Triển khai production với PostgreSQL + Nginx + Gunicorn
2. Tích hợp email thông báo khi có lịch hẹn mới
3. Thêm tính năng upload nhiều ảnh cho tin đăng
4. Tích hợp Google Maps hiển thị vị trí BĐS

**Trung hạn (3-6 tháng):**
1. Phát triển REST API cho mobile app
2. Tích hợp chat realtime (WebSocket/Django Channels)
3. Thêm tính năng so sánh tin đăng
4. Tích hợp thanh toán trực tuyến (VNPay, Momo)

**Dài hạn (6-12 tháng):**
1. Phát triển mobile app (React Native/Flutter)
2. Tích hợp AI gợi ý tin đăng phù hợp
3. Phân tích dữ liệu và dự đoán xu hướng giá
4. Mở rộng quy mô với microservices

### 7.4. Tài liệu tham khảo

1. Django Documentation - https://docs.djangoproject.com/
2. Bootstrap 5 Documentation - https://getbootstrap.com/docs/5.0/
3. Chart.js Documentation - https://www.chartjs.org/docs/
4. Batdongsan.com.vn - Tham khảo giao diện
5. Python Documentation - https://docs.python.org/3/

---

## PHỤ LỤC

### A. Hướng dẫn cài đặt

```bash
# Clone project
git clone <repository_url>
cd BatDongSan

# Tạo virtual environment
python -m venv venv

# Kích hoạt venv (Windows)
venv\Scripts\activate

# Cài đặt dependencies
pip install django pillow

# Chạy migrations
python manage.py migrate

# Tạo superuser
python manage.py createsuperuser

# Chạy server
python manage.py runserver
```

### B. Tài khoản test

| Vai trò | Username | Password |
|---------|----------|----------|
| Admin | admin | admin |
| Agent | test1@gmail.com | test123456 |
| Customer | test2@gmail.com | test234567 |

### C. URL endpoints chính

| URL | Chức năng |
|-----|-----------|
| / | Trang chủ |
| /search/ | Tìm kiếm tin đăng |
| /listing/<id>/ | Chi tiết tin đăng |
| /listings/create/ | Đăng tin mới (Agent) |
| /my-listings/ | Tin đã đăng (Agent) |
| /appointment/<id>/ | Đặt lịch xem nhà |
| /my-appointments/ | Lịch hẹn của tôi |
| /agent-appointments/ | Lịch hẹn khách (Agent) |
| /pending-listings/ | Duyệt tin (Admin) |
| /statistics/ | Thống kê (Admin) |
| /tin-tuc/ | Danh sách tin tức |
| /tin-tuc/<slug>/ | Chi tiết bài viết |
| /accounts/login/ | Đăng nhập |
| /accounts/register/ | Đăng ký |
| /accounts/profile/ | Hồ sơ cá nhân |
| /admin/ | Django Admin |

---

**Ngày hoàn thành:** 23/01/2026

**Sinh viên thực hiện:** [Họ tên sinh viên]

**Giảng viên hướng dẫn:** [Họ tên giảng viên]
