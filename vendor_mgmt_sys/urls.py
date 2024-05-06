from django.urls import path

from .views import VendorDetailView, VendorListView,PurchaseOrderListView, PurchaseOrderDetailView,VendorPerformanceView, AcknowledgePurchaseOrderView,On_time_delevery_rate

urlpatterns = [
    path('api/vendors/', VendorListView.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderListView.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
    path('api/test/<int:id>/', On_time_delevery_rate, name='acknowledge-delivery-rate'),
]
