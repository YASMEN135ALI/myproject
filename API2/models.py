from django.db import models

# Create your models here.
# models.py
class Student(models.Model):
    name = models.CharField(max_length=100)
    score_math = models.FloatField()
    score_science = models.FloatField()
    score_language = models.FloatField()

    def average_score(self):
        return (self.score_math + self.score_science + self.score_language) / 3
