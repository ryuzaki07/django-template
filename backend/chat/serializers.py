from rest_framework import serializers
from chat.models import Chat


class Chatserializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
