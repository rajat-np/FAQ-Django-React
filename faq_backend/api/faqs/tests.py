from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Faqs
from .serializers import FaqsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_faq(question="", answer=""):
        if question != "" and answer != "":
            Faqs.objects.create(question=question, answer=answer)

    def setUp(self):
        # add test data
        self.create_faq("Will I get any certificate?", "No, wiztute tutors do not provide any certificate.")
        self.create_faq("Is it online learning ?", "Yes, the whole learning process will be online.")



class GetAllFaqsTest(BaseViewTest):

    def test_get_all_faqs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("faqs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Faqs.objects.all()
        serialized = FaqsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)