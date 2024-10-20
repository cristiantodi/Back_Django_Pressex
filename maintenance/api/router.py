from rest_framework.routers import DefaultRouter
from maintenance.api.views import CarrierApiViewSet, AgentApiViewSet, VendorApiViewSet, CustomerApiViewSet, EmployeeApiViewSet, PortApiViewSet, PackageTypeApiViewSet, LocationApiViewSet, CompanyApiViewSet, ShipperApiViewSet, PickUpLocationApiViewSet, ConsigneeApiViewSet, DeliveryLocationApiViewSet, ClientToBillApiViewSet, ReleasedToApiViewSet , SupplierApiViewSet, HazardousMaterialApiViewSet

router_maintenance = DefaultRouter()

router_maintenance.register(prefix='carrier', basename='carrier', viewset=CarrierApiViewSet)
router_maintenance.register(prefix='agent', basename='agent', viewset=AgentApiViewSet)
router_maintenance.register(prefix='vendor', basename='vendor', viewset=VendorApiViewSet)
router_maintenance.register(prefix='customer', basename='customer', viewset=CustomerApiViewSet)
router_maintenance.register(prefix='employee', basename='employee', viewset=EmployeeApiViewSet)
router_maintenance.register(prefix='port', basename='port', viewset=PortApiViewSet)
router_maintenance.register(prefix='packageType', basename='packageType', viewset=PackageTypeApiViewSet)
router_maintenance.register(prefix='location', basename='location', viewset=LocationApiViewSet)
router_maintenance.register(prefix='hazardousMaterials', basename='hazardousMaterials', viewset=HazardousMaterialApiViewSet)
router_maintenance.register(prefix='company', basename='company', viewset=CompanyApiViewSet)
router_maintenance.register(prefix='shipper', basename='shipper', viewset=ShipperApiViewSet)
router_maintenance.register(prefix='supplier', basename='supplier', viewset=SupplierApiViewSet)
router_maintenance.register(prefix='pickUpLocation', basename='pickUpLocation', viewset=PickUpLocationApiViewSet)
router_maintenance.register(prefix='consignee', basename='consignee', viewset=ConsigneeApiViewSet)
router_maintenance.register(prefix='deliveryLocation', basename='deliveryLocation', viewset=DeliveryLocationApiViewSet)
router_maintenance.register(prefix='clientToBill', basename='clientToBill', viewset=ClientToBillApiViewSet)
router_maintenance.register(prefix='releasedTo', basename='ReleasedTo', viewset=ReleasedToApiViewSet)
