from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # -----------Patient Profile Model-------------
    path('patient-profile-list/', PatientProfileListView.as_view(), name='patient-profile-list'),
    path('patient-profile/<int:pk>/', RUD_PatientProfile.as_view(), name='patient-profile'),
    # -----------Patient Profile Model-------------


    #-----------Patient Medical Profile Model(Single Object)-------------
    path('patient-medical/',PatientMedicalProfileListView.as_view(), name='patient-medical-post'),
    path('patient-medical-profile/<int:p_id>/',RUD_PatientMedicalProfile.as_view(), name ='patient-medical-profile' ),
    #-----------End Patient Medical Profile Model-------------

    #-----------Patient with Nested Medical Profile(Single Object But Nested With Profile)-------------
    path('patient-with-medical-profile/',PatientAndMedicalProfileListView.as_view(), name='patient-with-medical-profile-list'),
    path('patient-with-medical-profile/<int:pk>',RUD_PatientAndMedicalProfile.as_view(), name='patient-with-medical-profile'),
    #-----------Patient with Nested Medical Profile-------------

    # -----------Work Done Logs-------------
    # ---------Bulk Post
    path('Work-Done-Log/', WorkDoneLogListView.as_view(), name='work-done-log-list'),
    path('Work-Done-Log/<int:pk>', RUD_WorkDoneLog.as_view(), name='work-done-log'),
    # -----------End Work Done Logs-------------

    # -----------Complaint Model-------------
    path('Complaints-List/', ComplaintsListView.as_view(), name='Complaints-list'),
    path('Complaint/<int:pk>', RUD_Complaints.as_view(), name='Complaint'),
    # -----------End Complaint Model-------------

    # -----------Visit Model-------------
    path('Visit-List/', VisitsListView.as_view(), name='Visit-list'),
    path('Visit/<int:pk>', RUD_Visits.as_view(), name='Visit'),
    # -----------End Visit Model-------------

    # -----------Prescription Model-------------
    # ---------Bulk Post
    path('Prescription-List/', PrescriptionListView.as_view(), name='Prescription -list'),
    path('Prescription/<int:pk>', RUD_Prescription.as_view(), name='Prescription'),
    # -----------End Visit Model-------------

    # path('patient-profile-list/',Post_Patients.as_view(), name='patient-profile-list'),
    # path('patient-profile/<int:pk>/',RUD_Patient.as_view(), name ='patient-profile' ),

    # path('doctor-profile-list/',Post_Doctors.as_view(), name='doctor-profile-list'),
    # path('doctor-profile/<int:pk>/',RUD_Doctors.as_view(), name ='doctor-profile'),

    # path('treatment-new/',Post_Treatment.as_view(), name='treatment-new'),
    # path('treatment',RUD_Treatment.as_view(), name ='treatment'),

    # In_Process

    # path('patient-treatment-history/',Post_Patient_Treatment_History.as_view(), name='patient-treatment-history'),
    # path('patient-treatment-history/<int:pk>/<int:p_id>',RUD_Patient_Treatment_History.as_view(), name ='patient-treatment-history'),

    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:emonth>/<slug:slug>/', views.article_detail),

]
