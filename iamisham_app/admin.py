from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from iamisham_app.models import Question, Test, TestType, TestQuestion, TestEvaluation,  Choice, CorrectChoice

admin.site.register(Question)
admin.site.register(TestType)
admin.site.register(TestQuestion)
admin.site.register(TestEvaluation)
admin.site.register(Choice)
admin.site.register(CorrectChoice)


class QuestionInline(admin.TabularInline):
    model = TestQuestion


class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('questions_list',)
    fields = ('name', 'test_type', 'questions_list')

    def questions_list(self, obj):
        test_questions = TestQuestion.objects.filter(test=obj)
        if test_questions.count() == 0:
            return '(None)'
        question_list = []
        for q in test_questions:
            question_list.append(q.question.question_text)
        return format_html(", \n".join(question_list))
    questions_list.short_description = 'Question(s)'



admin.site.register(Test, TestAdmin)
