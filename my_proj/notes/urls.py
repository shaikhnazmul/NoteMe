from django.urls import path

from notes import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('view/<int:pk>', views.note_view, name='note_view'),
    path('new', views.note_create, name='note_new'),
    path('edit/<int:pk>', views.note_update, name='note_edit'),
    path('delete/<int:pk>', views.note_delete, name='note_delete'),
]