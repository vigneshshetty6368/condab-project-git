from django import forms
from .models import con,item, part
from django.forms.widgets import DateInput
from django.contrib.admin.widgets import AdminDateWidget

class Search(forms.Form):
    #con_number = forms.CharField()
    Grid = forms.CharField(required=False)

class importcon(forms.Form):
    #con_number = forms.CharField()
    newcon = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-3 form-control-sm'}))


class createconform(forms.ModelForm):
    class Meta:
        model=con
        #fields='__all__'
        #fields=('Description','Indate','Outdate','Decision',)
        exclude = ['User']
        widgets = {
            'Conc_Number':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Description':forms.Textarea(attrs={'class':'form-control form-control-sm'}),
            'partnumber':forms.Select(attrs={'class':'form-control form-control-sm',}),
            'Drawing_issue':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Quantity':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Indate': forms.DateInput(attrs={'type': 'date','class':'form-control form-control-sm'}),
            'Outdate': DateInput(attrs={'type': 'date', 'class':'form-control form-control-sm'}),
            'Decision':forms.Select(attrs={'class':'form-control form-control-sm',}),
            #'User':forms.Select(attrs={'class':'form-control form-control-sm',}),
        }

class createitemform(forms.ModelForm):
    class Meta:
        model=item
        #fields='__all__'
        #fields=('Description','Indate','Outdate','Decision',)
        exclude = ['User']
        widgets = {
            'Conc_Number':forms.Select(attrs={'class':'form-control form-control-sm',},),
            'Number':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Description':forms.Textarea(attrs={'class':'form-control form-control-sm'}),
            'SNumber':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Feature':forms.Select(attrs={'class':'form-control form-control-sm',}),
            'Requirement':forms.Select(attrs={'class':'form-control form-control-sm',}),
            'Mpos':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Grid':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Nom':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Tol':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Actual':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Nom':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'Unit':forms.Select(attrs={'class':'form-control form-control-sm',}),
            'Rootcause':forms.Select(attrs={'class':'form-control form-control-sm',}),

        }

class createpartform(forms.ModelForm):
    class Meta:
        model=part
        fields='__all__'
        widgets = {
            'Partnumber':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Part'},),
            'Partname':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name'},),
            'Supplier':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Supplier'}),
            'Commodity':forms.Select(attrs={'class':'form-control form-control-sm','placeholder':'Commodity'}),
            'Engine':forms.Select(attrs={'class':'form-control form-control-sm','placeholder':'Engine'}),
        }
