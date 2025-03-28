from django.urls import path
from .views import chatbot_page, chatbot_response

urlpatterns = [
    path('', chatbot_page, name='chatbot_page'),  # ✅ Frontend page
    path('get_response/', chatbot_response, name='chatbot_response'),  # ✅ API route
]
