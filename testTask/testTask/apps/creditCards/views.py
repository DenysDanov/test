from datetime import date,datetime
from dateutil.relativedelta import relativedelta

import json
from random import choice
from string import digits

from django.shortcuts import redirect, render
from django.db.models import Q

from .models import CreditCard
from .service import setInterval


t = None

def changeCardStatus(cardNumber,status, card=None):
    if not card:
        card = CreditCard.objects.get(cardNumber=cardNumber)
    card.status = status
    card.save()

#checking card`s expiration
def checkDate():
    _cards = CreditCard.objects.all().filter(
        cardExpirationDate__lte=datetime.now()
        )
    for card in _cards:
        changeCardStatus(None,'ov',card)
    

def index(request):
    global t
    if not t:
        t = setInterval(10,checkDate)

    searchQuery : str = request.GET.get('q')
    cards = CreditCard.objects.all()

    if searchQuery:
        if searchQuery.isdecimal():
            cards = CreditCard.objects.all().filter(
                Q(cardSeries__contains=searchQuery) | 
                Q(cardNumber__contains=searchQuery))
        elif searchQuery.isascii():
            cards = CreditCard.objects.all().filter(
                Q(status__contains=searchQuery[:2]))
       
    return render(request, 'index.html', {
        'cards': cards
    })

def deactivate(request):
    changeCardStatus(request.GET.get('cardNumber'),'in')
    return redirect('/')

def activate(request):
    changeCardStatus(request.GET.get('cardNumber'),'ac')
    return redirect('/')

def delete(request):
    CreditCard.objects.get(cardNumber=request.GET.get('cardNumber')).delete()
    return redirect('/')

def history(request):
    card = CreditCard.objects.get(cardNumber=request.GET.get('cardNumber'))
    history = json.loads(card.history)
    print(history)
    return render(request,'history.html',{
        'card': card,
        'history' : history['history']
    })

def addTransaction(request):
    amount : str = request.POST.get('amount')
    if not amount.isdecimal(): return redirect('../')
    card = CreditCard.objects.get(cardNumber=request.POST.get('cardNumber'))
    card.addTransaction(
        amount = amount
    )
    card.save()
    return redirect(f'../?cardNumber={card.cardNumber}')

def __generate(series, expTime):
    cardNumber_gen = lambda: int('4' + ''.join([choice(digits) for i in range(15)]))
    cardExpirationDate = date.today() + relativedelta(days=int(expTime))
    CVVCode = ''.join([choice(digits) for i in range(3)])
    cardNumber = None
    while True:
        cardNumber = cardNumber_gen()
        try:
            CreditCard.objects.get(cardNumber=cardNumber)
        except BaseException:
            break

    CreditCard.objects.get_or_create(
        cardSeries = int(series),
        cardNumber = cardNumber,
        cardExpirationDate = cardExpirationDate,
        CVVCode = CVVCode,
        status='ac'
        )




def generateCards(request):
    amount : str = request.POST.get('amount')
    series : str = request.POST.get('series')
    expTime : str = request.POST.get('expTime')
    [__generate(series,expTime) for i in range(int(amount))]
    return redirect('../')

