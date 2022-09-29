from rest_framework import serializers
from appointments.models import Car,Appointment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    appointments = serializers.PrimaryKeyRelatedField(many=True, queryset = Appointment.objects.all())
    
    class Meta:
        model = User
        fields = ['id','username','appointments']


class AppointmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Appointment
        fields = ['customerName','date','car','owner']
        
        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields= ['carName']
