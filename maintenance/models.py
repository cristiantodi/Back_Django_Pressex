from django.db import models


# Create your models here.
class Carrier(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    reference_number = models.CharField(max_length=200, blank=True, null=True)
    contact_first_name = models.CharField(max_length=200, blank=True, null=True)
    contact_last_name = models.CharField(max_length=200, blank=True, null=True)
    identification_number = models.CharField(max_length=200, blank=True, null=True)
    identification_type = models.CharField(max_length=200, blank=True, null=True)
    street_and_number = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    carrier_type = models.CharField(max_length=200, blank=True, null=True)
    method_code = models.CharField(max_length=200, blank=True, null=True)
    carrier_code = models.CharField(max_length=200, blank=True, null=True)
    scac_number = models.CharField(max_length=200, blank=True, null=True)
    iata_code = models.CharField(max_length=200, blank=True, null=True)
    airline_code = models.CharField(max_length=200, blank=True, null=True)
    airline_prefix = models.CharField(max_length=200, blank=True, null=True)
    airway_bill_number = models.TextField(blank=True, null=True)
    passenger_only_airline = models.BooleanField(default=False)
    type_person = models.CharField(max_length=200, blank=True, null=True, default="Carrier")
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    reference_number = models.CharField(max_length=200, blank=True, null=True)
    contact_first_name = models.CharField(max_length=200, blank=True, null=True)
    contact_last_name = models.CharField(max_length=200, blank=True, null=True)
    identification_number = models.CharField(max_length=200, blank=True, null=True)
    identification_type = models.CharField(max_length=200, blank=True, null=True)
    street_and_number = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    type_person = models.CharField(max_length=200, default="agent", blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    reference_number = models.CharField(max_length=200, blank=True, null=True)
    contact_first_name = models.CharField(max_length=200, blank=True, null=True)
    contact_last_name = models.CharField(max_length=200, blank=True, null=True)
    identification_number = models.CharField(max_length=200, blank=True, null=True)
    identification_type = models.CharField(max_length=200, blank=True, null=True)
    street_and_number = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    type_person = models.CharField(max_length=200, default="vendor", blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    reference_number = models.CharField(max_length=200, blank=True, null=True)
    contact_first_name = models.CharField(max_length=200, blank=True, null=True)
    contact_last_name = models.CharField(max_length=200, blank=True, null=True)
    identification_number = models.CharField(max_length=200, blank=True, null=True)
    identification_type = models.CharField(max_length=200, blank=True, null=True)
    street_and_number = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    type_person = models.CharField(max_length=200, default="customer", blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    reference_number = models.CharField(max_length=200, blank=True, null=True)
    contact_first_name = models.CharField(max_length=200, blank=True, null=True)
    contact_last_name = models.CharField(max_length=200, blank=True, null=True)
    identification_number = models.CharField(max_length=200, blank=True, null=True)
    identification_type = models.CharField(max_length=200, blank=True, null=True)
    street_and_number = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    type_person = models.CharField(max_length=200, default="employee", blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Port(models.Model):
    code = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    method = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    sub_division = models.CharField(max_length=200, blank=True, null=True)
    used = models.BooleanField(default=False, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    air = models.BooleanField(default=False, blank=True, null=True)
    maritime = models.BooleanField(default=False, blank=True, null=True)
    rail = models.BooleanField(default=False, blank=True, null=True)
    road = models.BooleanField(default=False, blank=True, null=True)
    mail = models.BooleanField(default=False, blank=True, null=True)
    border_crossing = models.BooleanField(default=False, blank=True, null=True)
    us_customs_code = models.CharField(max_length=200, blank=True, null=True)
    type_person = models.CharField(max_length=200, default="port", blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PackageType(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    max_weight = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    type_code = models.CharField(max_length=200, blank=True, null=True)
    container_code = models.CharField(max_length=200, blank=True, null=True)
    container_type = models.CharField(max_length=200, blank=True, null=True)
    ground = models.BooleanField(default=False, blank=True, null=True)
    air = models.BooleanField(default=False, blank=True, null=True)
    ocean = models.BooleanField(default=False, blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Location(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    empty = models.BooleanField(default=False, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    zone = models.CharField(max_length=200, blank=True, null=True)
    length = models.FloatField(max_length=200, blank=True, null=True)
    width = models.FloatField(max_length=200, blank=True, null=True)
    height = models.FloatField(max_length=200, blank=True, null=True)
    volume = models.FloatField(max_length=200, blank=True, null=True)
    weight = models.FloatField(max_length=200, blank=True, null=True)
    max_weight = models.FloatField(max_length=200, blank=True, null=True)
    disabled = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.code


class Company(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, default="none", blank=True, null=True)
    contact_first_name = models.CharField(max_length=200, blank=True, null=True)
    contact_last_name = models.CharField(max_length=200, blank=True, null=True)
    identification_number = models.CharField(max_length=200, blank=True, null=True)
    division = models.CharField(max_length=200, blank=True, null=True)
    street_and_number = models.TextField()
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    port = models.CharField(max_length=200, blank=True, null=True)
    type_logistic_provider = models.BooleanField(default=False)
    type_distribution = models.BooleanField(default=False)
    type_airline_carrier = models.BooleanField(default=False)
    type_ocean_carrier = models.BooleanField(default=False, blank=True, null=True)
    type_company_warehouse = models.BooleanField(default=False, blank=True, null=True)
    company_iata_code = models.CharField(max_length=200, blank=True, null=True)
    company_fmc_code = models.CharField(max_length=200, blank=True, null=True)
    company_scac_code = models.CharField(max_length=200, blank=True, null=True)
    company_tsa_code = models.CharField(max_length=200, blank=True, null=True)
    company_img_name = models.CharField(max_length=200, blank=True, null=True)
    company_img_logo = models.ImageField(upload_to="./logo", blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Shipper(models.Model):
    customerid = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='shipper_customer')
    vendorid = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING,
                               related_name='shipper_vendor')
    agentid = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='shipper_agent')
    data = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.customer:
            return self.customer.name
        elif self.vendor:
            return self.vendor.name
        elif self.agent:
            return self.agent.name
        else:
            return "N/A"


class Supplier(models.Model):
    customerid = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='supplier_customer')
    vendorid = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING,
                               related_name='supplier_vendor')
    agentid = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='supplier_agent')
    data = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.customer:
            return self.customer.name
        elif self.vendor:
            return self.vendor.name
        elif self.agent:
            return self.agent.name
        else:
            return "N/A"


class PickUpLocation(models.Model):
    customerid = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='pickup_customer')
    vendorid = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickup_vendor')
    agentid = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickup_agent')
    data = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.customer:
            return self.customer.name
        elif self.vendor:
            return self.vendor.name
        elif self.agent:
            return self.agent.name
        else:
            return "N/A"


class Consignee(models.Model):
    customerid = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='consignee_customer')
    vendorid = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING,
                               related_name='consignee_vendor')
    carrierid = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING,
                                related_name='consignee_carrier')
    agentid = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='consignee_agent')
    data = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.customer:
            return self.customer.name
        elif self.vendor:
            return self.vendor.name
        elif self.agent:
            return self.agent.name
        elif self.carrier:
            return self.carrier.name
        else:
            return "N/A"


class DeliveryLocation(models.Model):
    customerid = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='delivery_customer')
    vendorid = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING,
                               related_name='delivery_vendor')
    carrierid = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING,
                                related_name='delivery_carrier')
    agentid = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='delivery_agent')
    data = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.customer:
            return self.customer.name
        elif self.vendor:
            return self.vendor.name
        elif self.agent:
            return self.agent.name
        elif self.carrier:
            return self.carrier.name
        else:
            return "N/A"


class ClientToBill(models.Model):
    customerid = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='client_customer')
    vendorid = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='client_vendor')
    agentid = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='client_agent')
    carrierid = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING,
                                related_name='client_carrier')
    shipperid = models.CharField(max_length=200, blank=True, null=True)
    shipper = models.ForeignKey(Shipper, blank=True, null=True, on_delete=models.DO_NOTHING,
                                related_name='client_shipper')
    consigneeid = models.CharField(max_length=200, blank=True, null=True)
    consignee = models.ForeignKey(Consignee, blank=True, null=True, on_delete=models.DO_NOTHING,
                                  related_name='client_consignee')
    data = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.shipper:
            if self.customer:
                return self.customer.name
            elif self.vendor:
                return self.vendor.name
            elif self.agent:
                return self.agent.name
            else:
                return "N/A"
        elif self.consignee:
            if self.customer:
                return self.customer.name
            elif self.vendor:
                return self.vendor.name
            elif self.agent:
                return self.agent.name
            elif self.carrier:
                return self.carrier.name
            else:
                return "N/A"
        elif self.customer:
            return self.customer.name
        elif self.agent:
            return self.agent.name
        elif self.vendor:
            return self.vendor.name
        elif self.carrier:
            return self.carrier.name
        else:
            return "N/A"


class ReleasedTo(models.Model):
    customerid = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='releasedto_customer')
    vendorid = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING,
                               related_name='releasedto_vendor')
    carrierid = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING,
                                related_name='releasedto_carrier')
    agentid = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING,
                              related_name='releasedto_agent')
    data = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.customer:
            return self.customer.name
        elif self.vendor:
            return self.vendor.name
        elif self.agent:
            return self.agent.name
        elif self.carrier:
            return self.carrier.name
        else:
            return "N/A"


class HazardousMaterial(models.Model):
    material_name = models.CharField(max_length=200, blank=True, null=True)
    class_name = models.CharField(max_length=200, blank=True, null=True)
    disabled = models.BooleanField(default=False)
