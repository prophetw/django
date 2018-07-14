# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    # context = {'latest_question_list': latest_question_list}
    # return HttpResponse("You're voting on question.")
    return render(request, 'mysite/index.html')