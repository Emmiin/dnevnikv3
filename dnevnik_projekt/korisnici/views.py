from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from korisnici.forms import Mehanicke_form, Analizaform, Obrada_mr_form, Obrada_r_form, Osposobljavanje_form, UserRegisterForm, Zasadi_form, Uzgojni_oblik_form, Rezidba_form, Prihrana_form, Voda_form, Berba_form, Bioloske_form, Biotehnicke_form, Hemijske_form, Kontrola_form
from korisnici.models import Bioloske, Biotehnicke, Hemijske, Mehanicke, Osposobljavanje, Analiza_zemljišta, Obrada_mr_prostora, Obrada_r_prostora, Zasadi, Uzgojni_oblik, Rezidba, Prihrana, Voda, Berba, Kontrola



def home(request):
    
    if request.user.is_authenticated:
        return render (request, "korisnici/profile.html")
    else:
        context= {
            "analize":Analiza_zemljišta.objects.all()
        }
        return render(request, 'korisnici/home.html', context)
    

def about(request):
    context= {
    "analize":Analiza_zemljišta.objects.all()
    }
    return render(request, 'korisnici/about.html', context)

def kontakt(request):
    return render(request, 'korisnici/kontakt.html')

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request, f"Nalog je napravljen! Možete se sada prijaviti!")
            return redirect("login")
    else:
        form=UserRegisterForm()
    return render (request, "korisnici/register.html", {"form": form})

@login_required
def profile(request):
        return render (request, "korisnici/profile.html")

@login_required
def analize(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Analizaform(request.POST)
        context= {
                "analize":Analiza_zemljišta.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za analizu korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/analize.html", context)
    else:
        form=Analizaform()
        context= {
            "analize":Analiza_zemljišta.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za analizu korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/analize.html", context)

@login_required
def obrada_mr(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Obrada_mr_form(request.POST)
        context= {
                "analize":Obrada_mr_prostora.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/odrzavanjemr.html", context)
    else:
        form=Obrada_mr_form()
        context= {
            "analize":Obrada_mr_prostora.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/odrzavanjemr.html", context)

@login_required
def obrada_r(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Obrada_r_form(request.POST)
        context= {
                "analize":Obrada_r_prostora.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/odrzavanjer.html", context)
    else:
        form=Obrada_r_form()
        context= {
            "analize":Obrada_r_prostora.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/odrzavanjer.html", context)

@login_required
def zasadi(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Zasadi_form(request.POST)
        context= {
                "analize":Zasadi.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/zasadi.html", context)
    else:
        form=Zasadi_form()
        context= {
            "analize":Zasadi.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/zasadi.html", context)

@login_required
def uzgojni(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Uzgojni_oblik_form(request.POST)
        context= {
                "analize":Uzgojni_oblik.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/uzgojni.html", context)
    else:
        form=Uzgojni_oblik_form()
        context= {
            "analize":Uzgojni_oblik.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/uzgojni.html", context)

@login_required
def rezidba(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Rezidba_form(request.POST)
        context= {
                "analize":Rezidba.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/rezidba.html", context)
    else:
        form=Rezidba_form()
        context= {
            "analize":Rezidba.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/rezidba.html", context)

@login_required
def prihrana(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Prihrana_form(request.POST)
        context= {
                "analize":Prihrana.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/prihrana.html", context)
    else:
        form=Prihrana_form()
        context= {
            "analize":Prihrana.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/prihrana.html", context)

@login_required
def voda(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Voda_form(request.POST)
        context= {
                "analize":Voda.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/navodnjavanje.html", context)
    else:
        form=Voda_form()
        context= {
            "analize":Voda.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/navodnjavanje.html", context)

@login_required
def berba(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Berba_form(request.POST)
        context= {
                "analize":Berba.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/berba.html", context)
    else:
        form=Berba_form()
        context= {
            "analize":Berba.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/berba.html", context)

@login_required
def mehanicke(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Mehanicke_form(request.POST)
        context= {
                "analize":Mehanicke.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/mehanicke.html", context)
    else:
        form=Mehanicke_form()
        context= {
            "analize":Mehanicke.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/mehanicke.html", context)

@login_required
def bioloske(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Bioloske_form(request.POST)
        context= {
                "analize":Bioloske.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/bioloske.html", context)
    else:
        form=Bioloske_form()
        context= {
            "analize":Bioloske.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/bioloske.html", context)

@login_required
def biotehnicke(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Biotehnicke_form(request.POST)
        context= {
                "analize":Biotehnicke.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/biotehnicke.html", context)
    else:
        form=Biotehnicke_form()
        context= {
            "analize":Biotehnicke.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/biotehnicke.html", context)

@login_required
def hemijske(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Hemijske_form(request.POST)
        context= {
                "analize":Hemijske.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/hemijske.html", context)
    else:
        form=Hemijske_form()
        context= {
            "analize":Hemijske.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/hemijske.html", context)

@login_required
def kontrola(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Kontrola_form(request.POST)
        context= {
                "analize":Kontrola.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/kontrola.html", context)
    else:
        form=Kontrola_form()
        context= {
            "analize":Kontrola.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/kontrola.html", context)


@login_required
def osposobljavanje(request):
    current_user = request.user.get_username()
    if request.method=="POST":
        form = Osposobljavanje_form(request.POST)
        context= {
                "analize":Osposobljavanje.objects.filter(korisnik=request.user),
                "form":form,
                }
        if form.is_valid():
            form=form.save(commit=False)
            form.korisnik=request.user
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
            return render(request, "korisnici/osposobljavanje.html", context)
    else:
        form=Osposobljavanje_form()
        context= {
            "analize":Osposobljavanje.objects.filter(korisnik=request.user),
            "form":form
            }
        if form.is_valid():
            form.save()
            messages.success(request, f"Prihvaćeni rezultati za korisnika {current_user}!")
            form=form.clean
        return render (request, "korisnici/osposobljavanje.html", context)