# views.py
import json

from django.shortcuts import render

from apps.models import User
from apps.serializers import UserSerializer


def chat_view(request):
    users = User.objects.all()
    users = json.dumps(UserSerializer(instance=users, many=True).data)
    return render(request, 'chat.html', {'users_json': users})
