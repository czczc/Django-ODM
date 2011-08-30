from django import forms

class DcsForm(forms.Form):
    model = forms.ChoiceField(
        label='Table',
        choices=(
            ('All', '------'),
            ('Lid Sensors', (
                ('Ad1Lidsensor', 'Ad1Lidsensor'),
                ('Ad2Lidsensor', 'Ad2Lidsensor'),)
            ),
            ('HV', (
                ('DbnsAd1Hv', 'DbnsAd1Hv', ),
                ('DbnsAd2Hv', 'DbnsAd2Hv', ),
                ('DbnsMuonPmtHvVmon', 'DbnsMuonPmtHvVmon'),
                ('DbnsRpcHvVmon', 'DbnsRpcHvVmon'),)
            ),
            ('VME Crate', (
                ('DbnsAd1Vme', 'DbnsAd1Vme'),
                ('DbnsAd2Vme', 'DbnsAd2Vme'),
                ('DbnsIWVme', 'DbnsIWVme'),
                ('DbnsOWVme', 'DbnsOWVme'),
                ('DbnsRPCVme', 'DbnsRPCVme'),)
            ),
            ('Environment & Others', (
                ('DbnsEnvPth', 'DbnsEnvPth'),
                ('DbnsIowTemp', 'DbnsIowTemp'),
                ('DbnsRpcGas101', 'DbnsRpcGas101'),)
            ),
        ),
    )
    
    fields = forms.MultipleChoiceField(
        label='Fields',
        choices=(),
        widget=forms.SelectMultiple(attrs={'size':'20', 'style':'width:95%;'}),
    )
    
    date_from = forms.DateField(
        label='Date From', required=False,
        widget=forms.TextInput(attrs={'size':'12'})
    )
    
    date_to = forms.DateField(
        label='Date To', required=False,
        widget=forms.TextInput(attrs={'size':'12'})
    )
    
    
    def clean(self):
        '''custom validation'''
        import os
        cleaned_data = self.cleaned_data
        
        # fields = cleaned_data.get('fields')
        if 'fields' in self._errors:
            # skip fields check, (filled by ajax)
            del self._errors['fields']
            
        cleaned_data['fields'] = self.data.getlist('fields')
        # cleaned_data['date_from'] = str(self.cleaned_data.get('date_from'))
        # cleaned_data['date_to'] = str(self.cleaned_data.get('date_to'))
        return cleaned_data
        # return self.data
    