from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
from .forms import DateForm

# Вставь сюда свой токен и URL бота
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

def send_message_to_telegram(message):
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(TELEGRAM_API_URL, data=payload)

def process_date(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            
            # Логика для обработки даты
            result = f'Обработанная дата: {date}'
            
            # Отправка результата в Telegram
            send_message_to_telegram(result)
            
            return HttpResponse('Дата обработана и отправлена в Telegram!')
    else:
        form = DateForm()
    
    return render(request, 'date_form.html', {'form': form})

def home(request):
    return render(request, 'home.html')