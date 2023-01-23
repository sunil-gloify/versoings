from rest_framework import serializers
from myapp.models import *



class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields =  ('full_name','age' )
    
    def get_full_name(self, obj):
        return '{0} {1}'.format(obj.first_name, obj.last_name)
