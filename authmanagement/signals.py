# library 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()
# import 
from cart.models import Cart

@receiver (post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
	if created:
		try:
			print('created')
			Cart.objects.create(user=instance) 
		except:
			print('Not created')

@receiver (post_save, sender=User)
def save_cart(sender, instance, **kwargs):
	instance.cart.save() 


