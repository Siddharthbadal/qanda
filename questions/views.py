from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, redirect
from django.contrib import messages
from .models import Question, Answer, Comment
from .forms import CommentForm, User, UserRegistraionForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm, ProfileForm
from django.contrib.auth.decorators import login_required


def question_list(request):
    user = User.objects.filter(username=request.user)
    if 'searchquery' in request.GET:
        searchquery = request.GET['searchquery']
        questions_list = Question.objects.filter(title__icontains=searchquery)
    else:
        questions_list  = Question.objects.all().order_by('-created_at')

    return render(request, 'questions/questionsList.html', {'questions_list': questions_list,'user':user})


@login_required
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    
    answer_list = Answer.objects.filter(question=question)
    user = User.objects.filter(username=request.user)
    
    
    if request.method == 'POST':
        answerform = AnswerForm(request.POST)
        if answerform.is_valid():
            answer = answerform.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = answerform.save()

            return redirect('question_details', slug=question.slug)
    else:
        answerform = AnswerForm()


    

    return render(request, 'questions/qdetails.html', {'question': question,'answer_list':answer_list, 'answerform':answerform, 'user':user,})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistraionForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return render(request, 'questions/register_done.html', {'user_form': user_form})

    else:
        user_form = UserRegistraionForm()

    return render(request, 'questions/register.html', {'user_form':user_form})


@login_required
def create_question(request):

    if request.method == 'POST':
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()

            return redirect('questions_list')

    else:
        question_form = QuestionRegistrationForm()

    return render(request, 'questions/add_question.html',{'question_form':question_form})

@login_required
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)

    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('questions_list')
    
    return render(request, 'questions/updateQuestion.html', {'form':form})



@login_required
def delete_question(question, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect("questions_list")


@login_required
def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)

    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)

    return render(request, 'questions/updateAnswer.html',{'form':form})

@login_required
def delete_answer(answer, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect("question_details",slug=answer.question.slug)

@login_required
def changeProfile(request):
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, instance=request.user)

        if profileForm.is_valid():
            profileForm.save()
            messages.success(request, 'Profile has been Updated')
    profileForm = ProfileForm(instance=request.user)

    return render(request, 'registration/profile.html',{'profileForm':profileForm})



@login_required
def profileInfo(request):
    questions=Question.objects.filter(author=request.user).order_by('-created_at')
    answers = Answer.objects.filter(author=request.user).order_by('-created_at')
    user = User.objects.filter(username=request.user)

    return render(request, 'questions/profileInfo.html',{'questions':questions,'answers':answers, 'user':user})

