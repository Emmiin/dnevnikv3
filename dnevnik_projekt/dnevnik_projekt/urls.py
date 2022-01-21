"""dnevnik_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from korisnici import views as korisnici_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path("registracija/", korisnici_views.register, name="register"),
    path("analize/", korisnici_views.analize, name="analize"),
    path("prijava/", auth_views.LoginView.as_view(template_name="korisnici/login.html"), name="login"),
    path("odjava/", auth_views.LogoutView.as_view(template_name="korisnici/logout.html"), name="logout"),
    path("profil/", korisnici_views.profile, name="profile"),
    path("analize/", korisnici_views.analize, name="analize"),
    path("obrada_meduredna/", korisnici_views.obrada_mr, name="obrada_mr"),
    path("obrada_redna/", korisnici_views.obrada_r, name="obrada_r"),
    path("zasadi/", korisnici_views.zasadi, name="zasadi"),
    path("uzgojni_oblik/", korisnici_views.uzgojni, name="uzgojni"),
    path("rezidba/", korisnici_views.rezidba, name="rezidba"),
    path("prihrana/", korisnici_views.prihrana, name="prihrana"),
    path("navodnjavanje/", korisnici_views.voda, name="voda"),
    path("berba/", korisnici_views.berba, name="berba"),
    path("mehanicke-mjere-zastite/", korisnici_views.mehanicke, name="mehanicke"),
    path("bioloske-mjere-zastite/", korisnici_views.bioloske, name="bioloske"),
    path("biotehnicke-mjere-zastite/", korisnici_views.biotehnicke, name="biotehnicke"),
    path("hemijske-mjere-zastite/", korisnici_views.hemijske, name="hemijske"),
    path("kontrola-aparata-za-primjenu-hemijskih-sredstava/", korisnici_views.kontrola, name="kontrola"),
    path("stručno-osposobljavanje/", korisnici_views.hemijske, name="osposobljavanje"),
    path("kontakt/", korisnici_views.kontakt, name="kontakt"),



    path("", include("korisnici.urls")),
]

urlpatterns+=staticfiles_urlpatterns()