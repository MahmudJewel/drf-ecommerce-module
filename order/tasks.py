from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Order, DailyData

@shared_task
def calculate_daily_revenue():
	try:
		end_date = timezone.now()
		start_date = end_date - timedelta(days=1)
		orders_today = Order.objects.filter(created_at__range=(start_date, end_date))
		total_revenue = sum(order.total_price for order in orders_today)
		print('Total reveneue ==> ', total_revenue)
		# Save daily revenue data
		DailyData.objects.create(date=start_date.date(), total_revenue=total_revenue)
		print('data saved =============> ')
		return 'Daily revenue calculation successful'
	except Exception as e:
		print('error ========> calculate_daily_revenue', e)
		return 'Invalid header found.'
