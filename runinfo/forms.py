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
            ('WP' , 'WP' ),
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
            ('WPCalib', 'WPCalib'),
            ('Pedestal', 'Pedestal'),
            ('FEEDiag', 'FEEDiag'),
        ),
    )
    
    run_from = forms.CharField(
        label='Run From', required=False, 
        # min_value=0,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    run_to = forms.CharField(
        label='Run To', required=False, 
        # min_value=0,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    date_from = forms.DateField(
        label='Date From', required=False,
        widget=forms.TextInput(attrs={'size':'12'})
    )
    
    date_to = forms.DateField(
        label='Date To', required=False,
        widget=forms.TextInput(attrs={'size':'12'})
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


class SearchCalibRunListForm(SearchRunListForm):
        
    detector = forms.ChoiceField(
        label='Detector',
        choices=(
            ('All', 'DETECTOR'),
            ('AD1', 'AD1'),
            ('AD2', 'AD2'),
            ('AD3', 'AD3'),
            ('AD4', 'AD4'),
        ),
    )    
    
    runtype = forms.IntegerField(
        label='Run Type', required=False, min_value=0,
        widget=forms.TextInput(attrs={'size':'6'})
    ) # hack, not needed
    