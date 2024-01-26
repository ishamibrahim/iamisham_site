from abc import ABC

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from iamisham_app.models import Test, TestType, Choice, Question, TestQuestion


class TestTypeSerializer(ModelSerializer):
    class Meta:
        model = TestType
        fields = ['id', 'test_type']


class TestSerializer(ModelSerializer):
    test_type = TestTypeSerializer()

    class Meta:
        model = Test
        fields = ['id', 'name', 'test_type']


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class TestQuestionSerializer(ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = "__all__"


class QuestionAttendSerializer(Serializer):
    question_data = serializers.SerializerMethodField()
    choices_data = serializers.SerializerMethodField()

    def get_question_data(self, obj):
        question_szlr = QuestionSerializer(obj['question_data'])
        return question_szlr.data

    def get_choices_data(self, obj):
        choices_serializer = ChoiceSerializer(obj["choices_data"], many=True)
        return choices_serializer.data


class AnswerSerializer(Serializer):
    choice_id = serializers.IntegerField()
    choice_text = serializers.CharField(max_length=200)




