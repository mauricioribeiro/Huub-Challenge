import json
import os


class AbstractService:
	payload: dict = {}
	source: str = None

	def init(self):
		"""
		Initialize service
		"""
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'payload')

		with open(os.path.join(path, f'{self.source}.json'), 'r') as f:
			self.payload = json.load(f)

		return self

	def get_all(self):
		"""
		Get all payload items
		:return: dict
		"""
		return self.payload


class OrderService(AbstractService):
	source: str = 'orders'


class DeliveryService(AbstractService):
	source: str = 'deliveries'
