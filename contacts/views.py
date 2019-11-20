from django.shortcuts import render
from rest_framework.views import APIView
from .models import Contact, Suscriber
from .serializers import ContactSerializer, SuscriberSerializer
import itertools
from rest_framework.response import Response
from rest_framework import  status
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from collections import OrderedDict
import traceback 
from .email import send_mail_contact, send_mail_suscriber

# Create your views here.


class ContactAPI(APIView):

    def post(self, request,  format=None):
        try:
            print ('in contact')
            serializer = ContactSerializer(data=request.data)
            if serializer.is_valid():
                contacto = serializer.save()                
                send_mail_contact(contacto)
                return Response({}, status=status.HTTP_201_CREATED)
            else:            
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:            
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SuscriberAPI(APIView):

    def post(self, request,  format=None):
        try:
            print ('in suscriber')
            serializer = SuscriberSerializer(data=request.data)
            if serializer.is_valid():
                suscriber = serializer.save()
                send_mail_suscriber(suscriber)
                return Response({}, status=status.HTTP_201_CREATED)
            else:            
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:            
            print (traceback.format_exc())
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
