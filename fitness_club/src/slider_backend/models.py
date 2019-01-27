from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator

def slider_directory_path(instance, filename):
    output_filename = 'slider/'
    output_filename += filename
    return output_filename

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('Position 0 is not allowed')
        )

class SliderPicture(models.Model):
    image = models.ImageField(upload_to=slider_directory_path,
                              blank=False)
    order = models.PositiveIntegerField(default=1,
                                        validators=[MaxValueValidator(10), validate_nonzero])

    class Meta:
        ordering = ('order',)                
