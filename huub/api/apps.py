from django.apps import AppConfig

from .services import OrderService, DeliveryService

order_service: OrderService
delivery_service: DeliveryService


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        """
        Load services following singleton principle
        """
        global order_service, delivery_service

        order_service = OrderService().init()
        delivery_service = DeliveryService().init()
