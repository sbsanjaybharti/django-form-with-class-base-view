from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Career(models.Model):

    MONTH_CHOICES = (
        ('January', 'January'),
        ('Ferbruary', 'Ferbruary'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    user = models.ForeignKey(User, related_name='career_user', null=True, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, null=True, blank=True)
    responsibility = models.CharField(max_length=100, null=True, blank=True)
    current_working = models.BooleanField(default=True , blank=True)
    start_month = models.CharField(max_length=15, choices=MONTH_CHOICES, default='January')
    start_year = models.CharField(max_length=4, null=True, blank=True)
    end_month = models.CharField(max_length=20, choices=MONTH_CHOICES, null=True, blank=True)
    end_year = models.CharField(max_length=20, null=True, blank=True)
    company_type = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='career_created_by', null=True, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='career_updated_by', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "account_career"