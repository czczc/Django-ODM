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
            ('local', 'local'),
        ),
    )
    
    job_name = forms.ChoiceField(
        choices=(
            ('odm_v3', 'odm_v3'),
            ('odm_v2', 'odm_v2'),
            ('adBasicFigs', 'adBasicFigs'),
            ('nuwaConvert_v1', 'nuwaConvert_v1'),
        ),
    )
    
    run_no = forms.IntegerField(
        label='Run No.', min_value=1,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    seq_no = forms.IntegerField(
        label='Seq No.', min_value=1, required=False,
        widget=forms.TextInput(attrs={'size':'6'})
    )
     
# ==================================
class ViewRunProcessForm(RunProcessForm):
    
    print_state = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )

# ==================================
class ClearRunProcessForm(RunProcessForm):
    
    all_sequences = forms.BooleanField(required=False)
      
    clear_sequence = forms.BooleanField(required=False)
    
    clear_stats = forms.BooleanField(required=False)
    
    clear_summary = forms.BooleanField(required=False)
    
    dry_run = forms.BooleanField(required=False)

# ==================================
class ProcessRunProcessForm(RunProcessForm):
    
    run_no = forms.IntegerField(
        label='Run No.', min_value=1, required=False,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    all_sequences = forms.BooleanField(required=False)
    
    batch = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )
    
    run_nuwa = forms.BooleanField(
        label='Run NuWa', required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )       
    
    add_stats = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )
    
    summarize_run = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )
        
    dry_run = forms.BooleanField(required=False)
    
    data_file = forms.CharField(required=False)
    
    def clean(self):
        '''custom validation'''
        import os
        cleaned_data = self.cleaned_data
        
        data_file = cleaned_data.get('data_file')
        if data_file:
            # skip file exist check because 'apache' does not have permission for most directories
            basename = os.path.basename(data_file)
            tokens = basename.split('.')
            if len(tokens) != 8 or tokens[-1] not in ['root', 'data']:
                msg = 'Invalid file name format.'
                self._errors['data_file'] = self.error_class([msg])
                del cleaned_data['data_file']
        
        return cleaned_data


# ==================================
class SimulationRunProcessForm(forms.Form):
    
    cluster = forms.ChoiceField(
        choices=(
            ('pdsfSim', 'pdsfSim'),
            ('local', 'local'),
        ),
    )
    
    job_name = forms.ChoiceField(
        choices=(
            ('odmSim_v4', 'odmSim_v4'),
            ('odmSim_v2', 'odmSim_v2'),
        ),
    )

# ==================================
class SimulationViewRunProcessForm(SimulationRunProcessForm):
    
    run_no = forms.IntegerField(
        label='Run No.', min_value=1,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    seq_no = forms.IntegerField(
        label='Seq No.', min_value=1, required=False,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    print_state = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )

# ==================================
class SimulationClearRunProcessForm(SimulationRunProcessForm):
    
    run_no = forms.IntegerField(
        label='Run No.', min_value=1,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    seq_no = forms.IntegerField(
        label='Seq No.', min_value=1, required=False,
        widget=forms.TextInput(attrs={'size':'6'})
    )
    
    all_sequences = forms.BooleanField(required=False)
      
    clear_sequence = forms.BooleanField(required=False)
    
    clear_stats = forms.BooleanField(required=False)
    
    clear_summary = forms.BooleanField(required=False)
    
    dry_run = forms.BooleanField(required=False)
    
# ==================================
class SimulationProcessRunProcessForm(SimulationRunProcessForm):
        
    batch = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )
    
    run_nuwa = forms.BooleanField(
        label='Run NuWa', required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )       
    
    add_stats = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )
    
    summarize_run = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(check_test=lambda x: True),
    )
        
    dry_run = forms.BooleanField(required=False)
    
    data_file = forms.CharField()
    
    def clean(self):
        '''custom validation'''
        import os
        cleaned_data = self.cleaned_data
        
        data_file = cleaned_data.get('data_file')
        if data_file:
            # skip file exist check because 'apache' does not have permission for most directories
            basename = os.path.basename(data_file)
            tokens = basename.split('.')
            if len(tokens) != 8 or tokens[-1] not in ['root', 'data']:
                msg = 'Invalid file name format.'
                self._errors['data_file'] = self.error_class([msg])
                del cleaned_data['data_file']
        
        return cleaned_data
