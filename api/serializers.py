# library 
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()
# import 
from product.models import Product

# *********** start serializer for account create and update ************
class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'password', 'email',
				  'first_name', 'last_name'] 

	# create overwrite for password hashing and grouping
	def create(self, validated_data):
		new_user = User(**validated_data)
		new_user.password = make_password(validated_data.get('password'))
		new_user.save()
		return new_user

# *********** end serializer for account create and update ************

# *********** start serializer for product ************
class ProductSerializers(serializers.ModelSerializer):
	seller = UserSerializers(read_only=True)
	class Meta:
		model = Product
		fields = ['id', 'title', 'description', 'price',
				  'quantity', 'image', 'created_at', 'updated_at', 'seller'] 

	# create overwrite for password hashing and grouping
	def create(self, validated_data):
		current_user = self.context['request'].user
		validated_data['seller'] = current_user
		new_product = Product(**validated_data)
		new_product.save()
		return new_product

