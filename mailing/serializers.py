from rest_framework import serializers
from mailing.models import Mailing
from client.models import Client
from message.models import Message


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
