from rest_framework import serializers
from configuration.models import PaymentTerms

class PaymentTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTerms
        fields = [ 'id',
                    'description',
                    'dueDays',
                    'discountPercentage',
                    'discountDays',
                    'inactive', 
      ]