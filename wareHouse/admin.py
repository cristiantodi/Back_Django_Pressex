from django.contrib import admin
from wareHouse.models import PickUpOrder, ReceptionOrder, ReleaseOrder


from import_export import resources
from import_export.admin import ImportExportModelAdmin

######################## Classes assigned for import/export. HERE ############################## 

class PickUpOrderResource(resources.ModelResource):
    class Meta:
        model = PickUpOrder

class ReceptionOrderResource(resources.ModelResource):
    class Meta:
        model = ReceptionOrder

class ReleaseOrderResource(resources.ModelResource):
    class Meta:
        model = ReleaseOrder

@admin.register(PickUpOrder)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'number',
                    'creation_date_text',
                    'pick_up_date_text',
                    'delivery_date_text',
                    'date',
                    'inland_carrier',
                    'main_carrier',
                    'issued_by',
                    'destination_agent',
                    'employee',
                    'shipper',
                    'pick_up_location',
                    'consignee',
                    'client_to_bill',
                    'delivery_location',
                    'pro_number',
                    'tracking_number',
                    'supplier',
                    'invoice_number',
                    'purchase_order_number',
                    'volumen',
                    'weight',
                ]
    resource_class = PickUpOrderResource


@admin.register(ReceptionOrder)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'number',
                    'creation_date',
                    'creation_date_text',
                    'employee',
                    'issued_by',
                    'destination_agent',
                    'shipper',
                    'consignee',
                    'client_to_bill',
                    'main_carrier',
                    'inland_carrier',
                    'commodities',
                    'events',
                    'attachments',
                    'volumen',
                    'weight',
                ]
    resource_class = ReceptionOrderResource


@admin.register(ReleaseOrder)
class warehouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'number', 
                    'clienTo',
                    'client_to_bill',
                    # 'creation_date', 
                    'creation_date_text',
                    # 'release_date', 
                    'release_date_text',
                    'employee', 
                    'issued_by', 
                    'carrier',
                    'warehouse_receipt', 
                    'consignee',
                    'pro_number', 
                    'tracking_number', 
                    'purchase_order_number', 
                    'commodities',
                    'notes',
                    'attachments',
                    ]
    resource_class = ReleaseOrderResource
