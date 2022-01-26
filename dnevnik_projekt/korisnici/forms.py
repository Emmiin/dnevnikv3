from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bioloske, Biotehnicke, Hemijske, Kontrola, Mehanicke, Berba, Osposobljavanje, Uzgojni_oblik, Analiza_zemljišta, Obrada_mr_prostora, Obrada_r_prostora, Zasadi, Rezidba, Prihrana,Voda
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]

class Analizaform(ModelForm):

    class Meta:
        model=Analiza_zemljišta
        fields=("kod_analize", "datum_analize", "parcela", "pH_M_KCL", "pH_H_H2O", "Humus_procent", "CaCO3_procent", "Azot_procent", "Fosfor_procent", "Kalij_procent")
        exceptions=("korisnik")

class Obrada_mr_form(ModelForm):

    class Meta:
        model=Obrada_mr_prostora
        fields=("godina", "parcela", "vrsta_kulture", "starost_zasada", "trava", "period_košenja", "folija_malč", "kultiviranje", "plitko_oranje", "datum")
        exceptions=("korisnik")

class Obrada_r_form(ModelForm):

    class Meta:
        model=Obrada_r_prostora
        fields=("godina", "parcela", "vrsta_kulture", "starost_zasada", "folija_malč", "kultiviranje", "okopavanje", "datum")
        exceptions=("korisnik")

class Zasadi_form(ModelForm):

    class Meta:
        model=Zasadi
        fields=("godina", "parcela", "vrsta_voća", "sorta", "godina_sadnje", "površina", "broj_sadnica", "broj_redova")
        exceptions=("korisnik")

class Uzgojni_oblik_form(ModelForm):

    class Meta:
        model=Uzgojni_oblik
        fields=("godina", "parcela", "vrsta_kulture", "sorta", "uzgojni_oblik", "razmak_sadnje", "visina_krošnje", "datum_sadnje")
        exceptions=("korisnik")

class Rezidba_form(ModelForm):

    class Meta:
        model=Rezidba
        fields=("godina", "parcela", "vrsta_kulture", "sorta", "zimska_rezidba", "termin_zimske_rezidbe", "ljetna_rezidba", "termin_ljetne_rezidbe", "zakidanje_izdanaka", "termin_zakidanja_izdanaka")
        exceptions=("korisnik")

class Prihrana_form(ModelForm):

    class Meta:
        model=Prihrana
        fields=("godina", "parcela", "kultura", "stadij_rasta", "datum_primjene", "đubrivo", "količina", "način_primjene", "svrha_primjene")
        exceptions=("korisnik")

class Voda_form(ModelForm):

    class Meta:
        model=Voda
        fields=("godina", "parcela", "kultura", "stadij_rasta", "količina_vode_m2_trajanje", "datum_navodnjavanja", "vrijeme_navodnjavanja", "temperatura_vode", "način", "analiza")
        exceptions=("korisnik")

class Berba_form(ModelForm):

    class Meta:
        model=Berba
        fields=("godina", "parcela", "kultura", "sorta", "početak_cvatnje", "početak_berbe", "završetak_berbe", "očekivani_prinos", "ostvareni_prinos", "ostvareni_prihod")
        exceptions=("korisnik")

class Mehanicke_form(ModelForm):

    class Meta:
        model=Mehanicke
        fields=("godina", "parcela", "malč", "mehaničko_suzbijanje_korova", "spaljivanje_korova", "agrotekstil", "ljepljive_zamke", "rezidba")
        exceptions=("korisnik")

class Bioloske_form(ModelForm):

    class Meta:
        model=Bioloske
        fields=("godina", "parcela", "korištene_biljke", "korišteni_organizmi", "svrha_organizma")
        exceptions=("korisnik")

class Biotehnicke_form(ModelForm):

    class Meta:
        model=Biotehnicke
        fields=("godina", "parcela", "feromonske_zamke", "svrha_feromonske_zamke", "druge_zamke", "svrha_drugih_zamki")
        exceptions=("korisnik")

class Hemijske_form(ModelForm):

    class Meta:
        model=Hemijske
        fields=("godina", "parcela", "datum_primjene", "naziv_sredstva", "količina_vode", "koncentracija", "svrha_primjene")
        exceptions=("korisnik")

class Kontrola_form(ModelForm):

    class Meta:
        model=Kontrola
        fields=("godina", "aparat", "godište", "kontrolu_obavio", "datum_kontrole", "primjedba")
        exceptions=("korisnik")

class Osposobljavanje_form(ModelForm):

    class Meta:
        model=Osposobljavanje
        fields=("naziv_edukacije", "organizator_edukacije", "mjesto_održavanja", "datum_održavanja")
        exceptions=("korisnik")