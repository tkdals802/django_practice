from django.urls import path
from . import views

app_name = 'pybo' #다른 앱과 url 별칭이 중복되지 않도록 namespace 추가

urlpatterns = [
    path('', views.index, name='index'), #/pybo/는 index라는 별명
    path('<int:question_id>/', views.detail, name='detail'), #/pybo/2는 detail이라는 별명
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), #main/answer/create/[int]로 이동
    path('question/create/', views.question_create, name='question_create'), #누르면 main/pybo/question/create로 이동
]
