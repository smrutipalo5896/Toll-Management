from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import employdetails
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .forms import UserForm


def index(request):
    empss= employdetails.objects.all()
    context={'empss':empss} 
    return render(request,'emp/index.html',context)
   


def detail(request,employeeId):
    return render(request,'emp/User.html')


class UserFormView(View):
    form_class = UserForm
    template_name='emp/registration.html'
    
    def get(self, request):
        form=self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password =form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('/emp/')
            
        return render(request,self.template_name,{'form':form})
            
            