from rest_framework.routers import DefaultRouter
from accounting.api.views import  ChartAccountsApiViewSet, ItemServicesApiViewSet, OpeningBalanceApiViewSet, InvoiceApiViewSet, PaymentsApiViewSet, BillsApiViewSet, DepositsApiViewSet

router_accounting = DefaultRouter()

router_accounting.register(prefix='ChartAccounts', basename='ChartAccounts', viewset=ChartAccountsApiViewSet)
router_accounting.register(prefix='ItemServices', basename='ItemServices', viewset=ItemServicesApiViewSet)
router_accounting.register(prefix='OpeningBalance', basename='OpeningBalance', viewset=OpeningBalanceApiViewSet)
router_accounting.register(prefix='Invoice', basename='Invoice', viewset=InvoiceApiViewSet)
router_accounting.register(prefix='Payments', basename='Payments', viewset=PaymentsApiViewSet)
router_accounting.register(prefix='Bills', basename='Bills', viewset=BillsApiViewSet)
router_accounting.register(prefix='Deposits', basename='Deposits', viewset=DepositsApiViewSet)
