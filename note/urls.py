from django.urls import path
from . import views

app_name = "note"

urlpatterns = [
    path('', views.index, name="index"),
    path('api/protected/', views.ProtectedView.as_view(), name='protected'),

]