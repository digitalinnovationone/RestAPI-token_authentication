from rest_framework.serializers import ModelSerializer
from register.models import Register

class RegisterModelSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        