from django.contrib import admin

# Register your models here.
from .models import Invoice,InvoiceBillSundry,InvoiceHeader,InvoiceItems

admin.site.register(Invoice)
admin.site.register(InvoiceBillSundry)
admin.site.register(InvoiceHeader)
admin.site.register(InvoiceItems)