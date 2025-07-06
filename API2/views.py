from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
# views.py
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 
# views.py
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def welcome_view(request):
    hour = datetime.now().hour
    if hour < 12:
        greeting = "صباح الخير 🌅"
    elif hour < 18:
        greeting = "مساء الخير 🌇"
    else:
        greeting = "سهرة طيبة 🌙"

    return Response({
        "message": f"{greeting} ومرحباً بك في منصة المدرسة الذكية 🎓",
        "tip": "تذكّر تسجّل حضورك اليوم 😉"
    })
