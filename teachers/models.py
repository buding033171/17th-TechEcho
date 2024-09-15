from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import IntegrityError, models
from taggit.managers import TaggableManager

from chat.models import ChatGroup


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    labels = TaggableManager()
    introduce = models.TextField(
        validators=[MinLengthValidator(50), MaxLengthValidator(500)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    chat_group = models.OneToOneField(
        "chat.ChatGroup",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_teacher",
    )

    class Meta:
        ordering = ["-updated_at"]

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.user.is_teacher = True
            self.user.save()

        if self.user.is_teacher and not self.chat_group:
            group_name = f"{self.user.username}_group_{self.id or ''}"
            try:
                self.chat_group = ChatGroup.objects.create(group_name=group_name)
            except IntegrityError:
                self.chat_group = ChatGroup.objects.get(group_name=group_name)

        super().save(*args, **kwargs)

        if self.chat_group and not self.chat_group_id:
            self.chat_group_id = self.chat_group.id
            super().save(update_fields=["chat_group_id"])

    def __str__(self):
        return f"{self.user.username}"
