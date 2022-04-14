from django.contrib import admin
from .models import EnterpriseSpecialist, Manager, Operator

admin.site.register(EnterpriseSpecialist)
admin.site.register(Manager)
admin.site.register(Operator)