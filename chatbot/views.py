from django.shortcuts import render, redirect
from django.http import JsonResponse
import google.generativeai as genai
from dotenv import load_dotenv
import os

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(message):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(message)
    return response.text

# Create your views here.
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)
    response_text = ""
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            response_text = ask_gemini(message)
            return JsonResponse({'response': response_text})
    return render(request, 'chatbot.html', {'chats': chats})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')