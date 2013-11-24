from django.forms import ModelForm, RadioSelect, HiddenInput

from game.models import Kind, Opponent, Player, Round, Question, Option, Answer

class OfferAcceptanceForm(ModelForm):
    class Meta:
        model = Round
        fields = ['accepted', 'time_elapsed']
        widgets = { 'accepted': RadioSelect, 'time_elapsed' : HiddenInput }

class QuestionnaireForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['option']
        widgets = { 'option': RadioSelect }
    
    #def clean_option(self):
    #    option = self.cleaned_data['option']
    #    return Option.objects.get(id=option)