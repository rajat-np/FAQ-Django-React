from rest_framework import serializers
from .models import Faqs


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = ("question", "answer")