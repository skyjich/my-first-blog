from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    #PostForm 은 form의 이름임.

    class Meta:
        #이 구문은 이 form을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에게 알려주는 구문
        model = Post
        fields = ('title', 'text',)
