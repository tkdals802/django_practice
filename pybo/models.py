from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200) #CharField는 글자수를 제한하고 싶을 때
    content = models.TextField() #글자수 제한 x
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키, Question가 삭제되면 연쇄 삭제
    content = models.TextField() 
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

#sqlite에는 pybo_question, pybo_answer 이런 식으로 테이블이 생기지만, Question, Answer을 이름으로 사용할거임

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,null=True,blank=True,on_delete=models.CASCADE)
