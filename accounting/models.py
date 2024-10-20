from django.db import models

from maintenance.models import Agent
from configuration.models import PaymentTerms
from maintenance.models import Customer, Vendor, Carrier

# Create your models here.

class ChartAccounts(models.Model):
    name            =   models.CharField(max_length=100, blank=True, null=True)
    type            =   models.CharField(max_length=100, blank=True, null=True)
    referenceNum    =   models.BigIntegerField(blank=True, null=True)
    balanceUSD      =   models.BigIntegerField(blank=True, null=True)
    currency        =   models.CharField(max_length=100, blank=True, null=True)
    parentAccount   =   models.CharField(max_length=100, blank=True, null=True)
    accountNumber   =   models.CharField(max_length=100, blank=True, null=True)
    note            =   models.CharField(max_length=100, blank=True, null=True)
    typeChart       =   models.CharField(max_length=100, blank=True, null=True)
    disabled        =   models.BooleanField(default=False)

class ItemServices(models.Model):
    code        =   models.CharField(max_length=100, blank=True, null=True)
    description =   models.CharField(max_length=200, blank=True, null=True)
    accountName =   models.CharField(max_length=200, blank=True, null=True)
    type        =   models.CharField(max_length=100, blank=True, null=True)
    amount      =   models.FloatField(blank=True, null=True)
    autCreation =   models.CharField(max_length=100, blank=True, null=True)
    currency    =   models.CharField(max_length=100, blank=True, null=True)
    iataCode    =   models.CharField(max_length=100, blank=True, null=True)
    disabled    =   models.BooleanField(default=False)
  
class OpeningBalance(models.Model):
    name        =   models.CharField(max_length=100, blank=True, null=True)
    balance     =   models.FloatField(blank=True, null=True)
    disabled    =   models.BooleanField(default=False)

class Invoice(models.Model):
    status          =   models.CharField(max_length=200, blank=True, null=True)
    number          =   models.CharField(max_length=200, blank=True, null=True)
    account         =   models.CharField(max_length=200, blank=True, null=True)#Borrar
    paymentTem      =   models.CharField(max_length=200, blank=True, null=True)
    division        =   models.CharField(max_length=200, blank=True, null=True)
    apply           =   models.CharField(max_length=200, blank=True, null=True)   #Verificar y borrar
    due             =   models.DateTimeField(blank=True, null=True)
    trasaDate       =   models.DateTimeField(blank=True, null=True)
    bilingAddres    =   models.TextField(blank=True, null=True)
    currency        =   models.CharField(max_length=200, blank=True, null=True)
    issued_by       =   models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING)
    issuedByName    =   models.CharField(max_length=200, blank=True, null=True)
    invoiceById         =   models.CharField(max_length=200, blank=True, null=True)
    invoiceBydescription=   models.CharField(max_length=200, blank=True, null=True)
    paymentById     =   models.ForeignKey(PaymentTerms, blank=True, null=True, on_delete=models.DO_NOTHING)
    paymentByDesc   =   models.CharField(max_length=200, blank=True, null=True)
    accountByType   =   models.CharField(max_length=200, blank=True, null=True)
    accountById     =   models.ForeignKey(ChartAccounts, blank=True, null=True, on_delete=models.DO_NOTHING)
    accountByName   =   models.CharField(max_length=200, blank=True, null=True)
    typeByCode      =   models.CharField(max_length=200, blank=True, null=True)
    typeService     =   models.CharField(max_length=200, blank=True, null=True)
    paidAdd         =   models.CharField(max_length=200, blank=True, null=True)
    exchangeRate    =   models.BigIntegerField(blank=True, null=True)
    invoiceCharges  =   models.JSONField(blank=True, null=True)
    disabled        =   models.BooleanField(default=False)

class Payments(models.Model):
    customerById    =   models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING)
    customerByName  =   models.CharField(max_length=200, blank=True, null=True)
    amountReceived  =   models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    trasaDate       =   models.DateTimeField(blank=True, null=True)
    number          =   models.CharField(max_length=200, blank=True, null=True)
    memo            =   models.CharField(max_length=200, blank=True, null=True)
    accountByType   =   models.CharField(max_length=200, blank=True, null=True)
    accountById     =   models.ForeignKey(ChartAccounts, blank=True, null=True, on_delete=models.DO_NOTHING)
    accountRecei    =   models.CharField(max_length=200, blank=True, null=True)
    accountByBankType   =   models.CharField(max_length=200, blank=True, null=True)
    accountByBankId     =   models.ForeignKey(ChartAccounts, blank=True, null=True, on_delete=models.DO_NOTHING,related_name='accountByBankId')
    accountReceiBank    =   models.CharField(max_length=200, blank=True, null=True)
    disabled            =   models.BooleanField(default=False)

class Bills(models.Model): 
    status          =   models.CharField(max_length=200, blank=True, null=True)
    number          =   models.CharField(max_length=200, blank=True, null=True)
    due             =   models.DateTimeField(blank=True, null=True)
    trasaDate       =   models.DateTimeField(blank=True, null=True)
    accountById     =   models.ForeignKey(ChartAccounts, blank=True, null=True, on_delete=models.DO_NOTHING)
    accountByType   =   models.CharField(max_length=200, blank=True, null=True)
    carriVerndorById=   models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING)
    carriVerndorByName=   models.CharField(max_length=200, blank=True, null=True)
    paymentById     =   models.ForeignKey(PaymentTerms, blank=True, null=True, on_delete=models.DO_NOTHING)
    paymentByDesc   =   models.CharField(max_length=200, blank=True, null=True)
    billCharges     =   models.JSONField(blank=True, null=True)
    disabled        =   models.BooleanField(default=False)  
    
class Deposits(models.Model): 
    bankAccount     =   models.CharField(max_length=200, blank=True, null=True)
    date            =   models.DateTimeField(blank=True, null=True)
    memo            =   models.CharField(max_length=200, blank=True, null=True)
    depositCharges  =   models.JSONField(blank=True, null=True)
    total           =   models.CharField(max_length=200, blank=True, null=True)
    disabled        =   models.BooleanField(default=False)