from django.db import models


class Faqs(models.Model):
    # song title
    question = models.TextField(null=False)
    # name of artist or group/band
    answer = models.TextField(null=False)

    def __str__(self):
        return "{} - {}".format(self.question, self.answer)