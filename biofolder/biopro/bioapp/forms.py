from django import forms

class bioform(forms.Form):

    FirstName=forms.CharField(
        label='Enter Your FirstName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your FirstName'
            }
        )
    )
    LastName = forms.CharField(
        label='Enter Your LastName',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your LastName'
            }
        )
    )
    CollegeName = forms.CharField(
        label='Enter Your CollegeName',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your CollegeName'
            }
        )
    )
    Qualification = forms.CharField(
        label='Enter Your Qualification',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Qualification'
            }
        )
    )
    Percentage = forms.IntegerField(
        label='Enter Your Percentage',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Percentage'
            }
        )
    )

    Gender=forms.CharField(
        label='Enter Your Gender',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Gender'
            }
        )
    )
    Dateofbirth = forms.IntegerField(
        label='Enter Your Dateofbirth',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Dateofbirth'
            }
        )
    )
    Age = forms.IntegerField(
        label='Enter Your Age',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Age'
            }
        )
    )

    Address = forms.CharField(
        label='Enter your Address',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your Address'
            }
        )
    )

#class contactform(forms.Form):
   # name=forms.CharField(max_length=20)
   # salary=forms.IntegerField()
   # location=forms.CharField(max_length=20)
    #email=forms.EmailField(max_length=50)
   # username=forms.CharField(max_length=20)
  #  password=forms.CharField(max_length=20
#