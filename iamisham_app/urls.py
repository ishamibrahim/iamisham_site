from django.urls import path, include

from iamisham_app.views import TestViewSet, TestAttendViewSet

urlpatterns = [
    path('tests/', TestViewSet.as_view({'get': 'list'})),
    path('tests/<int:test_id>/attend', TestAttendViewSet
         .as_view({'get':'attend'})),
    path('tests/<int:test_id>/attend/question/<int:question_id>', TestAttendViewSet
         .as_view({'post': 'answer_question'})),
    path('tests/<int:test_id>/evaluate', TestAttendViewSet
         .as_view({'get': 'evaluate_test'}))

]
