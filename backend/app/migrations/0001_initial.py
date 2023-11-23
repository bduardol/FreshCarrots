# Generated by Django 4.2.7 on 2023-11-23 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=50)),
                ('edition', models.IntegerField()),
                ('year', models.DateField()),
                ('category', models.CharField(max_length=100)),
                ('thumbnail', models.BinaryField(null=True)),
                ('grade', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(default=None, max_length=30, unique=True)),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=255)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('phoneNumber', models.CharField(default=None, max_length=20)),
                ('password', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('isbn', models.BigIntegerField()),
                ('cpf', models.BigIntegerField()),
                ('availability', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('idReview', models.IntegerField(primary_key=True, serialize=False)),
                ('grade', models.IntegerField()),
                ('comment', models.TextField()),
                ('bookIsbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('userCpf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('idLoan', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.IntegerField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('bookIsbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_as_borrower', to='app.user')),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_as_lender', to='app.user')),
            ],
        ),
    ]
