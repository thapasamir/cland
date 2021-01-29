from django.forms import EmailField
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models  import Comment,cateogies,Content
import django_filters
from django_filters import CharFilter

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body','content')
        labels = {
            "body": "Add comment"
        }

class UserRegisterForm(UserCreationForm):
  email = EmailField()

  class Meta:
      model = User
      fields = ['username', 'email', 'first_name']

#search or Filters

class ContentSearch(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains',label=" ")
    class Meta:
        model = Content
        fields = '__all__'
        exclude =['link','acess']


class CateogrySearch(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains',label=" ")
    class Meta:
        model = cateogies
        fields = ['name']
