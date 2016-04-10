from django import forms
from django.core.exceptions import ValidationError

from mothers.models import Mothers, Operators


class MotherForm(forms.ModelForm):

    registration_date = forms.DateField(label='Data Registrazione', required=True, widget=forms.DateInput(format='%d/%m/%Y'))
    operator = forms.ModelChoiceField(label='Operatore', required=True, queryset=Operators.objects.all())

    name = forms.CharField(label='Nome', required='True')
    surname = forms.CharField(label='Cognome', required='True')
    husband_surname = forms.CharField(label='Cognome Marito')

    place_of_birth = forms.CharField(label='Luogo nascita', required=True)
    date_of_birth = forms.DateField(label='Data nascita', required=True, widget=forms.DateInput(format='%d/%m/%Y'))

    city = forms.CharField(label='Citta')
    address = forms.CharField(label='Indirizzo')

    phone_1 = forms.CharField(label='Telefono1')
    phone_2 = forms.CharField(label='Telefono2')

    residency = forms.CharField(label='Cittadinanza')
    origin_country = forms.CharField(label='Stato provenienza')

    highest_academic_achievement = forms.CharField(label='Titolo studi')
    civil_status = forms.CharField(label='Stato civile')

    job = forms.CharField(label='Lavoro')
    husband_job = forms.CharField(label='Lavoro marito')

    income = forms.FloatField(label='Entrate', min_value=0)
    fixed_expenditures = forms.FloatField(label='Uscite fisse', min_value=0)

    notes = forms.CharField(label='Osservazioni', widget=forms.Textarea)

    class Meta:
        model = Mothers
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # if kwargs.get('instance'):
        #     kwargs.setdefault('initial', {})['name'] = kwargs['instance'].name
        #     kwargs.setdefault('initial', {})['surname'] = kwargs['instance'].surname
        ret = super(MotherForm, self).__init__(*args, **kwargs)

        self.rows = [
            [self['registration_date'], self['operator']],
            [self['name'], self['surname']],
            [self['husband_surname']],
            [self['place_of_birth'], self['date_of_birth']],
            [self['city'], self['address']],
            [self['phone_1'], self['phone_2']],
            [self['residency'], self['origin_country']],
            [self['highest_academic_achievement'], self['civil_status']],
            [self['job'], self['husband_job']],
            [self['income'], self['fixed_expenditures']],
            [self['notes']]
        ]
        self.date_fields = [self['registration_date'], self['date_of_birth']]
        self.large_fields = [self['notes']]
        self.disabled = False
        return ret

    def clean(self):
        # if self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email'):
        #     raise ValidationError("Email addresses must match.")

        return self.cleaned_data
