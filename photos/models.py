from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse


def validate_name_length(value):
    if len(value) < 4:
        raise ValidationError('A kép neve legalább 4 karakter hosszú kell legyen.')


class Photo(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name_length],
                            verbose_name='Kép neve')
    image = models.ImageField(upload_to='photos/', verbose_name='Kép')
    upload_date = models.DateTimeField(default=timezone.now, verbose_name='Feltöltés dátuma')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Feltöltő')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-upload_date']
        verbose_name = 'Fénykép'
        verbose_name_plural = 'Fényképek'
