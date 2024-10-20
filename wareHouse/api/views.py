from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from wareHouse.models import  PickUpOrder, ReceptionOrder, ReleaseOrder
from wareHouse.api.serializers import PickUpOrderSerializer, ReceptionOrderSerializer, ReleaseOrderSerializer
from rest_framework import status
from rest_framework.response import Response

class BaseModelViewSet(ModelViewSet):
    disabled_field = 'disabled'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance, self.disabled_field, True)
        instance.save()
        return Response(data = instance,status=status.HTTP_200_OK)

class PickUpOrderApiViewSet(BaseModelViewSet):
    serializer_class = PickUpOrderSerializer
    queryset = PickUpOrder.objects.filter(disabled=False).select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','number','creation_date_text','pick_up_date_text','delivery_date_text','creation_date','pick_up_date','delivery_date','date','issued_by','destination_agent','employee','shipper','pick_up_location','consignee','delivery_location','inland_carrier','main_carrier','pro_number','tracking_number','supplier','invoice_number','purchase_order_number','volumen','weight',]

    def perform_create(self, serializer):

        last_pickup_order = PickUpOrder.objects.order_by('-number').first()
        if last_pickup_order:
            serializer.validated_data['number'] = last_pickup_order.number + 1
        else:
            serializer.validated_data['number'] = 1

        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReceptionOrderApiViewSet(BaseModelViewSet):
    serializer_class = ReceptionOrderSerializer
    queryset = ReceptionOrder.objects.filter(disabled=False).select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','number','creation_date','creation_date_text','employee','issued_by','destination_agent','shipper','consignee','client_to_bill','main_carrier', 'inland_carrier','commodities','events','attachments','volumen','weight',]

    def perform_create(self, serializer):

        last_reception_order = ReceptionOrder.objects.order_by('-number').first()
        if last_reception_order:
            serializer.validated_data['number'] = last_reception_order.number + 1
        else:
            serializer.validated_data['number'] = 1

        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReleaseOrderApiViewSet(BaseModelViewSet):
    serializer_class = ReleaseOrderSerializer
    queryset = ReleaseOrder.objects.filter(disabled=False).select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'number', 'creation_date', 'release_date', 'release_date_text', 'employee', 'employeeObj', 'issued_by', 'issued_byObj', 'client_to_bill', 'clientBillObj', 'carrier', 'mainz_carrierObj', 'warehouse_receipt', 'warehouseReceiptObj',  'consignee','pro_number', 'tracking_number', 'purchase_order_number', 'commodities','clienTo']

    def perform_create(self, serializer):

        last_release_order = ReleaseOrder.objects.order_by('-number').first()
        if last_release_order:
            serializer.validated_data['number'] = last_release_order.number + 1
        else:
            serializer.validated_data['number'] = 1

        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)