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
    
    figname = forms.MultipleChoiceField(
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
        
    num_col = forms.CharField(
        label='Num. Columns', initial='3', max_length=2,
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
    
    figname = forms.MultipleChoiceField(
        label='Plot Name',
        choices=Pqm().figure_choices(),
        widget=forms.SelectMultiple(attrs={'size':'10'})
    )
    


