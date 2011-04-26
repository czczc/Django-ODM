from django import forms
from odm.production.diagnostics import Diagnostics
from odm.production.pqm import Pqm

class SearchPlotsForm(forms.Form):
    
    site = forms.ChoiceField(
        label='Site',
        choices=(
            ('DayaBay', 'DayaBay'),
            ('LingAo', 'LingAo'),
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
    
    plot_list = forms.MultipleChoiceField(
        label=r'Plot(s)',
        choices=Diagnostics().figure_choices(),
        widget=forms.SelectMultiple(attrs={'size':'10'})
    )
    
    runtype = forms.ChoiceField(
        label='Run Type',
        choices=(
            ('All', 'All'),
            ('Physics', 'Physics'),
            ('ADCalib', 'ADCalib'),
            ('Pedestal', 'Pedestal'),
            ('FEEDiag', 'FEEDiag')
        )
    )

    run_list = forms.CharField(
        label='Run List', 
        widget=forms.Textarea(attrs={
            'style' : "width:200px; height:8em;",
        })
    )
        
    num_col = forms.IntegerField(
        label='Num. Columns', initial='3', max_value=10, required=False,
        widget=forms.TextInput(attrs={'size':'2'})
    )

    sort_run = forms.ChoiceField(
        label='Sort Run',
        choices=(
            ('ASC', 'ASC'),
            ('DESC', 'DESC'),
            ('None', 'None'),
        )
    )

# ==================================
class PQMSearchPlotsForm(SearchPlotsForm):
    
    plot_list = forms.MultipleChoiceField(
        label='Plot(s)',
        choices=Pqm().figure_choices(),
        widget=forms.SelectMultiple(attrs={'size':'10'})
    )


# ==================================
class RunProcessForm(forms.Form):
    
    cluster = forms.ChoiceField(
        choices=(
            ('pdsf', 'pdsf'),
            ('pdsfSim', 'pdsfSim'),
            ('local', 'local'),
        ),
    )
    
    job_name = forms.CharField(
        widget=forms.TextInput(attrs={'size':'10'})
    )
    
    run_no = forms.IntegerField(
        label='Run No.', min_value=1,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    seq_no = forms.IntegerField(
        label='Seq No.', min_value=1,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
# ==================================
class ViewRunProcessForm(RunProcessForm):
    
    print_state = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )

# ==================================
class BatchRunProcessForm(RunProcessForm):
        
    data_file = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'size':'50'})
    )

