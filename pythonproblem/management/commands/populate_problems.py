# your_app/management/commands/populate_problems.py

from django.core.management.base import BaseCommand
from pythonproblem.models import Problem
from pythonproblem.problems_data import python_problems

class Command(BaseCommand):
    help = 'Populate problems data in the database'

    def handle(self, *args, **options):
        for problem_data in python_problems:
            title = problem_data['title']
            description = problem_data['description']

            
            if not Problem.objects.filter(title=title).exists():
                Problem.objects.create(title=title, description=description)

        self.stdout.write(self.style.SUCCESS('Problems data successfully populated'))
