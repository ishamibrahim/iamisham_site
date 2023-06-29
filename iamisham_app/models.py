from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class TestType(models.Model):
    BASIC = "BASIC"
    INTERIM = "INTERIM"
    ADVANCED = "ADVANCED"

    TEST_TYPE = (
        (BASIC, BASIC),
        (INTERIM, INTERIM),
        (ADVANCED, ADVANCED)
    )
    test_type = models.CharField(max_length=100, choices=TEST_TYPE, default=BASIC)

    def __str__(self):
        return self.test_type


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('choice_text', 'question')

    def __str__(self):
        return "{} - {}".format(self.choice_text, self.question.question_text[:70])


class Test(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TestQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('question', 'test')

    def __str__(self):
        return "{} - {}".format(self.test.name, self.question.question_text[:30])


class TestEvaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('test_question', 'user')

