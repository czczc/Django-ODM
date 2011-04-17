from django import forms

class SearchRunListForm(forms.Form):
    
    site = forms.ChoiceField(
        label='Site',
        choices=(
            ('All', 'SITE'),
            ('EH1', 'EH1'),
            ('EH2', 'EH2'),
            ('EH3', 'EH3'),
            ('SAB', 'SAB'),
        ),
    )
        
    detector = forms.ChoiceField(
        label='Detector',
        choices=(
            ('All', 'DETECTOR'),
            ('AD' , 'AD' ),
            ('AD1', 'AD1'),
            ('AD2', 'AD2'),
            ('AD3', 'AD3'),
            ('AD4', 'AD4'),
            ('WPI', 'WPI'),
            ('WPO', 'WPO'),
            ('RPC', 'RPC'),
        ),
    )

    runtype = forms.ChoiceField(
        label='Run Type',
        choices=(
            ('All', 'RUN TYPE'),
            ('Physics', 'Physics'),
            ('ADCalib', 'ADCalib'),
            ('Pedestal', 'Pedestal'),
            ('FEEDiag', 'FEEDiag'),
        ),
    )
    
    run_from = forms.IntegerField(
        label='Run From', required=False, min_value=0,
        widget=forms.TextInput(attrs={'size':'5'})
    )
    
    run_to = forms.IntegerField(
        label='Run To', required=False, min_value=0,
        widget=forms.TextInput(attrs={'size':'5'})
    )
    
    date_from = forms.DateField(
        label='Date From', required=False,
        widget=forms.TextInput(attrs={'size':'10'})
    )
    
    date_to = forms.DateField(
        label='Date To', required=False,
        widget=forms.TextInput(attrs={'size':'10'})
    )
    
    records = forms.IntegerField(
        label='Records per Page', required=False, min_value=1,
        widget=forms.TextInput(attrs={'size':'4'})
    )
    
    sort_run = forms.ChoiceField(
        label='Sort Run',
        choices=(
            ('DESC', 'DESC'),
            ('ASC', 'ASC'),
        ),
    )
    