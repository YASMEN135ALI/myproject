from rest_framework import serializers
from .models import Student




# serializers.py
class StudentSerializer(serializers.ModelSerializer):
    average = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'score_math', 'score_science', 'score_language', 'average', 'status']

    def get_average(self, obj):
        return round(obj.average_score(), 2)

    def get_status(self, obj):
        avg = obj.average_score()
        if avg >= 90:
            return "ممتاز جداً 💯"
        elif avg >= 75:
            return "جيد جداً ✨"
        elif avg >= 60:
            return "مقبول 😊"
        else:
            return "يحتاج دعم 🧠"
