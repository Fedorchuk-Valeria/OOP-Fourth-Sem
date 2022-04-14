from django.contrib import admin
from .models import Bank, Enterprise, Account, Transfer, Installment, Credit


admin.site.register(Bank)
admin.site.register(Enterprise)
admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Installment)
admin.site.register(Credit)