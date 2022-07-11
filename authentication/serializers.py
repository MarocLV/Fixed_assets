from rest_framework import  serializers
from authentication.models import User

    

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
   
    
    class Meta:
         model = User
         fields = ['id', 'first_name', 'last_name', 'username']

         