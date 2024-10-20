from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from configuration.models import PaymentTerms
from configuration.api.serializers import PaymentTermsSerializer
from rest_framework import status
from rest_framework.response import Response

class BaseModelViewSet(ModelViewSet):
    disabled_field = 'disabled'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance, self.disabled_field, True)
        instance.save()
        return Response(data = instance,status=status.HTTP_200_OK)

class PaymentTermsViewSet(BaseModelViewSet):
    serializer_class = PaymentTermsSerializer
    queryset = PaymentTerms.objects.filter(disabled=False).all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
                    'id',
                    'description',
                    'dueDays',
                    'discountPercentage',
                    'discountDays',
                    'inactive', 
                ]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)