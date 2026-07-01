from django.http import JsonResponse
from .models import Quote
import random

def random_quote(request):
    # Get all quotes from the database
    all_quotes = list(Quote.objects.values('text', 'author'))
    
    # Pick a random one, or show a default message if the database is empty
    if all_quotes:
        selected_quote = random.choice(all_quotes)
    else:
        selected_quote = {"text": "Keep going!", "author": "Unknown"}
    
    return JsonResponse(selected_quote)
