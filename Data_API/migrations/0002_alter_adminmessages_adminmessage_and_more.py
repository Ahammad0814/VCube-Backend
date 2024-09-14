# Generated by Django 5.0.6 on 2024-08-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmessages',
            name='AdminMessage',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='assessmentquestionsdata',
            name='Examples',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='assessmentquestionsdata',
            name='Question',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='assessmentquestionsdata',
            name='Test_Cases',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='batchmessagesdata',
            name='BatchMessage',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='batchtostudentmessagesdata',
            name='BatchMessage',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='coursefeedbackdata',
            name='FeedbackData',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='logindata',
            name='Image',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='placementfeedbackdata',
            name='FeedbackData',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='placementposts',
            name='Description',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='placementposts',
            name='File',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='sendmail',
            name='OTP',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Educational_Info',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Personal_Info',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Placement_Info',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='studentmessagesdata',
            name='StudentMessage',
            field=models.JSONField(default=dict),
        ),
    ]
