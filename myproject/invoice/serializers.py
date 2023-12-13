from rest_framework import serializers
from .models import InvoiceHeader,Invoice


class InvoiceHeaderSerializer(serializers.ModelSerializer):
    invoices=serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all(), many=True)
    class Meta:
        model=InvoiceHeader
        fields=("date","InvoiceNumber","CustomerName","BillingAddress","ShippingAddress","GSTIN","TotalAmount")


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_headers_list=InvoiceHeaderSerializer(many=True)
    class Meta:
        model=Invoice
        fields=("id","invoiceNumber","invoice_headers_list")
        