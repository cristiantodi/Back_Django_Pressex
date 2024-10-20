from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from maintenance.models import Carrier, Agent, Vendor, Customer, Employee, Port, PackageType, Location, Company, \
    Shipper, PickUpLocation, Consignee, DeliveryLocation, ClientToBill, ReleasedTo, Supplier, HazardousMaterial
from maintenance.api.serializers import CarrierSerializer, AgentSerializer, VendorSerializer, CustomerSerializer, \
    EmployeeSerializer, PortSerializer, PackageTypeSerializer, LocationSerializer, CompanySerializer, ShipperSerializer, \
    PickUpLocationSerializer, ConsigneeSerializer, DeliveryLocationSerializer, ClientToBillSerializer, \
    ReleasedToSerializer, SupplierSerializer, HazardousMaterialSerializer
from rest_framework.response import Response
from rest_framework import status


class BaseModelViewSet(ModelViewSet):
    disabled_field = 'disabled'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance, self.disabled_field, True)
        instance.save()
        return Response(data=instance, status=status.HTTP_200_OK)


class DataSendingMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CarrierApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = CarrierSerializer
    queryset = Carrier.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class AgentApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = AgentSerializer
    queryset = Agent.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class VendorApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CustomerApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class EmployeeApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class PortApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = PortSerializer
    queryset = Port.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'name']


class PackageTypeApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = PackageTypeSerializer
    queryset = PackageType.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'length', 'height', 'width', 'weight', 'volume', 'max_weight', 'type', 'type_code',
                     'container_code', 'container_type', 'ground', 'air', 'ocean']


class LocationApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = LocationSerializer
    queryset = Location.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'code', 'description', 'empty', 'type', 'zone', 'length', 'width', 'height', 'volume',
                     'weight', 'max_weight', 'disabled']


class CompanyApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ShipperApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = ShipperSerializer
    queryset = Shipper.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer', 'vendor', 'agent']


class SupplierApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer', 'vendor', 'agent']


class SupplierApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer', 'vendor', 'agent']


class PickUpLocationApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = PickUpLocationSerializer
    queryset = PickUpLocation.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer', 'vendor', 'agent']


class ConsigneeApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = ConsigneeSerializer
    queryset = Consignee.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer', 'vendor', 'agent', 'carrier']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeliveryLocationApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = DeliveryLocationSerializer
    queryset = DeliveryLocation.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer', 'vendor', 'agent', 'carrier']


class ClientToBillApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = ClientToBillSerializer
    queryset = ClientToBill.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['shipper', 'consignee']


class ReleasedToApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = ReleasedToSerializer
    queryset = ReleasedTo.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'customer', 'vendor', 'agent', 'carrier']


class HazardousMaterialApiViewSet(BaseModelViewSet, DataSendingMixin):
    serializer_class = HazardousMaterialSerializer
    queryset = HazardousMaterial.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['material_name', 'class_name']
