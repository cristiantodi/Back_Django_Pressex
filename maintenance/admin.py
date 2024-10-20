from django.contrib import admin
from maintenance.models import Carrier,Agent,Vendor,Customer,Employee,Port,PackageType,Location,Company,Shipper,PickUpLocation,Consignee,DeliveryLocation,ClientToBill, HazardousMaterial

from import_export import resources
from import_export.admin import ImportExportModelAdmin

##################### Classes assigned for import/export HERE #####################
################### Register your models here. #########################
class CarrierResource(resources.ModelResource):
    class Meta:
        model = Carrier
        
@admin.register(Carrier)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['name']
    list_display = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    resource_class = CarrierResource 

class AgentResource(resources.ModelResource):
    class Meta:
        model = Agent

@admin.register(Agent)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['name']
    list_display = ['id','name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    resource_class = AgentResource

class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor
@admin.register(Vendor)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['name']
    list_display = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    resource_class = VendorResource

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
@admin.register(Customer)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['name']
    list_display = ['id','name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    resource_class = CustomerResource

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
@admin.register(Employee)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    resource_class = EmployeeResource

class PortResource(resources.ModelResource):
    class Meta:
        model = Port
@admin.register(Port)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['code','name','method','country','sub_division','used','remarks','maritime','rail','road','air','mail','border_crossing','us_customs_code']
    resource_class = PortResource

class PackageTypeResource(resources.ModelResource):
    class Meta:
        model = PackageType
@admin.register(PackageType)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['description','length','height','width','weight','volume','max_weight','type','type_code','container_code','container_type','ground','air','ocean']
    resource_class = PackageTypeResource

class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
@admin.register(Location)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['status','code','description','empty','type','zone','length','width','height','volume','weight','max_weight','disabled']
    resource_class = LocationResource

class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
@admin.register(Company)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name','phone','mobile_phone','email','website','account_number','contact_first_name','contact_last_name','identification_number','division','street_and_number','city','state','country','zip_code','port',
                    'type_logistic_provider','type_distribution','type_airline_carrier','type_ocean_carrier','type_company_warehouse','company_iata_code','company_fmc_code','company_scac_code','company_tsa_code','company_img_name','company_img_logo']
    resource_class = CompanyResource

class ShipperResource(resources.ModelResource):
    class Meta:
        model = Shipper
@admin.register(Shipper)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['customer','vendor','agent']
    resource_class = ShipperResource

class PickUpLocationResource(resources.ModelResource):
    class Meta:
        model = PickUpLocation
@admin.register(PickUpLocation)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['customer','vendor','agent']
    resource_class = PickUpLocationResource

class ConsigneeResource(resources.ModelResource):
    class Meta:
        model = Consignee
@admin.register(Consignee)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['customer','vendor','agent','carrier']
    resource_class = ConsigneeResource

class DeliveryLocationResource(resources.ModelResource):
    class Meta:
        model = DeliveryLocation
@admin.register(DeliveryLocation)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['customer','vendor','agent','carrier']
    resource_class = DeliveryLocationResource

class ClientToBillResource(resources.ModelResource):
    class Meta:
        model = ClientToBill
@admin.register(ClientToBill)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['shipper','consignee']
    resource_class = ClientToBillResource

class HazardousMaterialResource(resources.ModelResource):
    class Meta:
        model = HazardousMaterial
@admin.register(HazardousMaterial)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['material_name','class_name']
    resource_class = HazardousMaterialResource