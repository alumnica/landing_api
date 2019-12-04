from rest_framework import serializers
from .models import Contact, Suscriber



class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Contact        
        fields = ('name', 'phone',  'email', 'msg')


class SuscriberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Suscriber        
        fields = ('email',)