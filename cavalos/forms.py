from django import forms
from django.forms import ClearableFileInput
from .models import Cavalo

class CavaloForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'text', 'id': 'data_nascimento', 'placeholder': 'dd/mm/aaaa', 'class': 'form-control'}),
        input_formats=['%d/%m/%Y', '%d/%m/%y'],
        label='Data de Nascimento'
    )

    class Meta:
        model = Cavalo
        fields = '__all__'  
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'foto': ClearableFileInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'foto' in self.fields:
            self.fields['foto'].widget.clear_checkbox_label = ''
            self.fields['foto'].widget.initial_text = ''
            self.fields['foto'].widget.input_text = 'Selecionar nova foto'