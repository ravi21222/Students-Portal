from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('notes/',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete_note"),
    path('notes_detail/<int:pk>',views.Notesdetailedview.as_view(),name='notes_detail'),
    path('homework/',views.homework,name='homework'),
]
