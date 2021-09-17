# Generated by Django 3.2.7 on 2021-09-17 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('km_por_galao', models.FloatField()),
                ('cilindros', models.SmallIntegerField()),
                ('cavalo_de_forca', models.SmallIntegerField()),
                ('peso', models.SmallIntegerField()),
                ('aceleracao', models.SmallIntegerField()),
                ('ano', models.DateField()),
                ('origem', models.CharField(max_length=20)),
                ('marca_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marca.marca')),
            ],
            options={
                'db_table': 'carro',
            },
        ),
    ]
