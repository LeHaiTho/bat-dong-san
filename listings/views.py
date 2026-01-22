from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Listing

def index(request):
    # Lấy tất cả tin, sắp xếp mới nhất lên đầu, giới hạn 6 tin
    listings = Listing.objects.order_by('-created_at')[:6] 
    
    context = {
        'listings': listings
    }
    return render(request, 'listings/index.html', context)

# <--- LẤY RA THÔNG TIN CỦA CĂN NHÀ
def listing(request, listing_id):
    # Tìm căn nhà có id bằng listing_id. Nếu không thấy thì báo lỗi 404
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)