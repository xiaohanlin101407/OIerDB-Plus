from django.shortcuts import HttpResponse, render
from typing import Callable
from piggySQL.models import Oier
from .QuickDjango import QJR


def loadtemplate(__path) -> Callable:
    def wrapper(request):
        return render(request, __path)
    return wrapper

