from django import forms
from .models import Jackets
from PIL import Image

SEX_CHOICES = (
    ('男性', '男性'),
    ('女性', '女性'),
    ('兼用', '兼用'),
)

SIZE_CHOICES = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
)

BLAND_CHOICES = (
    ('クロクロ', 'クロクロ'),
    ('SARA', 'SARA'),
    ('UNITED JAPAN', 'UNITED JAPAN'),
    ('HAGE', 'HAGE'),
    ('PACOSTE', 'PACOSTE'),
    ('SZUDIOUS', 'SZUDIOUS'),
    ('Grocky Monkey', 'Grocky Monkey'),
    ('IDONM', 'IDONM'),
)

class JacketsForm(forms.Form):
    jacket_name = forms.CharField(max_length=20)
    jacket_price = forms.CharField(max_length=10)
    jacket_size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    jacket_sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    jacket_bland = forms.ChoiceField(
        choices=BLAND_CHOICES,
    )
    jacket_stock = forms.CharField(max_length=3)
    jacket_image = forms.ImageField()

class ShirtsForm(forms.Form):
    shirt_name = forms.CharField(max_length=20)
    shirt_price = forms.CharField(max_length=10)
    shirt_size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    shirt_sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    shirt_bland = forms.ChoiceField(
        choices=BLAND_CHOICES,
    )
    shirt_stock = forms.CharField(max_length=3)
    shirt_image = forms.ImageField()

class PantsForm(forms.Form):
    pant_name = forms.CharField(max_length=20)
    pant_price = forms.CharField(max_length=10)
    pant_size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    pant_sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    pant_bland = forms.ChoiceField(
        choices=BLAND_CHOICES,
    )
    pant_stock = forms.CharField(max_length=3)
    pant_image = forms.ImageField()

class ShoesForm(forms.Form):
    shoe_name = forms.CharField(max_length=20)
    shoe_price = forms.CharField(max_length=10)
    shoe_size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    shoe_sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    shoe_bland = forms.ChoiceField(
        choices=BLAND_CHOICES,
    )
    shoe_stock = forms.CharField(max_length=3)
    shoe_image = forms.ImageField()

class CartListForm(forms.Form):
    purchase_num = forms.CharField(max_length=3)




