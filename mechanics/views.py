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

def index(request):
    return render(request,'index.html')

def profile(request, username):
    try:
        user = User.objects.get(pk = username)
        profile = UserProfile.objects.get(user = user)
        works = WorkDone.get_user_works(profile.id)
        works_count = works.count()
    except WorkDone.DoesNotExist:
        works = None

    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user.userprofile.mechanic
            work.save()
            return redirect('/accounts/profile/%d/'%user.id)
    else:
        form = WorkForm()

    return render(request, 'profile.html',{'works': works, 'count': works_count, 'form': form})

def wheelAlign(request):
    try:
        mechanics = Mechanic.objects.all()
    except Mechanic.DoesNotExist:
        mechanics = None
    return render(request, 'wheelAlignment.html',{'mechanics': mechanics})\

def paintJob(request):
    try:
        mechanics = Mechanic.objects.all()
    except Mechanic.DoesNotExist:
        mechanics = None
    return render(request, 'paintJob.html',{'mechanics': mechanics})

def engine(request):
    try:
        mechanics = Mechanic.objects.all()
    except Mechanic.DoesNotExist:
        mechanics = None
    return render(request, 'engine.html',{'mechanics': mechanics})

def tires(request):
    try:
        mechanics = Mechanic.objects.all()
    except Mechanic.DoesNotExist:
        mechanics = None
    return render(request, 'tires.html',{'mechanics': mechanics})

def brake(request):
    try:
        mechanics = Mechanic.objects.all()
    except Mechanic.DoesNotExist:
        mechanics = None
    return render(request, 'brake.html',{'mechanics': mechanics})

def battery(request):
    try:
        mechanics = Mechanic.objects.all()
    except Mechanic.DoesNotExist:
        mechanics = None
    return render(request, 'battery.html',{'mechanics': mechanics})
    
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, request.FILES, instance=request.user)
        profile_form = EditUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        mechanic_form = EditMechanicForm(request.POST, request.FILES, instance=request.user.userprofile.mechanic)

        if user_form.is_valid() or profile_form.is_valid() or mechanic_form.is_valid() :
            user_form.save()
            profile_form.save()
            return redirect('profile', user.id)
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditUserProfileForm(instance=request.user.userprofile)
    context = {
    'user_form': user_form,
    'profile_form': profile_form
    }
    return render(request, 'editprofile.html',context)

def update_mechanic_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, request.FILES, instance=request.user)
        profile_form = EditUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        mechanic_form = EditMechanicForm(request.POST, request.FILES, instance=request.user.userprofile.mechanic)

        if user_form.is_valid() or profile_form.is_valid() or mechanic_form.is_valid() :
            user_form.save()
            profile_form.save()
            mechanic_form.save()
            return redirect('profile', user.id)
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditUserProfileForm(instance=request.user.userprofile)
        mechanic_form = EditMechanicForm(instance=request.user.userprofile.mechanic)
    context = {
    'user_form': user_form,
    'profile_form': profile_form,
    'mechanic_form': mechanic_form
    }
    return render(request, 'editprofile.html',context)

@login_required(login_url='/accounts/login/')
def mechanic_info(request, username):
    try:
        user = Mechanic.objects.get(user=username)
        works = WorkDone.objects.filter(user=user)
    except WorkDone.DoesNotExist:
        works = None

    params = {
        'works': works, 
    }   
    return render(request, 'work.html', params)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def work_delete(request, id, pk):
    user = User.objects.get(id=id)
    card_that_is_ready_to_be_deleted = get_object_or_404(WorkDone, id=pk)
    if request.method == 'POST':
        card_that_is_ready_to_be_deleted.delete()
    return redirect('/accounts/profile/%d/'%user.id)