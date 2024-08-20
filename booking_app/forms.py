from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'check_in_date', 'check_out_date', 'hotel', 'room']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        # Perform custom validation: check-out date must be after check-in date
        if check_in_date and check_out_date:
            if check_in_date >= check_out_date:
                raise forms.ValidationError('Check-out date must be after check-in date.')

        return cleaned_data
