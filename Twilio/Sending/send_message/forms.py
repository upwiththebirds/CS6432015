from django import forms
 
class Msg(forms.Form):
    phone = forms.IntegerField()
    msg = forms.CharField(max_length=160)