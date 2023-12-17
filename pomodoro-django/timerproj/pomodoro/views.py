from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Pattern

# Create your views here.
def index(request):
    schedule = Pattern.objects.filter(id=1).values().last()
    context = {
            "sched": schedule,
        }
    return render(request, "pomodoro/index.html", context)
