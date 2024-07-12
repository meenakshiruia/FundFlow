from django.contrib import admin
from .models import Lender, Borrower

# Register your models here.

admin.site.register(Lender)
admin.site.register(Borrower)
