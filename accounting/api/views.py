from rest_framework.viewsets import ModelViewSet
from accounting.models import  ChartAccounts, ItemServices, OpeningBalance, Invoice, Payments, Bills, Deposits
from accounting.api.serializers import  ChartAccountsSerializer, ItemServicesSerializer, OpeningBalanceSerializer, InvoiceSerializer, PaymentsSerializer, BillsSerializer, DepositsSerializer
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

class BaseModelViewSet(ModelViewSet):
    disabled_field = 'disabled'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance, self.disabled_field, True)
        instance.save()

        # Serialize the instance using the serializer class
        serializer = self.get_serializer(instance)
        serialized_data = serializer.data

        return Response(data=serialized_data, status=status.HTTP_200_OK)

class ChartAccountsApiViewSet(BaseModelViewSet):
    serializer_class = ChartAccountsSerializer
    queryset = ChartAccounts.objects.filter(disabled=False).all()
    filter_backends = [filters.SearchFilter]
    search_fields  = [ 'id', 
                      'name', 
                      'type',
                      'referenceNum', 
                      'balanceUSD', 
                      'currency', 
                      'parentAccount', 
                      'accountNumber', 
                      'note', 
                      'typeChart',
                      'disabled', 
                      ]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class ItemServicesApiViewSet(BaseModelViewSet):
    serializer_class = ItemServicesSerializer
    queryset = ItemServices.objects.filter(disabled=False).all()
    search_fields  = [ 'id', 
                    'code', 
                    'description', 
                    'accountName', 
                    'type', 
                    'amount', 
                    'autCreation', 
                    'currency', 
                    'iataCode',
                    'disabled',
                    ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OpeningBalanceApiViewSet(BaseModelViewSet):
    serializer_class = OpeningBalanceSerializer
    queryset = OpeningBalance.objects.filter(disabled=False).all()
    search_fields  = [ 'id', 
                    'name',
                    'balance',
                    'disabled',
                    ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InvoiceApiViewSet(BaseModelViewSet):
    serializer_class =InvoiceSerializer
    queryset = Invoice.objects.filter(disabled=False).all()
    search_fields  = [ 'id', 
                    'status',
                    'number',
                    'account',
                    'paymentTem',
                    'division',
                    'apply',        #verificar y borrar
                    'due',
                    'trasaDate',
                    'bilingAddres',
                    'paidAdd',
                    'exchangeRate',
                    'invoiceCharges',
                    'currency',
                    'issued_by',
                    'issuedByName',
                    'paymentById',
                    'paymentByDesc',
                    'accountById',
                    'accountByName',
                    'accountByType',
                    'disabled',
                    ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PaymentsApiViewSet(BaseModelViewSet):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.filter(disabled=False).all()
    search_fields  = [ 'id', 
                    'customerById',
                    'customerByName',
                    'amountReceived',
                    'trasaDate',
                    'number',
                    'memo',
                    'accountByType',
                    'accountById',
                    'accountRecei',
                    'accountByBankType',
                    'accountByBankId',
                    'accountReceiBank',
                    'disabled',
                    ]
    
    @api_view(['GET'])
    def filter_invoices_by_account_id(request, account_id):
        invoices = Invoice.objects.filter(accountById=account_id)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BillsApiViewSet(BaseModelViewSet):
    serializer_class = BillsSerializer
    queryset = Bills.objects.filter(disabled=False).all()
    search_fields  = [ 'id', 
                    'status',
                    'number',
                    'due',
                    'trasaDate',
                    'accountById',
                    'accountByType',
                    'carriVerndorById',
                    'carriVerndorByName',
                    'paymentById',
                    'paymentByDesc',
                    'billCharges',
                    'disabled',
                    ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DepositsApiViewSet(BaseModelViewSet):
    serializer_class = DepositsSerializer
    queryset = Deposits.objects.filter(disabled=False).all()
    search_fields  = [  'id', 
                        'bankAccount',
                        'date',
                        'memo',
                        'depositCharges'
                        'total',
                        'disabled',
                    ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
