from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators  import login_required
import stripe

stripe.api_key=settings.STRIPE_SECRET_KEY

@login_required
def pay(request):
    publishKey=settings.STRIPE_PUBLISHABLE_KEY
    token = request.form['stripeToken']
    try:
     charge = stripe.Charge.create(
      amount=999,
      currency="usd",
      description="Example charge",
      source=token,
    )
    except stripe.error.CardError as e:
        #card has been declined
     pass   
    context={'publishKey': publishKey}
    template='payment.html'
    return render(request,template,context)
# Create your views here.
