from django.db import models
import random
import string

# Utility function to generate unique IDs
def generate_unique_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Participant model
class Participant(models.Model):
    event_choices = [
        ('CyberShow', 'CyberShow'),
        ('CodeGolf', 'CodeGolf'),
        ('PromptMatrix', 'PromptMatrix'),
        ('FragFest', 'FragFest'),
        ('ExpoRenaissance', 'ExpoRenaissance'),
        ('ArtBurst', 'ArtBurst'),
        ('MemeIfy', 'MemeIfy'),
    ]

    id = models.CharField(
        max_length=8,
        default=generate_unique_id,
        unique=True,
        editable=False,
        primary_key=True
    )
    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=155)
    college_name = models.CharField(max_length=255)
    college_id = models.CharField(max_length=25)
    course = models.CharField(max_length=155, blank=True, null=True)
    event = models.CharField(max_length=50, choices=event_choices)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.id}) - {self.event}"

# CyberShow details model
class CyberShowDetail(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=155)
    number_of_members = models.IntegerField()
    skit_detail_file = models.FileField(upload_to='uploads/cybershow_skits/')
    participant_names = models.JSONField()  # Stores participant names as a JSON list

    def __str__(self):
        return f"CyberShow - {self.team_name}"

# FragFest details model
class FragFestDetail(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    team_member_details = models.JSONField()  # Stores names and usernames as a JSON list

    def __str__(self):
        return f"FragFest - {self.participant.name}"

# Expo Renaissance details model
class ExpoDetail(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=155)
    number_of_members = models.IntegerField()
    project_detail = models.TextField()
    project_detail_file = models.FileField(upload_to='uploads/expo_projects/')

    def __str__(self):
        return f"ExpoRenaissance - {self.team_name}"

# General event-specific details can be extended similarly
class Bill(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255)