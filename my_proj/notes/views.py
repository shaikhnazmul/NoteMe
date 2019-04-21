from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from notes.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'serial']

def note_list(request, template_name='notes/note_list.html'):
    note = Note.objects.all()
    data = {}
    data['object_list'] = note
    return render(request, template_name, data)

def note_view(request, pk, template_name='notes/note_detail.html'):
    note= get_object_or_404(Note, pk=pk)    
    return render(request, template_name, {'object':note})

def note_create(request, template_name='notes/note_form.html'):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, template_name, {'form':form})

def note_update(request, pk, template_name='notes/note_form.html'):
    note= get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, template_name, {'form':form})

def note_delete(request, pk, template_name='notes/note_confirm_delete.html'):
    note= get_object_or_404(Note, pk=pk)    
    if request.method=='POST':
        note.delete()
        return redirect('note_list')
    return render(request, template_name, {'object':note})