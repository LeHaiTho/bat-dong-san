# listings/validators.py
from django.core.exceptions import ValidationError
import os

# Định dạng ảnh được phép
ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'webp', 'gif']

# Kích thước tối đa (5MB)
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB in bytes


def validate_image_extension(value):
    """Kiểm tra định dạng file ảnh"""
    ext = os.path.splitext(value.name)[1].lower().replace('.', '')
    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            f'Định dạng file không được hỗ trợ. Chỉ chấp nhận: {", ".join(ALLOWED_IMAGE_EXTENSIONS)}'
        )


def validate_image_size(value):
    """Kiểm tra kích thước file ảnh"""
    if value.size > MAX_FILE_SIZE:
        max_size_mb = MAX_FILE_SIZE / (1024 * 1024)
        raise ValidationError(
            f'Kích thước file quá lớn. Tối đa cho phép: {max_size_mb:.0f}MB'
        )


def validate_image(value):
    """Validate cả định dạng và kích thước"""
    validate_image_extension(value)
    validate_image_size(value)
