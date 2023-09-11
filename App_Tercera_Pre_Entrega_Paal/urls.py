from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('novedad/', novedad,),
    path('libro/', libro),
    path('merchandising/', merchandising),
    path('consulta/', consulta),

]