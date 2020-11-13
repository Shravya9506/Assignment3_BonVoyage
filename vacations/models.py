from django.db import models, IntegrityError
from django.urls import reverse
from django.template.defaultfilters import slugify


class AutoSlugifyOnSaveModel(models.Model):
    """
    Models that inherit from this class get an auto filled slug property based on the models name property.
    Correctly handles duplicate values (slugs are unique), and truncates slug if value too long.
    The following attributes can be overridden on a per model basis:
    * value_field_name - the value to slugify, default 'name'
    * slug_field_name - the field to store the slugified value in, default 'slug'
    * max_interations - how many iterations to search for an open slug before raising IntegrityError, default 1000
    * slug_separator - the character to put in place of spaces and other non url friendly characters, default '-'
    """

    def save(self, *args, **kwargs):

        pk_field_name = self._meta.pk.name
        value_field_name = getattr(self, 'value_field_name', 'name')
        slug_field_name = getattr(self, 'slug_field_name', 'slug')
        max_interations = getattr(self, 'slug_max_iterations', 1000)
        slug_separator = getattr(self, 'slug_separator', '-')

        # fields, query set, other setup variables
        slug_field = self._meta.get_field(slug_field_name)
        slug_len = slug_field.max_length
        queryset = self.__class__.objects.all()
        # if the pk of the record is set, exclude it from the slug search
        current_pk = getattr(self, pk_field_name)
        if current_pk:
            queryset = queryset.exclude(**{pk_field_name: current_pk})

        # setup the original slug, and make sure it is within the allowed length
        slug = slugify(getattr(self, value_field_name))
        if slug_len:
            slug = slug[:slug_len]
        original_slug = slug

        # iterate until a unique slug is found, or max_iterations
        counter = 2
        while queryset.filter(**{slug_field_name: slug}).count() > 0 and counter < max_interations:
            slug = original_slug
            suffix = '%s%s' % (slug_separator, counter)
            if slug_len and len(slug) + len(suffix) > slug_len:
                slug = slug[:slug_len - len(suffix)]
            slug = '%s%s' % (slug, suffix)
            counter += 1

        if counter == max_interations:
            raise IntegrityError('Unable to locate unique slug')

        setattr(self, slug_field.attname, slug)

        super(AutoSlugifyOnSaveModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Vacation(AutoSlugifyOnSaveModel):
    name = models.CharField(max_length=60, verbose_name='Vacation name')
    destination = models.CharField(max_length=60)
    description = models.TextField()
    destination_image = models.ImageField(upload_to='photos')
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.destination

class Trip(AutoSlugifyOnSaveModel):
    vacation = models.ForeignKey(
        Vacation,
        on_delete=models.CASCADE,
        related_name='trips'
    )
    name = models.CharField(max_length=60, verbose_name='Trip name')
    source = models.CharField(max_length=60, verbose_name='Starting point')
    transportation_choices = (
        ('FL','Flight'),
        ('TR','Train'),
        ('CR','Cruise'),
        ('BU','Bus')
    )
    slug = models.SlugField(max_length=200,
                            unique=True)
    mode_of_transport = models.CharField(max_length=2, choices=transportation_choices)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price ($)')
    additional_benefits = models.TextField()
    trip_description = models.TextField()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name