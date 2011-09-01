from django import forms

class DcsForm(forms.Form):
    model = forms.ChoiceField(
        label='Table',
        choices=(
            # ('All', '------'),
            ('Instrument Sensors', (
                ('Ad1Lidsensor', 'AD1 Lid Sensors'),
                ('Ad2Lidsensor', 'AD2 Lid Sensors'),
                ('DbnsIowTemp', 'WP Temperature'),
                ('DbnsRpcGas101', 'Rpc Gas'),
                ('DbnsEnvPth', 'Environment'),)
            ),
            ('HV', (
                ('DbnsAd1Hv', ' AD1 PMT HV', ),
                ('DbnsAd2Hv', 'AD2 PMT HV', ),
                ('DbnsMuonPmtHvVmon', 'Muon PMT HV'),
                ('DbnsRpcHvVmon', 'RPC HV'),)
            ),
            ('Current', (
                ('DbnsAd1HvImon', 'AD1 PMT Current', ),
                ('DbnsAd2HvImon', 'AD2 PMT Current', ),
                ('DbnsMuonPmtHvImon', 'Muon PMT Current'),)
            ),
            ('VME', (
                ('DbnsAd1Vme', 'AD1 VME'),
                ('DbnsAd2Vme', 'AD2 VME'),
                ('DbnsIWVme', 'IWS VME'),
                ('DbnsOWVme', 'OWS VME'),
                ('DbnsRPCVme', 'RPC VME'),)
            ),
        ),
        widget=forms.Select(attrs={'style':'width:98%;'}),
    )
    
    fields = forms.MultipleChoiceField(
        label='Fields', required=True,
        choices=(),
        widget=forms.SelectMultiple(attrs={'size':'20', 'style':'width:98%;'}),
    )
    
    date_from = forms.DateField(
        label='Date From', required=True,
        widget=forms.TextInput(attrs={'size':'11'})
    )
    
    date_to = forms.DateField(
        label='Date To', required=True,
        widget=forms.TextInput(attrs={'size':'11'})
    )
    
    points = forms.IntegerField(
        label='Points', required=False, min_value=1, initial=500,
        widget=forms.TextInput(attrs={'size':'11'})
    )
    
    y_min = forms.FloatField(
        label='y_min', required=False,
        widget=forms.TextInput(attrs={'size':'11'})
    )
    
    y_max = forms.FloatField(
        label='y_max', required=False,
        widget=forms.TextInput(attrs={'size':'11'})
    )
    
    plot_type = forms.ChoiceField(
        label='Type',
        choices=(
            ('scatter', 'Scatter'),
            ('line', 'Line')
        ),
    )
    
    def clean(self):
        '''custom validation'''
        import os
        cleaned_data = self.cleaned_data
        
        # fields = cleaned_data.get('fields')
        if 'fields' in self._errors:
            # skip fields check, (filled by ajax)
            del self._errors['fields']
        if 'fields' not in self.data:
            self._errors['fields'] = ['this field is required']
            
        cleaned_data['fields'] = self.data.getlist('fields')
        # cleaned_data['date_from'] = str(self.cleaned_data.get('date_from'))
        # cleaned_data['date_to'] = str(self.cleaned_data.get('date_to'))
        return cleaned_data
        # return self.data
    