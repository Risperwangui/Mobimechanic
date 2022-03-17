from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.http import HttpResponseRedirect


class register(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')