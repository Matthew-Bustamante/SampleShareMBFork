# website/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.chat_id = self.scope['url_route']['kwargs']['chat_id']
		self.chat_group_name = f'chat_{self.chat_id}'

		# Join the chat group
		await self.channel_layer.group_add(
			self.chat_group_name,
			self.channel_name
		)

		await self.accept()

	async def disconnect(self, close_code):
		# Leave the chat group
		await self.channel_layer.group_discard(
			self.chat_group_name,
			self.channel_name
		)

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		user = self.scope['user'].username

		# Send the message to the chat group
		await self.channel_layer.group_send(
			self.chat_group_name,
			{
				'type': 'chat_message',
				'message': message,
				'user': user
			}
		)

	async def chat_message(self, event):
		message = event['message']
		user = event['user']

		# Send the message to WebSocket
		await self.send(text_data=json.dumps({
			'message': message,
			'user': user
		}))
