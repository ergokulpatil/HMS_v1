from django.db import models


class PatientProfile(models.Model):
    P_Name = models.CharField(max_length=64)
    P_DOB = models.DateField()
    P_Address = models.CharField(max_length=128)
    P_Email = models.EmailField()
    P_Mobile = models.CharField(max_length=10)
    P_Religion = models.CharField(max_length=100)
    P_Gender = models.CharField(max_length=64)
    P_Family = models.CharField(max_length=200)
    P_MaritalStatus = models.CharField(max_length=200)
    P_Anniversary = models.DateField()

    # Medical Information
    @property
    def MedicalProfile(self):
        return self.patientmedicalprofile_set.all()

    # Visit Information
    @property
    def Appointment(self):
        return self.visits_set.all()


class DoctorProfile(models.Model):
    D_name = models.CharField(max_length=64)
    D_dob = models.DateField()
    D_address = models.CharField(max_length=128)
    D_email = models.EmailField()
    D_mobile = models.CharField(max_length=10)
    D_anniversary = models.DateField()


class DoctorClinic(models.Model):
    Doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    C_Name = models.CharField(max_length=64)
    C_Address = models.CharField(max_length=128)
    C_PhoneNumber = models.CharField(max_length=10)
    C_Google_url = models.CharField(max_length=64)
    C_OpenTime = models.DateField()
    C_Closing = models.DateField()


class PatientMedicalProfile(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    P_habbit = models.CharField(max_length=128)
    P_level_of_higgins = models.CharField(max_length=64)
    P_cosmetic_concern = models.CharField(max_length=128)
    P_medical_history = models.CharField(max_length=1024)


class Complaints(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    C_TimeStamp = models.DateTimeField()
    CompaintDetail = models.CharField(max_length=1024)


class DoctorSpecialization(models.Model):
    Doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    Treatment_Name = models.CharField(max_length=128)
    Treatment_Amount = models.IntegerField()


class Visits(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    Complaint = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    Treatment = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)
    Visit_Time_Stamp = models.DateField()
    Details = models.CharField(max_length=1024)
    Advice = models.CharField(max_length=1024)
    Is_Visited = models.BooleanField(default=False)
    Visit_Type = models.CharField(max_length=64)


class WorkDoneLog(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    Complaint = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    Visits = models.ForeignKey(Visits, on_delete=models.CASCADE)
    Treatment = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)
    WorkDone_Time_Stamp = models.DateField()


class Prescription(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    Visit = models.ForeignKey(Visits, on_delete=models.CASCADE)
    DrugName = models.CharField(max_length=64)
    Duration = models.CharField(max_length=64)
    Dose = models.CharField(max_length=64)