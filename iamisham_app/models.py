import uuid

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
USER = get_user_model()


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TestType(BaseModel):
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


class Question(BaseModel):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(BaseModel):
    question = models.ManyToManyField(Question, related_name='choices')
    choice_text = models.CharField(max_length=200, unique=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.choice_text )


class CorrectChoice(BaseModel):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'choice')

    def __str__(self):
        return f"{self.question.question_text} --> {self.choice.choice_text}"


class Test(BaseModel):
    name = models.CharField(max_length=300, null=False, blank=False)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TestQuestion(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_questions')

    class Meta:
        unique_together = ('question', 'test')

    def __str__(self):
        return "{} - {}".format(self.test.name, self.question.question_text[:30])


class TestEvaluation(BaseModel):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('test_question', 'user')

