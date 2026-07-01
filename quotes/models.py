from django.db import models

class Quote(models.Model):
    # Just two pieces of data: the quote itself, and who said it
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.text
