from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()

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
