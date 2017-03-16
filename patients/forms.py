from prescriptions.models import Prescription, Diagnoses
from patients.models import Notes

from django import forms

class DiagForm(forms.ModelForm):

    class Meta:
        model = Diagnoses
        fields = ['diagnosesName', 'diagnosesDateBegin', 'diagnosesSeverity']

class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = ['prescriptionTxt', 'printTime']

class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ['noteID', 'patientID', 'noteText']







