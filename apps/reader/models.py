from datetime import timedelta
from django.db import models
from django.contrib.auth.models import  AbstractUser, User

# Create your models here.
# Reader -> AbstractUser -> AbstractBaseUser -> models.Model

class NIC(models.Model):

    nic_number = models.CharField(max_length=10, primary_key=True)
    delivery_date = models.DateField()
    # auto-calculated field from other fields

    expiration_date = models.GeneratedField(
        expression = models.F('delivery_date') + timedelta(days=1827), 
        output_field = models.DateField(),
        db_persist = True #save into database
    )

    def __str__(self) -> str:
        return f'{self.nic_number}(del: {self.delivery_date}, exp: {self.expiration_date})'
    
    class Meta:
        db_table_comment = 'National Identity Card'
        verbose_name_plural = 'NIC'


class Reader(AbstractUser):
    
    READER_TITLE = {
        "Mr":"Mr",
        "Mrs":"Mrs",
        "Ms":"Ms",
        "Dr":"Dr"
    }
    # if no explicit primary key is defined, django will generate an id for us.
    # Class attribute will represent fields in our table
    # By default django fields are not null

    username = models.CharField(max_length=50, primary_key=True)
    # null = True set the null field when used on the terminal
    # blank= True set the null field when used on the dashboard
    title = models.CharField(max_length=5, null=True, blank=True, choices=READER_TITLE)
    # if you want to remove te default, just set it to None
    # email = None

    nic = models.OneToOneField('reader.NIC', related_name='reader', on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        db_table = 'reader'
        # Define some meta data, including constraints
        constraints = [
            models.CheckConstraint(
                # reader_Reader_title_check
                name='%(app_label)s_%(class)s_title_check',
                check=models.Q(title__in=['Mr','Mrs','Ms','Dr'])
            )
        ]

