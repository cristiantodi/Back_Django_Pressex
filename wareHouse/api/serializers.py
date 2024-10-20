from rest_framework import serializers

from wareHouse.models import  PickUpOrder, ReceptionOrder, ReleaseOrder
from maintenance.api.serializers import AgentSerializer,CustomerSerializer,EmployeeSerializer,CarrierSerializer, ShipperSerializer,PickUpLocationSerializer,ConsigneeSerializer,DeliveryLocationSerializer,ClientToBillSerializer, ReleasedToSerializer,SupplierSerializer



class PickUpOrderSerializer(serializers.ModelSerializer):
    issued_byObj = AgentSerializer(required=False,source='issued_by', read_only=True, allow_null=True)
    destination_agentObj = AgentSerializer(required=False,source='destination_agent', read_only=True, allow_null=True)
    employeeObj = EmployeeSerializer(required=False,source='employee', read_only=True, allow_null=True)
    shipperObj = ShipperSerializer(required=False,source='shipper', read_only=True, allow_null=True)
    pickUpLocationObj = PickUpLocationSerializer(required=False,source='pick_up_location', read_only=True, allow_null=True)
    consigneeObj = ConsigneeSerializer(required=False,source='consignee', read_only=True, allow_null=True)
    deliveryLocationObj = DeliveryLocationSerializer(required=False,source='delivery_location', read_only=True, allow_null=True)
    inland_carrierObj = CarrierSerializer(required=False,source='inland_carrier', read_only=True, allow_null=True)
    main_carrierObj = CarrierSerializer(required=False,source='main_carrier', read_only=True, allow_null=True)
    supplierObj = CustomerSerializer(required=False,source='supplier', read_only=True, allow_null=True)
    client_to_billObj = ClientToBillSerializer(required=False, source= 'client_to_bill', read_only=True, allow_null=True)
    
    class Meta:
        model = PickUpOrder
       
        fields = [ 'id', 'status','number','creation_date_text','pick_up_date_text','delivery_date_text','creation_date','pick_up_date','delivery_date','date','issued_by','issued_byObj','destination_agent','destination_agentObj','employee','employeeObj','shipper','shipperObj','pick_up_location','pickUpLocationObj','consignee','consigneeObj','delivery_location','deliveryLocationObj','inland_carrier','inland_carrierObj','main_carrier','main_carrierObj','pro_number','tracking_number','supplier','supplierObj','invoice_number','purchase_order_number', 'commodities', 'client_to_bill', 'client_to_billObj', 'charges','volumen','weight',]
 
class ReceptionOrderSerializer(serializers.ModelSerializer):
    issued_byObj = AgentSerializer(required=False,source='issued_by', read_only=True)
    destination_agentObj = AgentSerializer(required=False,source='destination_agent', read_only=True)
    shipperObj = ShipperSerializer(required=False,source='shipper', read_only=True)
    consigneeObj = ConsigneeSerializer(required=False,source='consignee', read_only=True)
    clientBillObj = ClientToBillSerializer(required=False,source='client_to_bill', read_only=True)
    main_carrierObj = CarrierSerializer(required=False,source='main_carrier', read_only=True)
    inland_carrierObj = CarrierSerializer(required=False,source='inland_carrier', read_only=True, allow_null=True)
    employeeObj = EmployeeSerializer(required=False, source='employee', read_only=True)
    supplierObj = SupplierSerializer(required=False,source='supplier' , read_only=True)
    class Meta:
        model = ReceptionOrder
        fields = [  'id', 'status','number','creation_date','creation_date_text','employee', 'employeeObj', 'issued_by','issued_byObj','destination_agent','destination_agentObj','shipper','shipperObj','consignee', 'consigneeObj','client_to_bill','clientBillObj','main_carrier','main_carrierObj','inland_carrier','inland_carrierObj','commodities','events','attachments', 'notes', 'charges', 'pro_number', 'tracking_number', 'invoice_number', 'purchase_order_number', 'supplier', 'supplierObj','volumen','weight','pickup_order_id',]

class ReleaseOrderSerializer(serializers.ModelSerializer):
    issued_byObj = AgentSerializer(required=False,source='issued_by', read_only=True)
    clientBillObj = ClientToBillSerializer(required=False,source='client_to_bill', read_only=True)
    inland_carrierObj = CarrierSerializer(required=False,source='carrier', read_only=True)
    employeeObj = EmployeeSerializer(required=False, source='employee', read_only=True)
    warehouseReceiptObj = PickUpOrderSerializer(required=False, source='warehouse_receipt', read_only=True)
    consigneeObj = ConsigneeSerializer(required=False,source='consignee', read_only=True)
    class Meta:
        model = ReleaseOrder
        fields = ['id', 'status', 'number','creation_date', 'creation_date_text', 'release_date', 'release_date_text','employee', 'employeeObj', 'issued_by', 'issued_byObj', 'client_to_bill', 'clientBillObj', 'carrier', 'inland_carrierObj', 'warehouse_receipt', 'warehouseReceiptObj', 'consignee', 'consigneeObj', 'pro_number', 'tracking_number', 'purchase_order_number', 'commodities', 'disabled','attachments', 'notes', 'clienTo','wh_receipt_id',]