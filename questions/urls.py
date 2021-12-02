from django.urls import path
from .views import question_list, question_details, register, create_question, update_question, delete_question, update_answer, delete_answer, changeProfile, profileInfo


urlpatterns = [
    path("", question_list, name='questions_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path("register/", register, name='register'),
    path("questions/create/", create_question, name='create_question'),
    path("updateQuestion/<slug:slug>/", update_question, name="update_question"),
    path("deleteQuestion/<slug:slug>/", delete_question, name="delete_question"),
    path("answer/update/<int:id>/", update_answer, name="update_answer"),
    path("answer/delete/<int:id>/", delete_answer, name="delete_answer"),
    path("profileUpdate/", changeProfile, name="changeProfile"),
    path("profiledetails/", profileInfo, name="profileInfo"),
  
]
