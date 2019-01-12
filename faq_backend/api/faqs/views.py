from rest_framework import generics
from .models import Faqs	
from .serializers import FaqsSerializer


class ListFaqsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Faqs.objects.all()
    serializer_class = FaqsSerializer