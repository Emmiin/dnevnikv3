from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

da_ne=(
    ("DA", "DA"),
    ("NE", "NE")
)

class Profile (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Profile'

from django.core.exceptions import ValidationError

#NAPRAVITI VALIDACIJU (TAKO DA PROCENTI, NPR. PROCENT HUMUSA
#BUDE IZMEĐU 0 I 100)
#def validate_percent(value):
    #if value<0 or value>100:
        #raise ValidationError(

        #)
class Analiza_zemljišta(models.Model):
    ACCESS_PUBLIC = 0
    ACCESS_PRIVATE = 1
    ACCESS_LEVEL_CHOICES = [
        (ACCESS_PUBLIC, 'Public'),
        (ACCESS_PRIVATE, 'Private'),
    ]
    kod_analize=models.CharField(max_length=5) #NAPRAVITI DEFAULT KOD
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    datum_analize=models.CharField(max_length=11)
    parcela=models.CharField(max_length=30)
    pH_M_KCL=models.IntegerField(default=4)
    pH_H_H2O=models.IntegerField(default=4)
    Humus_procent=models.IntegerField(default=4)#(validators=[validate_percent])
    CaCO3_procent=models.IntegerField(default=4)#(validators=[Humus_procentvalidate_percent])
    Azot_procent=models.IntegerField(default=4)#(validators=[validate_percent])
    Fosfor_procent=models.IntegerField(default=4)#(validators=[validate_percent])
    Kalij_procent=models.IntegerField(default=4)#(validators=[validate_percent])

    def __str__(self):
        return f"Analiza " + self.kod_analize

class Obrada_mr_prostora(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    vrsta_kulture=models.CharField(max_length=30)
    starost_zasada=models.CharField(max_length=30)
    trava=models.CharField(max_length=30)
    period_košenja=models.CharField(max_length=30)
    folija_malč=models.CharField(max_length=30)
    kultiviranje=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    plitko_oranje=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    datum=models.CharField(max_length=11)

class Obrada_r_prostora(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    vrsta_kulture=models.CharField(max_length=30)
    starost_zasada=models.CharField(max_length=30)
    folija_malč=models.CharField(max_length=30)
    kultiviranje=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    okopavanje=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    datum=models.CharField(max_length=11)

class Zasadi(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    vrsta_voća=models.CharField(max_length=30)
    sorta=models.CharField(max_length=30)
    godina_sadnje=models.CharField(max_length=5)
    površina=models.FloatField(max_length=5)
    broj_sadnica=models.IntegerField()
    broj_redova=models.IntegerField()

class Uzgojni_oblik(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    vrsta_kulture=models.CharField(max_length=30)
    sorta=models.CharField(max_length=30)
    uzgojni_oblik=models.CharField(max_length=30)
    razmak_sadnje=models.CharField(max_length=30)
    visina_krošnje=models.IntegerField()
    datum_sadnje=models.CharField(max_length=11)

class Rezidba(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    vrsta_kulture=models.CharField(max_length=30)
    sorta=models.CharField(max_length=30)
    zimska_rezidba=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )    
    termin_zimske_rezidbe=models.CharField(max_length=30)
    ljetna_rezidba=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )    
    termin_ljetne_rezidbe=models.CharField(max_length=11)
    zakidanje_izdanaka=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )       
    termin_zakidanja_izdanaka=models.CharField(max_length=11)

class Prihrana(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    kultura=models.CharField(max_length=30)
    stadij_rasta=models.CharField(max_length=30)
    datum_primjene=models.CharField(max_length=11)
    đubrivo=models.CharField(max_length=30)
    količina=models.CharField(max_length=10)
    način_primjene=models.CharField(max_length=30)
    svrha_primjene=models.CharField(max_length=30)

class Voda(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    kultura=models.CharField(max_length=30)
    stadij_rasta=models.CharField(max_length=30)
    količina_vode_m2_trajanje=models.CharField(max_length=30)   
    datum_navodnjavanja=models.CharField(max_length=11)
    vrijeme_navodnjavanja=models.CharField(max_length=5)
    temperatura_vode=models.CharField(max_length=11)
    način=models.CharField(max_length=30) 
    analiza=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )       

class Berba(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    kultura=models.CharField(max_length=30)
    sorta=models.CharField(max_length=30)
    početak_cvatnje=models.CharField(max_length=30)
    početak_berbe=models.CharField(max_length=30)   
    završetak_berbe=models.CharField(max_length=30)
    očekivani_prinos=models.CharField(max_length=30)   
    ostvareni_prinos=models.CharField(max_length=30)   
    ostvareni_prihod=models.CharField(max_length=30)     

class Mehanicke(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    malč=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    ) 
    mehaničko_suzbijanje_korova=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    spaljivanje_korova=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    agrotekstil=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    ljepljive_zamke=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )
    rezidba=models.CharField(
                    choices=da_ne,
                    default="NE",
                    max_length=2
                    )

class Bioloske(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    korištene_biljke=models.CharField(max_length=160)
    korišteni_organizmi=models.CharField(max_length=160)
    svrha_organizma=models.CharField(max_length=160)

class Biotehnicke(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    feromonske_zamke=models.CharField(max_length=160)
    svrha_feromonske_zamke=models.CharField(max_length=160)
    druge_zamke=models.CharField(max_length=160)
    svrha_drugih_zamki=models.CharField(max_length=160)

class Hemijske(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    parcela=models.CharField(max_length=30)
    datum_primjene=models.CharField(max_length=11)
    naziv_sredstva=models.CharField(max_length=160)
    količina_vode=models.CharField(max_length=160)
    koncentracija=models.CharField(max_length=160)
    svrha_primjene=models.CharField(max_length=160)

class Kontrola(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    godina=models.CharField(default=2011, max_length=4)
    aparat=models.CharField(max_length=160)
    godište=models.CharField(max_length=160)
    kontrolu_obavio=models.CharField(max_length=160)
    datum_kontrole=models.CharField(max_length=11)
    primjedba=models.CharField(max_length=160)

class Osposobljavanje(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    naziv_edukacije=models.CharField(max_length=160)
    organizator_edukacije=models.CharField(max_length=160)
    mjesto_održavanja=models.CharField(max_length=160)
    datum_održavanja=models.CharField(max_length=11)













    