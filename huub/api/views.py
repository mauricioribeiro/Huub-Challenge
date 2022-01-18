from django.http import JsonResponse

from .apps import order_service


def order_view(request):
	"""
	View of /orders endpoint.
	Returns all orders with deliveries by given brand id
	:param request: Request
	:return: JsonResponse
	"""
	data = order_service.get_all()
	return JsonResponse(data=data)


def order_products_view(request):
	"""
	View of /orders/products endpoint.
	Returns all products and its quantity by given order id or reference
	:param request: Request
	:return: JsonResponse
	"""
	data = order_service.get_all()
	return JsonResponse(data=data)
