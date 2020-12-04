# Generated by Django 2.2 on 2020-12-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions withoutexplicitly assigning them.', verbose_name='superuser status')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('profile_picture', models.ImageField(upload_to='users/profile/')),
                ('username', models.CharField(max_length=60, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobile', models.BigIntegerField(verbose_name='Navy Mobile')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Super_admin'), (3, 'staff'), (4, 'common_user')], default=4)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_groups_set', related_query_name='resonance_user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_permissions_set', related_query_name='resonance_user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]