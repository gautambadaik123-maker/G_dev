from django.urls import path
from . import views

urlpatterns = [
    # When someone goes to /api/quote/, run the random_quote function
    path('api/quote/', views.random_quote, name='random-quote'),
]
