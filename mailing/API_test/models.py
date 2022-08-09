from django.utils.timezone import now
from rest_framework.test import APITestCase
from mailing.models import Mailing
from client.models import Client
from message.models import Message


class TestModel(APITestCase):
    def creates_mailings(self):
        mailing = Mailing.objects.create(date_start=now(), date_end=now(), text='Simple text', time_start=now().time(), time_end=now().time(), tag='new',)
        self.assertIsInstance(mailing, Mailing)
        self.assertEqual(mailing.tag, 'new')

    def creates_clients(self):
        client = Client.objects.create(phone_number='79999999999', mobile_operator_code='123', tag='new', timezone='UTC')
        self.assertIsInstance(client, Client)
        self.assertEqual(client.phone_number, '79999999999')

    def creates_messages(self):
        self.creates_mailings()
        self.creates_clients()
        message = Message.objects.create(sending_status='No sent', mailing_id=1, client_id=1)
        self.assertIsInstance(message, Message)
        self.assertEqual(message.sending_status, 'No sent')
