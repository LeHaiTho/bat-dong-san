# Website Bất Động Sản - Django

Website đăng tin mua bán, cho thuê bất động sản với đầy đủ chức năng quản lý.
## Hướng dẫn chạy

### Yêu cầu
- Python 3.10+
- pip

### Cài đặt

```bash
# Clone project
cd BatDongSan

# Tạo virtual environment
python -m venv venv

# Kích hoạt venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Cài đặt dependencies
pip install django pillow

# Chạy migrations
python manage.py migrate

# Tạo superuser (admin)
python manage.py createsuperuser

# Chạy server
python manage.py runserver
```

### Truy cập
- **Website**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## Phân quyền người dùng

| Vai trò | Quyền hạn |
|---------|-----------|
| Customer | Xem tin, đặt lịch xem nhà, quản lý lịch hẹn cá nhân |
| Agent | Như Customer + Đăng tin, quản lý tin đăng, xử lý lịch hẹn khách |
| Admin | Toàn quyền + Duyệt tin, thống kê, quản lý tin tức |

## Cấu trúc dự án

```
BatDongSan/
├── core/           # Settings, URLs chính
├── listings/       # App quản lý tin BĐS
├── accounts/       # App xác thực, profile
├── news/           # App tin tức
├── templates/      # Templates chung (base.html)
├── media/          # Upload files
└── manage.py
```

## Chức năng chính

### Listings (Tin BĐS)
- CRUD tin đăng (Agent)
- Tìm kiếm, lọc theo: loại, danh mục, giá, diện tích, địa chỉ
- Sắp xếp theo: mới nhất, giá, diện tích
- Phân trang
- Duyệt tin (Admin)

### Appointments (Lịch hẹn)
- Đặt lịch xem nhà
- Trạng thái: Chờ xác nhận → Đã xác nhận → Hoàn thành/Hủy
- Agent xử lý lịch hẹn

### Statistics (Thống kê - Admin)
- Biểu đồ tin theo tháng
- Biểu đồ tin theo danh mục
- Bảng tổng hợp

### News (Tin tức - Admin)
- CRUD bài viết
- Danh mục, tags
- Bài viết nổi bật
- Đếm lượt xem

## Tài khoản test
Admin:
tài khoản: admin
mật khẩu : admin
Agent: 
tài khoản: test1@gmail.com
mật khẩu : test123456
Customer:
tài khoản: test2@gmail.com
mật khẩu : test234567
Sau khi tạo superuser, vào Admin để:
1. Tạo thêm user với các role khác nhau
2. Tạo Category cho listings
3. Tạo tin BĐS mẫu
4. Tạo danh mục và bài viết tin tức

---
**Tech Stack**: Django 5.2 | SQLite | Bootstrap 5 | Chart.js
