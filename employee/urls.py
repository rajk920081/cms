from django.urls import path
from .views import index
from .views import adde,update_emp
from .views import deletecus
urlpatterns = [
    path('',index, name="index"),
    path('adde/',adde),
    path('update/<id>/',update_emp, name="update"),
    path('delete/<id>/',deletecus, name='delete')
]