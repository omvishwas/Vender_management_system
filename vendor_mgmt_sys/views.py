from django.shortcuts import render
from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponse



class VendorDetailView(APIView):
    """
    Retrieve, update or delete a vendor instance.
    """
    def get(self, request, pk):
        try:
            vendor = Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            vendor = Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            vendor = Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class VendorListView(ListAPIView):

    def get(self, request):
        try:
            vendor = Vendor.objects.all()
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = VendorSerializer(vendor,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PurchaseOrderCreateView(generics.CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderListView(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get(self, request):
        try:
            purchaseorder = PurchaseOrder.objects.all()
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PurchaseOrderSerializer(purchaseorder,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate
        }
        return Response(data)
    
class AcknowledgePurchaseOrderView(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)

        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)
    
def On_time_delevery_rate(request,id):
    #id=request["id"]
    # print(request)
    total_completed_orders = PurchaseOrder.objects.filter(vendor=id, status='completed').count()
    print(total_completed_orders)

    completed_on_time_orders = PurchaseOrder.objects.filter(
        vendor=id,
        status='completed',
        acknowledgement_date__lte=delivery_date 
    ).count()
    print(completed_on_time_orders)


    if total_completed_orders > 0:
        on_time_delivery_rate = completed_on_time_orders / total_completed_orders
    else:
        on_time_delivery_rate = 0
    return HttpResponse(on_time_delivery_rate)