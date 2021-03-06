# Generated by Django 4.0.6 on 2022-07-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditCards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='id',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='history',
            field=models.JSONField(default='{"history": []}', verbose_name='Історія транзакцій'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='CVVCode',
            field=models.IntegerField(verbose_name='Захисний код'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cardAmount',
            field=models.IntegerField(verbose_name='Сума на рахунку'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cardExpirationDate',
            field=models.DateField(verbose_name='Строк придатності'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cardNumber',
            field=models.IntegerField(verbose_name='Номер картки'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cardSeries',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Серія картки'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='issueDate',
            field=models.DateField(verbose_name='Дата видачі'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='status',
            field=models.CharField(choices=[('in', 'Inactivated'), ('ac', 'Activated'), ('ov', 'Overdue')], max_length=2, verbose_name='Статус картки'),
        ),
    ]
