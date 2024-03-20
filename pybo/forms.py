from django import forms
from pybo.models import Question, Answer, Comment

#이런 형태를 장고 폼이라고 한다.
#forms.Form을 상속받으면 폼, forms.ModelForm을 상속받으면 모델 폼
class QuestionForm(forms.ModelForm): #질문 등록 폼 제작
    #장고 모델 폼은 내부 클래스로 Meta클래스를 반드시 가져야 한다.
    #Meta클래스에는 모델 폼이 사용할 모델과 모델의 필드들을 적어야 한다.
    #QuestionForm클래스는 Question모델과 연결되어 있으며 subject, content를 사용한다고 정의했다.
    class Meta:
        model = Question
        fields = ['subject','content']

        ''' 
        widgets = { 
            'subject' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control','rows':10}),
        } #폼 필드의 위젯을 지정하는 속성, TextInput, Textarea위젯을 사용함
          #부트스트랩의 form-control 클래스를 적용해 필드의 스타일을 조정
        '''

        labels = {
            'subject' : '제목',
            'content' : '내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }