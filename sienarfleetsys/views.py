from django.shortcuts import render
from django.views.generic import ListView
from sienarfleetsys.models import Ship
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django import forms

# Create your views here.
class ShipsList(TemplateView):
    model = Ship
    template_name = 'ships_list.html'
    
    def compareShip(self, request):
        form = self.form_class(request.POST)
        self.ship1 = get_object_or_404(Ship, name__iexact=self.args[0]) 
        self.ship2 = get_object_or_404(Ship, name__iexact=self.args[1]) 
        return HttpResponse(self.ship1)
        
    def post(self, request, *args, **kwargs):
        ship1Name = request.POST['ship1']
        ship2Name = request.POST.get('ship2')
        self.ship1 = get_object_or_404(Ship, nome__iexact=ship1Name) 
        self.ship2 = get_object_or_404(Ship, nome__iexact=ship2Name) 
        
        response = HttpResponse(content_type='text/html')
        
        #Arma primaria
        if self.ship1.armaprimaria > self.ship2.armaprimaria:
            response.write('<p>Arma primaria da '+ self.ship1.nome +' = '+ str(self.ship1.armaprimaria) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.armaprimaria)+'</p>')
        elif self.ship1.armaprimaria == self.ship2.armaprimaria:
            response.write('<p>Arma primaria da '+ self.ship1.nome +' = '+ str(self.ship1.armaprimaria) + ' &eacute; igual &agrave; arma da nave '+ self.ship2.nome +' = '+ str(self.ship2.armaprimaria)+'</p>')
        else:
            response.write('<p>Arma primaria da '+ self.ship2.nome +' = '+ str(self.ship2.armaprimaria) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.armaprimaria)+'</p>')
        
        #Agilidade
        if self.ship1.agilidade > self.ship2.agilidade:
            response.write('<p>Agilidade da '+ self.ship1.nome +' = '+ str(self.ship1.agilidade) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.agilidade)+'</p>')
        elif self.ship1.agilidade == self.ship2.agilidade:
            response.write('<p>Agilidade da '+ self.ship1.nome +' = '+ str(self.ship1.agilidade) + ' &eacute; igual &agrave; agilidade da nave '+ self.ship2.nome +' = '+ str(self.ship2.agilidade)+'</p>')
        else:
            response.write('<p>Agilidade da '+ self.ship2.nome +' = '+ str(self.ship2.agilidade) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.agilidade)+'</p>')
        
        #Casco
        if self.ship1.casco > self.ship2.casco:
            response.write('<p>Casco da '+ self.ship1.nome +' = '+ str(self.ship1.casco) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.casco)+'</p>')
        elif self.ship1.casco == self.ship2.casco:
            response.write('<p>Casco da '+ self.ship1.nome +' = '+ str(self.ship1.casco) + ' &eacute; igual ao casco da nave '+ self.ship2.nome +' = '+ str(self.ship2.casco)+'</p>')
        else:
            response.write('<p>Casco da '+ self.ship2.nome +' = '+ str(self.ship2.casco) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.casco)+'</p>')
        
        #Escudo
        if self.ship1.escudo > self.ship2.escudo:
            response.write('<p>Escudo da '+ self.ship1.nome +' = '+ str(self.ship1.escudo) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.escudo)+'</p>')
        elif self.ship1.escudo == self.ship2.escudo:
            response.write('<p>Escudo da '+ self.ship1.nome +' = '+ str(self.ship1.escudo) + ' &eacute; igual ao escudo da nave '+ self.ship2.nome +' = '+ str(self.ship2.escudo)+'</p>')
        else:
            response.write('<p>Escudo da '+ self.ship2.nome +' = '+ str(self.ship2.escudo) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.escudo)+'</p>')  

        #customin
        if self.ship1.customin > self.ship2.customin:
            response.write('<p>Custo m&iacute;nimo da '+ self.ship1.nome +' = '+ str(self.ship1.customin) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.customin)+'</p>')
        elif self.ship1.customin == self.ship2.customin:
            response.write('<p>Custo m&iacute;nimo '+ self.ship1.nome +' = '+ str(self.ship1.customin) + ' &eacute; igual ao Custo m&iacute;nimo da nave '+ self.ship2.nome +' = '+ str(self.ship2.customin)+'</p>')
        else:
            response.write('<p>Custo m&iacute;nimo '+ self.ship2.nome +' = '+ str(self.ship2.customin) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.customin)+'</p>')
        
        #customax
        if self.ship1.customax > self.ship2.customax:
            response.write('<p>Custo m&aacute;ximo da '+ self.ship1.nome +' = '+ str(self.ship1.customax) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.customax)+'</p>')
        elif self.ship1.customax == self.ship2.customax:
            response.write('<p>Custo m&aacute;ximo '+ self.ship1.nome +' = '+ str(self.ship1.customax) + ' &eacute; igual ao Custo m&aacute;ximo da nave '+ self.ship2.nome +' = '+ str(self.ship2.customax)+'</p>')
        else:
            response.write('<p>Custo m&aacute;ximo '+ self.ship2.nome +' = '+ str(self.ship2.customax) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.customax)+'</p>')
        
        #Arma secundaria
        if self.ship1.armasecundaria > self.ship2.armasecundaria:
            response.write('<p>Arma secundaria da '+ self.ship1.nome +' = '+ str(self.ship1.armasecundaria) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.armasecundaria)+'</p>')
        elif self.ship1.armasecundaria == self.ship2.armasecundaria:
            response.write('<p>Arma secundaria da '+ self.ship1.nome +' = '+ str(self.ship1.armasecundaria) + ' &eacute; igual &agrave; arma da nave '+ self.ship2.nome +' = '+ str(self.ship2.armasecundaria)+'</p>')
        else:
            response.write('<p>Arma secundaria da '+ self.ship2.nome +' = '+ str(self.ship2.armasecundaria) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.armasecundaria)+'</p>')
         
        #Manobrabilidade
        if self.ship1.manobrabilidade > self.ship2.manobrabilidade:
            response.write('<p>Manobrabilidade da '+ self.ship1.nome +' = '+ str(self.ship1.manobrabilidade) + ' &eacute; maior que da nave '+ self.ship2.nome +' = '+ str(self.ship2.manobrabilidade)+'</p>')
        elif self.ship1.manobrabilidade == self.ship2.manobrabilidade:
            response.write('<p>Manobrabilidade da '+ self.ship1.nome +' = '+ str(self.ship1.manobrabilidade) + ' &eacute; igual &agrave; manobrabilidade da nave '+ self.ship2.nome +' = '+ str(self.ship2.manobrabilidade)+'</p>')
        else:
            response.write('<p>Manobrabilidade da '+ self.ship2.nome +' = '+ str(self.ship2.manobrabilidade) + ' &eacute; maior que da nave '+ self.ship1.nome +' = '+ str(self.ship1.manobrabilidade)+'</p>')
        
        return response
#class ShipForm(forms.ModelForm):
#    class Meta:
#       model = Ship
#        fields = ('nome', 'armaprimaria',)
#    
#    def post_new(request):
#        form = ShipForm()
#        return render(request, 'compare2.html', {'form': form})