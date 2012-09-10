from django import forms

class DBIForm(forms.Form):
        
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
            ('RPC', 'RPC'),
        ),
    )
    
    sim = forms.ChoiceField(
        label='Simulation',
        choices=(
            (1, 'Exp'),
            (2, 'MC'),
        ),
    )


class DBIRecordsForm(DBIForm):
    
    table = forms.ChoiceField(
        label='Table',
        choices=(
            ('CableMap', 'CableMap'),
            ('CalibPmtFineGain', 'CalibPmtFineGain'),
            ('CalibPmtTiming', 'CalibPmtTiming'),
            ('EnergyRecon', 'EnergyRecon'),
            ('CalibPmtSpec', 'CalibPmtSpec'),
        ),
    )
    
    task = forms.ChoiceField(
        label='Task',
        choices=(
            (0, 'Task 0'),
            (1, 'Task 1'),
        ),
    )
    
    character = forms.CharField(
        label='Formatting Character', required=True, 
        max_length=1, min_length=1, initial='|',
        widget=forms.TextInput(attrs={'size':'1'})
    )
    
    width = forms.IntegerField(
        label='Width', required=True, 
        max_value=1000, min_value=20, initial=28,
        widget=forms.TextInput(attrs={'size':'3'})
    )


class EnergyReconForm(DBIForm):
            
    task = forms.ChoiceField(
        label='Task',
        choices=(
            (0, 'AdScaled'),
            (1, 'AdSimple'),
        ),
    )
    
    field = forms.ChoiceField(
        label='Value',
        choices=(
            ('peevis', 'PE to Evis'),
        ),
    )

class PMTForm(DBIForm):
    ring = forms.IntegerField(
        label='Ring', required=True, 
        max_value=40, min_value=0, initial=1,
        widget=forms.TextInput(attrs={'size':'2'})
    )
    
    column = forms.IntegerField(
        label='Column', required=True, 
        max_value=40, min_value=0, initial=1,
        widget=forms.TextInput(attrs={'size':'2'})
    )
    
    in_out = forms.ChoiceField(
        label='Inward',
        choices=(
            (1, 'Inward Facing'),
            (0, 'Outward Facing'),
        ),
        widget=forms.Select(attrs={'class':'hidden'})
    )


class ChannelForm(DBIForm):
    board = forms.IntegerField(
        label='Board', required=True, 
        max_value=40, min_value=0, initial=6,
        widget=forms.TextInput(attrs={'size':'2'})
    )
    
    connector = forms.IntegerField(
        label='Connector', required=True, 
        max_value=40, min_value=0, initial=1,
        widget=forms.TextInput(attrs={'size':'2'})
    )
    
class CalibPMTSpecForm(PMTForm):
    field = forms.ChoiceField(
        label='Value',
        choices=(
            ('pmtspehigh', 'High Gain SPE'),
            ('pmtspelow', 'Low Gain SPE'),
            ('pmttoffset', 'Time Offset'),
        ),
    )

class CalibPmtFineGainForm(ChannelForm):
    field = forms.ChoiceField(
        label='Value',
        choices=(
            ('spehigh', 'High Gain SPE'),
            ('sigmaspehigh', 'High Gain SPE Width'),
        ),
    )

class CableMapForm(PMTForm):
    field = forms.ChoiceField(
        label='Value',
        choices=(
            ('board', 'Board'),
            ('connector', 'Connector'),
        ),
    )    

    
    
    
    