from django import forms
class PetFilterForm(forms.Form):
    CHOICES_PET = (('cat', 'Cat'),
                   ('dog', 'Dog'))
    CHOICES_TYPE_IMG = (('png', 'png'),
                        ('gif', 'gif'),
                        ('jpg', 'jpg'),
                        ('jpeg', 'jpeg'))

    pet = forms.ChoiceField(choices=CHOICES_PET)
    type_img = forms.ChoiceField(choices=CHOICES_TYPE_IMG)