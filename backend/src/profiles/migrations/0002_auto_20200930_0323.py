# Generated by Django 3.1.1 on 2020-09-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='id',
        ),
        migrations.AddField(
            model_name='profiles',
            name='cidade',
            field=models.CharField(default='abcd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='complemento',
            field=models.CharField(default='complemento', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='logradouro',
            field=models.CharField(default='logradouro', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='uf',
            field=models.CharField(default='mg', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profiles',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]