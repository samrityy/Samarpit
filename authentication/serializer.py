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
                         'username',
                         'firstname',
                         'lastname', 'phone_number', 'email',
                          'products','products_input','total_price'
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
    
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['firstname','lastname','username','password','email']
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self, validated_data):
        user=CustomUser.objects.create_user(**validated_data)
        return user

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'