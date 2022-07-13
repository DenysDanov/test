import json
from time import timezone
from django.db import models



class CreditCard(models.Model):
    _statusChoices = (
        ('in', 'Inactivated'),
        ('ac', 'Activated'),
        ('ov', 'Overdue')
    )
    def historyDefault():
        return json.dumps({'history' : []})
    # Model fields
    cardSeries = models.IntegerField('Серія картки')
    cardNumber = models.IntegerField('Номер картки', primary_key=True, unique=True)
    issueDate = models.DateTimeField('Дата видачі', auto_now_add=True)
    cardExpirationDate = models.DateTimeField('Строк придатності')
    CVVCode = models.CharField('Захисний код', max_length=3)
    cardAmount = models.IntegerField('Сума на рахунку', default=0)
    status = models.CharField('Статус картки', max_length=2, choices=_statusChoices)
    history = models.JSONField('Історія транзакцій', default=historyDefault)

    # Model methods
    def addTransaction(self, amount, **kwargs):
        self.cardAmount += amount
        transaction = {
            'amount' : amount,
            'date' : str(timezone.now()),
            'kwargs' : kwargs
        }
        history = json.loads(self.history)
        history['history'].append(transaction)
        self.history = json.dumps(history)
        return None
    