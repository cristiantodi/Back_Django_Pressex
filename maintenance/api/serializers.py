from rest_framework import serializers
from maintenance.models import (
    Carrier,
    Agent,
    Vendor,
    Customer,
    Employee,
    Port,
    PackageType,
    Location,
    Company,
    Shipper,
     Supplier,
    Supplier,
    PickUpLocation,
    Consignee,
    DeliveryLocation,
    ClientToBill,
    ReleasedTo,
    HazardousMaterial
)

from drf_extra_fields.fields import Base64ImageField


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = [
            "id",
            "name",
            "phone",
            "mobile_phone",
            "email",
            "fax",
            "website",
            "reference_number",
            "contact_first_name",
            "contact_last_name",
            "identification_number",
            "identification_type",
            "street_and_number",
            "city",
            "state",
            "country",
            "zip_code",
            "type_person",
            'disabled'
        ]


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = [
            "id",
            "name",
            "phone",
            "mobile_phone",
            "email",
            "fax",
            "website",
            "reference_number",
            "contact_first_name",
            "contact_last_name",
            "identification_number",
            "identification_type",
            "street_and_number",
            "city",
            "state",
            "country",
            "zip_code",
            "type_person",
        ]


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "phone",
            "mobile_phone",
            "email",
            "fax",
            "website",
            "reference_number",
            "contact_first_name",
            "contact_last_name",
            "identification_number",
            "identification_type",
            "street_and_number",
            "city",
            "state",
            "country",
            "zip_code",
            "type_person",
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "phone",
            "mobile_phone",
            "email",
            "fax",
            "website",
            "reference_number",
            "contact_first_name",
            "contact_last_name",
            "identification_number",
            "identification_type",
            "street_and_number",
            "city",
            "state",
            "country",
            "zip_code",
            "type_person",
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "name",
            "phone",
            "mobile_phone",
            "email",
            "fax",
            "website",
            "reference_number",
            "contact_first_name",
            "contact_last_name",
            "identification_number",
            "identification_type",
            "street_and_number",
            "city",
            "state",
            "country",
            "zip_code",
            "type_person",
        ]


class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = [
            "id",
            "code",
            "name",
            "method",
            "country",
            "sub_division",
            "used",
            "remarks",
            "maritime",
            "rail",
            "road",
            "air",
            "mail",
            "border_crossing",
            "us_customs_code",
        ]


class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = [
            "id",
            "description",
            "length",
            "height",
            "width",
            "weight",
            "volume",
            "max_weight",
            "type",
            "type_code",
            "container_code",
            "container_type",
            "ground",
            "air",
            "ocean",
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "status",
            "code",
            "description",
            "empty",
            "type",
            "zone",
            "length",
            "width",
            "height",
            "volume",
            "weight",
            "max_weight",
            "disabled",
        ]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "phone",
            "mobile_phone",
            "email",
            "website",
            "account_number",
            "contact_first_name",
            "contact_last_name",
            "identification_number",
            "division",
            "street_and_number",
            "city",
            "state",
            "country",
            "zip_code",
            "port",
            "type_logistic_provider",
            "type_distribution",
            "type_airline_carrier",
            "type_ocean_carrier",
            "type_company_warehouse",
            "company_iata_code",
            "company_fmc_code",
            "company_scac_code",
            "company_tsa_code",
            "company_img_name",
            "company_img_logo",
        ]


class ShipperSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = Shipper
        fields = [
            "id",
            "customer",
            "customerid",
            "vendor",
            "vendorid",
            "agent",
            "agentid",
            "data",
        ]

    def create(self, validated_data):
        customer_id = validated_data.pop("customerid", None)
        vendor_id = validated_data.pop("vendorid", None)
        agent_id = validated_data.pop("agentid", None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        # Almacena los datos recuperados como una propiedad JSON
        shipperObj = None
        if customer:
            shipperObj = CustomerSerializer(customer).data
        if vendor:
            shipperObj = VendorSerializer(vendor).data
        if agent:
            shipperObj = AgentSerializer(agent).data
        data = {"obj": shipperObj}

        # Crea el objeto Shipper con los datos proporcionados
        shipper = Shipper.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        shipper.data = data
        shipper.save()

        return shipper
    
class SupplierSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = Supplier
        fields = [
            "id",
            "customer",
            "customerid",
            "vendor",
            "vendorid",
            "agent",
            "agentid",
            "data",
        ]

    def create(self, validated_data):
        customer_id = validated_data.pop("customerid", None)
        vendor_id = validated_data.pop("vendorid", None)
        agent_id = validated_data.pop("agentid", None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        # Almacena los datos recuperados como una propiedad JSON
        supplierObj = None
        if customer:
            supplierObj = CustomerSerializer(customer).data
        if vendor:
            supplierObj = VendorSerializer(vendor).data
        if agent:
            supplierObj = AgentSerializer(agent).data
        data = {"obj": supplierObj}

        # Crea el objeto Shipper con los datos proporcionados
        supplier = Supplier.objects.create(**validated_data) #estaba shipper

        # Almacenar los datos JSON en un campo separado
        supplier.data = data
        supplier.save()

        return supplier

class PickUpLocationSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = PickUpLocation
        fields = [
            "id",
            "customer",
            "vendor",
            "agent",
            "customerid",
            "vendorid",
            "agentid",
            "data",
        ]

    def create(self, validated_data):
        customer_id = validated_data.pop("customerid", None)
        vendor_id = validated_data.pop("vendorid", None)
        agent_id = validated_data.pop("agentid", None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        # Almacena los datos recuperados como una propiedad JSON
        shipperObj = None
        if customer:
            shipperObj = CustomerSerializer(customer).data
        if vendor:
            shipperObj = VendorSerializer(vendor).data
        if agent:
            shipperObj = AgentSerializer(agent).data
        data = {"obj": shipperObj}

        # Crea el objeto Shipper con los datos proporcionados
        shipper = PickUpLocation.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        shipper.data = data
        shipper.save()

        return shipper


class ConsigneeSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)
    carrierid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = Consignee
        fields = [
            "id",
            "customer",
            "vendor",
            "agent",
            "carrier",
            "customerid",
            "vendorid",
            "agentid",
            "carrierid",
            "data",
        ]

    def create(self, validated_data):
        customer_id = validated_data.pop("customerid", None)
        vendor_id = validated_data.pop("vendorid", None)
        agent_id = validated_data.pop("agentid", None)
        carrier_id = validated_data.pop("carrierid", None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None
        carrier = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        if carrier_id:
            try:
                carrier = Carrier.objects.get(id=carrier_id)
            except Carrier.DoesNotExist:
                pass

                # Almacena los datos recuperados como una propiedad JSON
        shipperObj = None
        if customer:
            shipperObj = CustomerSerializer(customer).data
        if vendor:
            shipperObj = VendorSerializer(vendor).data
        if agent:
            shipperObj = AgentSerializer(agent).data
        if carrier:
            shipperObj = CarrierSerializer(carrier).data
        data = {"obj": shipperObj}

        # Crea el objeto Shipper con los datos proporcionados
        consignee = Consignee.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        consignee.data = data
        consignee.save()

        return consignee


class DeliveryLocationSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)
    carrierid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = DeliveryLocation
        fields = [
            "id",
            "customer",
            "vendor",
            "agent",
            "carrier",
            "customerid",
            "vendorid",
            "agentid",
            "carrierid",
            "data",
        ]

    def create(self, validated_data):
        customer_id = validated_data.pop("customerid", None)
        vendor_id = validated_data.pop("vendorid", None)
        agent_id = validated_data.pop("agentid", None)
        carrier_id = validated_data.pop("carrierid", None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None
        carrier = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        if carrier_id:
            try:
                carrier = Carrier.objects.get(id=carrier_id)
            except Carrier.DoesNotExist:
                pass

        shipperObj = None
        if customer:
            shipperObj = CustomerSerializer(customer).data
        if vendor:
            shipperObj = VendorSerializer(vendor).data
        if agent:
            shipperObj = AgentSerializer(agent).data
        if carrier:
            shipperObj = CarrierSerializer(carrier).data
        data = {"obj": shipperObj}

        # Crea el objeto Shipper con los datos proporcionados
        shipper = DeliveryLocation.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        shipper.data = data
        shipper.save()

        return shipper


class ClientToBillSerializer(serializers.ModelSerializer):
    shipperid = serializers.CharField(max_length=200, required=False, allow_null=True)
    shipperObj = ShipperSerializer(required=False,source='shipper', allow_null=True)
    consigneeid = serializers.CharField(max_length=200, required=False, allow_null=True)
    consigneeObj = ConsigneeSerializer(required=False,source='consignee', allow_null=True)
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    customerObj = CustomerSerializer(required = False, source='customer', allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentObj = AgentSerializer(required= False, source='agent', allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorObj = VendorSerializer(required= False, source='vendor', allow_null=True)
    carrierid = serializers.CharField(max_length=200, required=False, allow_null=True)
    carrierObj = CarrierSerializer(required= False, source='carrier', allow_null=True)

    class Meta:
        model = ClientToBill
        fields = [
        "id",
        "shipper",
        "shipperid",
        "shipperObj",
        "consignee",
        "consigneeid",
        "consigneeObj",
        "customerid",
        "customerObj",
        "agentid",
        "agentObj",
        "vendorid",
        "vendorObj",
        "carrierid",
        "carrierObj",
        "data",
    ]

    def create(self, validated_data):
        shipper_id = validated_data.pop("shipperid", None)
        consignee_id = validated_data.pop("consigneeid", None)
        customer_id = validated_data.pop("customerid", None)
        agent_id = validated_data.pop("agentid", None)
        vendor_id = validated_data.pop("vendorid", None)
        carrier_id = validated_data.pop("carrierid", None)
        # Buscar los objetos correspondientes en las tablas respectivas
        shipper = None
        consignee = None
        customer = None
        agent = None
        vendor = None
        carrier = None

        if shipper_id:
            try:
                shipper = Shipper.objects.get(id=shipper_id)
            except Shipper.DoesNotExist:
                pass

        if consignee_id:
            try:
                consignee = Consignee.objects.get(id=consignee_id)
            except Consignee.DoesNotExist:
                pass

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass
        
        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if carrier_id:
            try:
                carrier = Carrier.objects.get(id=carrier_id)
            except Carrier.DoesNotExist:
                pass
        

        # Almacena los datos recuperados como una propiedad JSON
        clientBillObj = None
        if shipper:
            clientBillObj = ShipperSerializer(shipper).data
        if consignee:
            clientBillObj = ConsigneeSerializer(consignee).data
        if customer:
            clientBillObj = CustomerSerializer(customer).data
        if agent:
            clientBillObj = AgentSerializer(agent).data
        if vendor:
            clientBillObj = VendorSerializer(vendor).data
        if carrier:
            clientBillObj = CarrierSerializer(carrier).data

        data = {"obj": clientBillObj}

        # Crea el objeto Shipper con los datos proporcionados
        clientBill = ClientToBill.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        clientBill.data = data
        clientBill.save()
        print("validated_data", validated_data,shipper,consignee, customer,agent, vendor, carrier)

        return clientBill



class ReleasedToSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)
    carrierid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = DeliveryLocation
        fields = [
            "id",
            "customer",
            "vendor",
            "agent",
            "carrier",
            "customerid",
            "vendorid",
            "agentid",
            "carrierid",
            "data",
        ]

    def create(self, validated_data):
        customer_id = validated_data.pop("customerid", None)
        vendor_id = validated_data.pop("vendorid", None)
        agent_id = validated_data.pop("agentid", None)
        carrier_id = validated_data.pop("carrierid", None)

        customer = None
        vendor = None
        agent = None
        carrier = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        if carrier_id:
            try:
                carrier = Carrier.objects.get(id=carrier_id)
            except Carrier.DoesNotExist:
                pass

        obj = None
        if customer:
            obj = CustomerSerializer(customer).data
        if vendor:
            obj = VendorSerializer(vendor).data
        if agent:
            obj = AgentSerializer(agent).data
        if carrier:
            obj = CarrierSerializer(carrier).data
        data = {"obj": obj}

        # Crea el objeto Shipper con los datos proporcionados
        releasedTo = ReleasedTo.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        releasedTo.data = data
        releasedTo.save()

        return releasedTo


class HazardousMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HazardousMaterial
        fields = '__all__'
