from rest_framework.routers import DefaultRouter
from configuration.api.views import PaymentTermsViewSet

router_configuration = DefaultRouter()

router_configuration.register(prefix='PaymentTerms', basename='PaymentTerms', viewset=PaymentTermsViewSet)