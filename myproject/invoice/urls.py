from django.urls import path
from . import views
urlpatterns=[
    path("",views.InvoiceListCreate.as_view()),
    
    path("create/",views.create_invoice)

]