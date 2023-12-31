from rest_framework import serializers
from .models import CustomUser,Products
class UserSerializer(serializers.ModelSerializer):
    products=serializers.SerializerMethodField()
    products_input=serializers.ListField(write_only=True,
        child= serializers.CharField())

    def get_products(self, obj):
        if obj.products:
           return [product.name for product in obj.products.all()]
        return None             
    class Meta:
        model=CustomUser
        fields= ['id', 
                         'firstname','email',
                         'lastname', 'phone_number',
                          'products','products_input','total_price',
                           ]
    def create(self, validated_data):
        products_data = validated_data.pop('products_input',[ ])
        print(f'Products Input: {products_data}')
        obj = super().create(validated_data)

        for product_name in products_data:
            product_instance, created = Products.objects.get_or_create(name=product_name)
            obj.products.add(product_instance)
            print(f'Products Input: {products_data}')
        return obj
    
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    class Meta:
        model=CustomUser
        fields=['email','username','password','phone_number']
    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')
        phone_number=attrs.get('phone_number','')
        if not username.isalnum():
            raise serializers.ValidationError('the user name must only contain alphanumeric character')
        return attrs
    
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)
        
        
       
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'

class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=55)

    class Meta:
        model=CustomUser
        fields=['token']