from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_bot_reply

def chatbot_page(request):
    """Chatbot Page Render karega"""
    return render(request, 'index.html')

def chatbot_response(request):
    """User Query ko Process karega aur Response return karega"""
    user_query = request.GET.get('query', '').strip().lower()

    if not user_query:
        return JsonResponse({"reply": "❌ Invalid Query. Please ask something."}, status=400)

    bot_reply = get_bot_reply(user_query)
    return JsonResponse({"reply": bot_reply})  # ✅ JSON format me response dega
