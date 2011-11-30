from django import forms

class DBIRecordsForm(forms.Form):
    
    table = forms.ChoiceField(
        label='Table',
        choices=(
            ('CableMap', 'CableMap'),
            ('CalibPmtSpec', 'CalibPmtSpec'),
            ('EnergyRecon', 'EnergyRecon'),
        ),
    )
    
    site = forms.ChoiceField(
        label='Site',
        choices=(
            ('DayaBay', 'Daya Bay'),
            ('LingAo', 'Ling Ao'),
            ('Far', 'Far'),
            ('SAB', 'SAB'),
        ),
    )
        
    detector = forms.ChoiceField(
        label='Detector',
        choices=(
            ('AD1', 'AD1'),
            ('AD2', 'AD2'),
            ('AD3', 'AD3'),
            ('AD4', 'AD4'),
            ('IWS', 'IWS'),
            ('OWS', 'OWS'),
        ),
    )
    
    task = forms.ChoiceField(
        label='Task',
        choices=(
            (0, 'Task 0'),
            (1, 'Task 1'),
        ),
    )
    
    sim = forms.ChoiceField(
        label='Simulation',
        choices=(
            (1, 'Exp'),
            (2, 'MC'),
        ),
    )
    
    character = forms.CharField(
        label='Formatting Character', required=True, 
        max_length=1, min_length=1, initial='|',
        widget=forms.TextInput(attrs={'size':'1'})
    )
    
    width = forms.IntegerField(
        label='Width', required=True, 
        max_value=1000, min_value=20, initial=45,
        widget=forms.TextInput(attrs={'size':'3'})
    )
    
    

