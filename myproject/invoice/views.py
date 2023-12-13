from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework import generics
from .serializers import InvoiceHeaderSerializer,InvoiceSerializer
from .models import Invoice
from django.views.decorators.csrf import csrf_exempt



class InvoiceListCreate(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

@csrf_exempt
def create_invoice(request):
    if request.method=="POST":
        print(request)
        import pdb;pdb.set_trace()

    return JsonResponse({"message":"OK"})