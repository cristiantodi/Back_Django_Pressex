from rest_framework import serializers
from accounting.models import ChartAccounts, ItemServices, OpeningBalance, Invoice, Payments, Bills, Deposits
# from maintenance.api.serializers import AgentSerializer

class ChartAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ChartAccounts
        fields  = [ 'id', 
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
 
class ItemServicesSerializer(serializers.ModelSerializer):
    class Meta :
        model   = ItemServices
        fields  = ['id', 
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

class OpeningBalanceSerializer(serializers.ModelSerializer):
    class Meta :
        model   = OpeningBalance
        fields  = ['id', 
                    'name',
                    'balance',
                    'disabled',
                    ]

class InvoiceSerializer(serializers.ModelSerializer):
    # issued_byObj = AgentSerializer(required=False,source='issued_by', read_only=True, allow_null=True)
    class Meta :
        model   = Invoice
        fields   = ['id', 
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
                    # 'AgentSerializer',##########
                    # 'issued_by',
                    # 'issued_byObj'
                    ]
        
class PaymentsSerializer (serializers.ModelSerializer):
    class Meta :
        model   = Payments
        fields   = ['id', 
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

class BillsSerializer (serializers.ModelSerializer):
    class Meta :
        model   = Bills
        fields   = ['id', 
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

class DepositsSerializer (serializers.ModelSerializer):
    class Meta :
        model   = Deposits
        fields   = ['id', 
                    'bankAccount',
                    'date',
                    'memo',
                    'depositCharges',
                    'total',
                    'disabled',
                    ]