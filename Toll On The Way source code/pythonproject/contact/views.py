from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactforms
from django.forms.forms import Form


def contact(request):
    title = 'Contact'
    form = contactforms(request.POST or None)
    context = {'title': title,'form':form, }
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from TOLLonMYway.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
        title="thanks!"
        confirm_message="we will get back to u"
        
        context={'title':title,'confirm_message':confirm_message,}
    template = 'contact.html'
    return render(request, template, context)
    


