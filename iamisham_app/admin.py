from django.contrib import admin

# Register your models here.
from iamisham_app.models import Question, Test, TestType, TestQuestion, TestEvaluation,  Choice

admin.site.register(Question)
admin.site.register(Test)
admin.site.register(TestType)
admin.site.register(TestQuestion)
admin.site.register(TestEvaluation)
admin.site.register(Choice)
