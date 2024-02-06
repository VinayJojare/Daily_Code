# Your main project's urls.py
from django.contrib import admin
from django.urls import include, path
from pythonproblem.views import index, subscribe, send_problem, send_email, subscriber_list, submit_solution, top_performer, top_pro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pythonproblem.urls')),
    path('', index, name='index'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send_problem/<str:email>/', send_problem, name='send_problem'),
    path('send_email/', send_email, name='send_email'),
    path('subscriber_list/', subscriber_list, name='subscriber_list'),
    path('topprogrammer/', top_performer, name='top_performer' ),
    path('toppro/', top_pro, name='top_pro' ),
    path('Submit/<int:problem_id>/', submit_solution, name='submit_solution' ),
   
]

