from django import forms
from .models import Promise, Evidence, Party, Position, Politician, Source, User, PartyValidity, Rating

class PromisesForm(forms.ModelForm):
    class Meta:
        model = Promise
        fields = ['title','description', 'politician', 'start_kpi', 'rating']
        # widget = {
        # 'title': forms.TextInput(attrs={'class':'form-control'}),
        # }
    title = forms.CharField(label='Title:', max_length=200, widget=forms.TextInput(
                              attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description:', max_length=200, widget=forms.Textarea(
                              attrs={'class': "form-control"}))                              
    politician = forms.ChoiceField(label='Politician:', widget=forms.Select(attrs={'class': "form-control"}))                                                            
    start_kpi = forms.CharField(label='Key performance indicator (KPI):', widget=forms.TextInput(attrs={'class': "form-control"}))                              
    rating = forms.CharField(label='Rating:', widget=forms.Select(choices=Rating.objects.all() ,attrs={'class': "form-control"}))    
    # fuentes = models.ManyToManyField(Source, related_name="promise_sources")
    # creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    # date = models.DateField(auto_now_add=True)
    # status = models.BooleanField(default=False)
