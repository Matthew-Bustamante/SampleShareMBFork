# Generated by Django 5.1.1 on 2024-11-08 23:37

import django.core.validators
import django.db.models.deletion
import website.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatName', models.CharField(max_length=50)),
                ('chatTimeStamp', models.DateTimeField(auto_now_add=True)),
                ('is_group_chat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateField()),
                ('userPhoto', models.ImageField(default='profile_pics/profile_picture_default.jpg', upload_to='profile_pics/')),
                ('bio', models.TextField(max_length=1000)),
                ('numberOfFollowers', models.IntegerField()),
                ('friends', models.ManyToManyField(blank=True, to='website.userprofile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sampleName', models.CharField(max_length=50)),
                ('audioFile', models.FileField(upload_to='samples/', validators=[website.models.validate_length, django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'aac', 'flac', 'm4a'])])),
                ('isPublic', models.BooleanField()),
                ('genres', models.ManyToManyField(blank=True, related_name='samples', to='website.genre')),
                ('userProfiles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postText', models.TextField()),
                ('postTimeStamp', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='User_Posts', to=settings.AUTH_USER_MODEL)),
                ('samples', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.sample')),
                ('userProfiles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to='website.userprofile')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to='website.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentMessage', models.TextField()),
                ('commentTimeStamp', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.post')),
                ('samples', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.sample')),
                ('userProfile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='userProfiles',
            field=models.ManyToManyField(blank=True, to='website.userprofile'),
        ),
    ]
