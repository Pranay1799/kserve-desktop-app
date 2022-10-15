from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.http import JsonResponse
from .models import *


# Create your views here.
def home(request):
    return render(request,'login.html')


def submit_sentiment(request):

    try:

        if request.method == "POST":
            sentiment = request.POST.get("sentiment", None)
            employee_id = request.POST.get("emp_id", None)

            print(f"{sentiment=}")
            print(f"{employee_id=}")
            data={'eid':employee_id,'answer':sentiment}

            react=requests.post("http://localhost:8001/api/section/sentiment-analysis/",data)

            if sent:
                return JsonResponse({'status': 200})

        else:
            messages.error(request, "Bad request")
            return redirect("home")

    except Exception as ep:
        messages.error(request, str(ep))
        return redirect("home")


def questions_page(request):

    print(f"{type(request)}")

    return render(request, "question.html")