from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('add/<int:product_id>/', add_product, name="Add"),
    path('delete/<int:product_id>/', delete_product, name="Del"),
    path('substract/<int:product_id>/', substract_product, name="Sub"),
    path('clean_up/', clean_up_cart, name="Clean"),
    path('',index,name = "index"),
    path('products/',products,name = "products"),
    path('customizable/',customizable,name = "customizable"),
    path('filament/<int:brand>/',filament,name = "filament"),
    path('contact/',contact,name = "contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
