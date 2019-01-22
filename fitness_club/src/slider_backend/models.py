from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator

def slider_directory_path(instance, filename):

    for char in ((" ", "_"), (".", " ")):
        clean_title = instance.title.replace(*char)

    output_filename = 'slider/'
    output_filename += clean_title
    output_filename += '_' + str(instance.id)
    output_filename += '.' + filename.split(".")[-1]
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
