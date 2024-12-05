from rest_framework import serializers
from .models import programmer
from .models import student
 
class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        #fields = ('fullname', 'nickname', 'age')
        fields = '__all__'
        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        #fields = ('fullname', 'nickname', 'age')
        fields = '__all__'