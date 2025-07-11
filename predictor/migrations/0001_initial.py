# Generated by Django 5.2.3 on 2025-06-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('SeniorCitizen', models.IntegerField(blank=True, null=True)),
                ('Partner', models.CharField(blank=True, max_length=10, null=True)),
                ('Dependents', models.CharField(blank=True, max_length=10, null=True)),
                ('tenure', models.IntegerField(blank=True, null=True)),
                ('PhoneService', models.CharField(blank=True, max_length=10, null=True)),
                ('MultipleLines', models.CharField(blank=True, max_length=50, null=True)),
                ('InternetService', models.CharField(blank=True, max_length=50, null=True)),
                ('OnlineSecurity', models.CharField(blank=True, max_length=50, null=True)),
                ('OnlineBackup', models.CharField(blank=True, max_length=50, null=True)),
                ('DeviceProtection', models.CharField(blank=True, max_length=50, null=True)),
                ('TechSupport', models.CharField(blank=True, max_length=50, null=True)),
                ('StreamingTV', models.CharField(blank=True, max_length=50, null=True)),
                ('StreamingMovies', models.CharField(blank=True, max_length=50, null=True)),
                ('Contract', models.CharField(blank=True, max_length=50, null=True)),
                ('PaperlessBilling', models.CharField(blank=True, max_length=10, null=True)),
                ('PaymentMethod', models.CharField(blank=True, max_length=50, null=True)),
                ('MonthlyCharges', models.FloatField(blank=True, null=True)),
                ('TotalCharges', models.FloatField(blank=True, null=True)),
                ('prediction', models.CharField(max_length=3)),
                ('probability', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
