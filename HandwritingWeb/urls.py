from django.urls import path
from . import views


urlpatterns = [
    path('', views.HandwritingView, name='HandwritingView'),
    path('answer/', views.ResultView, name='ResultView'),
    path('AboutProgram/', views.AboutProgramView, name='AboutProgramView')
]
