from django import forms


from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            'brith_date': forms.widgets.DateInput(attrs={'type':'date'}),
            'hire_date': forms.widgets.DateInput(attrs={'type':'date'}),
        }