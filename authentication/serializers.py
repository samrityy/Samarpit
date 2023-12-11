from rest_framework import serializers
from .models import CustomUser,Products
class UserSerializer(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()
    product_input=serializers.ListField(write_only=True,
        child= serializers.CharField())

    def get_product(self,obj):
        return[product.name for product in obj.product.all()]                         
    class Meta:
        model=CustomUser
        fields= ['id', 
                         'username',
                         'firstname',
                         'lastname', 'phone_number', 'email',
                          'products','product_input',
                           ]

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['firstname','lastname','username','password','email']
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self, validated_data):
        user=CustomUser.objects.create_user(**validated_data)
        return user
