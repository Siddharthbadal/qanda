from django import forms 
from django.contrib.auth import get_user_model
from django.forms import fields
from .models import Comment, Question, Answer


User = get_user_model()

class UserRegistraionForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if len(cd['password']) < 7:
            raise forms.ValidationError('Password should be of minimum 8 characters')
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError("Email already exist!")


class QuestionRegistrationForm(forms.ModelForm):

    class  Meta:
        model = Question
        fields = ('title', 'body')


class AnswerForm(forms.ModelForm):    
    class Meta:
        model = Answer
        fields = ('description',)

class CommentForm(forms.ModelForm):    
    class Meta:
        model = Comment
        fields = ('description',)

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')



class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)




class ProfileForm(forms.ModelForm):
    class Meta:
        model = User    
        fields = ('first_name', 'last_name', 'username','email')