from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile, Problem, Solution
from .forms import SubscriptionForm, SolutionForm
from django.http import Http404
from django.core.management.base import BaseCommand
from django.contrib import messages


def index(request):
    problems = Problem.objects.all()
    return render(request, 'problems/index.html', {'problems': problems})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            user, created = UserProfile.objects.get_or_create(email=email, defaults={'name': name})
            return redirect(top_pro)
    else:
        form = SubscriptionForm()

    return render(request, 'problems/subscribe.html', {'form': form})

def send_problem():
    problem = Problem.objects.order_by('?').first()

    # Check if a problem exists
    if problem:
        subject = f'Daily Coding Problem - {problem.title}'
        message = f"{problem.description}\n\nhttp://127.0.0.1:8000/Submit/{problem.id}/"

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email for user in UserProfile.objects.all()]

        send_mail(subject, message, from_email, recipient_list)




from .problems_data import python_problems 

def problem_list(request):
    allproblems = Problem.objects.all()

    return render(request, 'problems/all_problems.html', {'allproblems':allproblems})


def send_email(request):
    send_problem()
    return redirect('/')



def subscriber_list(request):
    subscribers = UserProfile.objects.all()
    return render(request, 'problems/my_subscriber.html', {'subscribers':subscribers})




def submit_solution(request, problem_id):
    problem = Problem.objects.get(id=problem_id)

    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['user_email']
            code_solution = form.cleaned_data['code']

            # Save the solution to the database
            solution = Solution(user_email=user_email, code=code_solution)
            solution.save()

            # Implement your notification logic here

            # Update the user's solved problems count
            # (Assuming you have a UserProfile model with a solved_problems field)
            user_profile = UserProfile.objects.get(email=user_email)
            user_profile.problems_solved += 1
            user_profile.save()


            return redirect('/toppro/')  

    else:
        form = SolutionForm()

    return render(request, 'problems/submit_solution.html', {'form': form, 'problem': problem})




def top_performer(request):
    top_performers = UserProfile.objects.all().order_by('-problems_solved')

    return render(request, 'problems/topprogrammer.html', {'top_performers': top_performers})


def top_pro(request):
    top_pros = UserProfile.objects.all().order_by('-problems_solved')

    return render(request, 'problems/toppro.html', {'top_pros': top_pros})






