from django.db import models

class InvoiceHeader(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    InvoiceNumber=models.CharField(max_length=1000)
    CustomerName=models.CharField(max_length=1000)
    BillingAddress=models.CharField(max_length=1000)
    ShippingAddress=models.CharField(max_length=1000)
    GSTIN=models.CharField(max_length=1000)
    TotalAmount=models.FloatField()

class InvoiceItems(models.Model):
    itemName=models.CharField(max_length=1000)    
    Quantity=models.FloatField()
    Price=models.FloatField()
    Amount=models.FloatField()

class InvoiceBillSundry(models.Model):
    billSundryName=models.CharField(max_length=1000)    
    Amount=models.FloatField()

class Invoice(models.Model):
    invoiceNumber=models.CharField(max_length=100)
    invoice_headers=models.ManyToManyField(InvoiceHeader)
    invoice_items=models.ManyToManyField(InvoiceItems)
    invoice_bill_sundry=models.ManyToManyField(InvoiceBillSundry)
    timestamp=models.DateTimeField(auto_now_add=True)
