
from django.urls import path
from .views import ListFaqsView


urlpatterns = [
    path('faqs/', ListFaqsView.as_view(), name="faqs-all")
]
