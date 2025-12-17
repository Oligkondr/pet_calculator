from django import forms


class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label="First number")
    number2 = forms.FloatField(label="Second number")
    operation = forms.ChoiceField(
        choices=[
            ('add', 'Addition'),
            ('sub', 'Subtraction'),
            ('mul', 'Multiplication'),
            ('div', 'Division'),
        ],
        label="Action"
    )
