from django import forms


from .models import Employee, UserRegistration


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            'brith_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"

        widgets = {
            'brith_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
            'gender': forms.RadioSelect(),
            'email': forms.EmailInput(),
        }

   # Form Level Validation
    def clean(self):
        cleaned_data = super().clean()
        ipassword = cleaned_data.get("password")
        iconfirm_password = cleaned_data.get("confirm_password")

        if ipassword and iconfirm_password:
            if ipassword != iconfirm_password:
                raise forms.ValidationError("Passwords do not match.")  

        iusername = cleaned_data.get("username")
        ipassword = cleaned_data.get("password")

        if ipassword and iusername:
            if ipassword == iusername:
                raise forms.ValidationError("User Name and password should not be same..")

        
        
        
        return cleaned_data
    
