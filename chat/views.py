# views.py
from django.shortcuts import render

from apps.models import User


def chat_view(request):
    users = User.objects.exclude(id=request.user.id).values(
        'username', 'fullname', 'is_online', 'last_message', 'last_message_time')
    return render(request, 'chat.html', {'users_json': users})
