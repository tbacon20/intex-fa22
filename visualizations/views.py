from django.shortcuts import render

# Create your views here.
def signUpPageView (request) :
    return render(request, 'visualizations/signup.html')