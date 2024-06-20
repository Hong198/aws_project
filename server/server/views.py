from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("테스트 입니다.")
