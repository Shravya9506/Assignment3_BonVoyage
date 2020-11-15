from django.contrib.auth.models import AbstractUser
from django.db import models
from vacations.models import Vacation


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="customer")
    UNMARRIED = 'UM'
    MARRIED = 'MA'
    BLANK = ''
    marital_status_choices = (
        (BLANK,''),
        (UNMARRIED, 'Unmarried'),
        (MARRIED, 'Married'),
    )
    marital_status = models.CharField(max_length=2,
                                      choices=marital_status_choices,
                                      default=BLANK)
    def __str__(self):
        return self.user.username


class CustomerFavoriteVacation(models.Model):
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    vacation = models.ForeignKey(Vacation, on_delete=models.CASCADE, related_name='trip', null=True)

    class Meta:
        unique_together = (('customer', 'vacation'),)

    def __str__(self):
        return self.customer.user.username + " likes " + self.vacation.name


