
from django.urls import path
from .views import problem_list, submit_solution, top_performer

app_name = 'pythonproblem'

urlpatterns = [
    path('problems/', problem_list, name='problem_list'),
    path('Submit/<int:problem_id>/', submit_solution, name='submit_solution' ),
]




