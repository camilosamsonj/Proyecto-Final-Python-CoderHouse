# Generated by Django 4.2.4 on 2023-09-02 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_tercera_entrega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaAhorro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('monto_objetivo', models.IntegerField()),
                ('fecha_limite', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='itemgasto',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='GastoMensual',
        ),
    ]
