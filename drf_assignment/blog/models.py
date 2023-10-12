from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Post(models.Model):
    # Your model fields
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Replace 'created_at' with your actual timestamp field

@receiver(post_save, sender=Post)
def send_post_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'Your post "{instance.title}" has been created.'
        from_email = 'mitali@gmail.com'  # Set your email here
        recipient_list = [instance.author.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)