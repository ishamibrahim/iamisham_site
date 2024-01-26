from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from iamisham_site.settings import STATIC_URL
from django.template import loader
from django.http import HttpResponse
from rest_framework.response import Response
from iamisham_app.models import Test, TestQuestion, TestEvaluation, CorrectChoice
from iamisham_app.models import  Question
from iamisham_app.serializers import TestSerializer, QuestionAttendSerializer, AnswerSerializer
from rest_framework.viewsets import ViewSet
from rest_framework import status


# Create your views here.
def index(request):
    template = loader.get_template("iamisham_app/index.html")
    context = {
        "STATIC_URL": STATIC_URL
    }

    return HttpResponse(template.render(context, request))


class TestViewSet(ViewSet):
    queryset = Test.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        serializer = TestSerializer(self.queryset, many=True)
        return Response(serializer.data)


class TestAttendViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'])
    def attend(self, request, test_id):
        user = request.user
        queryset = Test.objects.all()
        test = get_object_or_404(queryset, id=test_id)
        test_questions = TestQuestion.objects.filter(test=test)
        questions_taken = TestEvaluation.objects.filter(user=user, test_question__test=test)


        if test_questions.count() == questions_taken.count():
            return Response({"message": "Test already taken; "
                                        "Please retake the test if you like"})

        if questions_taken:
            questions_taken_id_list = [tq.test_question.question.id
                                       for tq in questions_taken]

            test_question = test_questions.filter(~Q(question__id__in=questions_taken_id_list))\
                .select_related("question").prefetch_related("question__choices")\
                .first()
            question = test_question.question
            choices = test_question.question.choices.all()
        else:
            test_question = test_questions.first()
            question = test_question.question
            choices = test_question.question.choices.all()


        data = {'question_data': question, 'choices_data': choices}
        serializer = QuestionAttendSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'])
    def answer_question(self, request, test_id, question_id):
        user = request.user
        queryset = Test.objects.all()
        test = get_object_or_404(queryset, id=test_id)
        queryset = Question.objects.all()
        question_taken = get_object_or_404(queryset, id=question_id)

        test_question = TestQuestion.objects.get(test=test, question=question_taken)
        serializer = AnswerSerializer(data = request.data)
        if serializer.is_valid():
            evaluation = TestEvaluation.objects.create(user=user,
                                                       selected_choice_id=serializer.validated_data['choice_id'],
                                                       test_question=test_question)
            return Response({"message": f"Choice noted successfully for question {question_id}"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['post'])
    def evaluate_test(self, request, test_id):
        user = request.user
        queryset = Test.objects.all()
        test = get_object_or_404(queryset, id=test_id)
        tests_taken = TestEvaluation.objects.filter(user=user, test_question__test=test)
        tests_available = TestQuestion.objects.filter(test=test)
        if tests_taken.count() != tests_available.count():
            return Response({"message": "Test incomplete. Please complete the test before evaluation"},
                            status=status.HTTP_200_OK)
        correct_answers_count = 0
        for test_taken in tests_taken:
            correct_choice = CorrectChoice.objects.get(question=test_taken.test_question.question)
            if correct_choice.choice == test_taken.selected_choice:
                correct_answers_count += 1

        return Response({"message": f"Your score is {correct_answers_count}/{tests_taken.count()}"},
                            status=status.HTTP_200_OK)








