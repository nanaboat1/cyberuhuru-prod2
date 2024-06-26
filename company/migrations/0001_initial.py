# Generated by Django 4.2.5 on 2023-09-21 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stats', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=25, null=True)),
                ('establish_at', models.DateField(blank=True, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_address', to='users.address')),
                ('industry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_type', to='stats.industry')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_user', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='HireStatus',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('status_order', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('IND', 'IND'), ('UAE', 'UAE')], max_length=255, null=True)),
                ('min_range', models.PositiveIntegerField(blank=True, null=True)),
                ('max_range', models.PositiveIntegerField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecommendationCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=255)),
                ('candidate_skill', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('YEARLY', 'YEARLY'), ('MONTHLY', 'MONTHLY')], max_length=255, null=True)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('is_paid', models.BooleanField(default=0)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('resumes_limit', models.PositiveIntegerField(blank=True, null=True)),
                ('resumes_count', models.PositiveIntegerField(default=0)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscriptions', to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TechnolgyStack',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('no_of_candidate', models.PositiveIntegerField(default=0)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('skills_set', models.CharField(blank=True, max_length=255, null=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.skills')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReplacementRequests',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacement_request', to='users.user')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_replacement', to='company.company')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.hirestatus')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HireCandidate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hired_candidate', to='users.user')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_hire', to='company.company')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.hirestatus')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_title', models.CharField(blank=True, max_length=255, null=True)),
                ('workplace_title', models.CharField(blank=True, max_length=100, null=True)),
                ('job_location', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=255)),
                ('description_of_job', models.TextField(blank=True, null=True)),
                ('filter', models.CharField(blank=True, max_length=150, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
            ],
            options={
                'verbose_name': 'Company User',
                'verbose_name_plural': 'Company User',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('company.company',),
        ),
    ]
