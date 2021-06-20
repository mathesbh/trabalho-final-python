# Generated by Django 3.2.4 on 2021-06-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('category_type', models.CharField(choices=[('D', 'Despesa'), ('R', 'Receita')], default='D', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='paybills',
            name='due_day',
        ),
        migrations.RemoveField(
            model_name='paybills',
            name='pay_day',
        ),
        migrations.AddField(
            model_name='paybills',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paybills',
            name='pay_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paybills',
            name='payment',
            field=models.CharField(choices=[('D', 'Dinheiro'), ('CD', 'Débito'), ('CC', 'Crédito'), ('B', 'Boleto')], default='D', max_length=10),
        ),
        migrations.AlterField(
            model_name='paybills',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='paybills',
            name='status',
            field=models.CharField(choices=[('N', 'a Pagar'), ('S', 'Pago')], default='N', max_length=10),
        ),
        migrations.CreateModel(
            name='ReceiveBills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('N', 'a Receber'), ('S', 'Recebido')], default='N', max_length=10)),
                ('receive_date', models.DateField()),
                ('categories', models.ManyToManyField(to='my_app.Category')),
            ],
        ),
        migrations.AddField(
            model_name='paybills',
            name='categories',
            field=models.ManyToManyField(to='my_app.Category'),
        ),
    ]
