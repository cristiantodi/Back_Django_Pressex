from django.contrib import admin
from configuration.models import PaymentTerms

from import_export import resources
from import_export.admin import ImportExportModelAdmin

##################### Classes assigned for import/export HERE #####################

class paymentTermsResource(resources.ModelResource):
    class Meta:
        model = PaymentTerms

################### Register your models here. #########################

@admin.register(PaymentTerms)
class configurationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'description',
                    'dueDays',
                    'discountPercentage',
                    'discountDays',
                    'inactive',
    ]
    resource_class = paymentTermsResource 
