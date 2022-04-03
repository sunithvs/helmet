from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Image(models.Model):
    image_file = models.ImageField(upload_to="pic", )
    processed_image = models.ImageField(upload_to="pic", blank=True, null=True)

    def generate(self, *args, **kwargs):
        # self.processed_image.save(f'{self.transaction_id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


@receiver(post_save, sender=Image)
def create(sender, instance, created, **kwargs):
    if created:
        instance.generate()
