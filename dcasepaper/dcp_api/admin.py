from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PatientProfile),
admin.site.register(DoctorProfile),
admin.site.register(DoctorClinic),
admin.site.register(PatientMedicalProfile),
admin.site.register(Complaints),
admin.site.register(DoctorSpecialization),
admin.site.register(WorkDoneLog),
admin.site.register(Visits),
admin.site.register(Prescription)