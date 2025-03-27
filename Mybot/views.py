from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_bot_reply

def chatbot_page(request):
    """Chatbot का Frontend Page Render करें"""
    return render(request, 'index.html')  # ✅ सही Template Load करें

def chatbot_response(request):
    """User Query ko Process karke Dataset se Response Dena"""
    user_query = request.GET.get('query', '').strip().lower()  # ✅ Query ko Lowercase me Convert karein
    
    if not user_query:
        return JsonResponse({"reply": "❌ Invalid Query. Please ask something."})

    bot_reply = get_bot_reply(user_query)  # ✅ Bot reply ko fetch karein
    
    return JsonResponse({"reply": bot_reply})  # ✅ Response return karein