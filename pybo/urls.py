from django.urls import path
from . import views
from .views import base_views, question_views, answer_views, comment_views

app_name = 'pybo' #다른 앱과 url 별칭이 중복되지 않도록 namespace 추가

urlpatterns = [
    #base_views.py
    path('', base_views.index, name='index'), #/pybo/는 index라는 별명
    path('<int:question_id>/', base_views.detail, name='detail'), #/pybo/2는 detail이라는 별명
    #question_views.py
    path('question/create/', question_views.question_create, name='question_create'), #누르면 main/pybo/question/create로 이동
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    #answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'), #main/answer/create/[int]로 이동
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    #comment_views.py
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
]
