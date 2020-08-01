from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import NoteForm
from webapp.models import Note, STATUS_CHOICE, DEFAUL_STATUS


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        order_date = Note.objects.all()
    else:
        order_date = Note.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={
        'notes': order_date,
        'status': STATUS_CHOICE
    })


def note_create(request):
    if request.method == "GET":
        return render(request, 'create_new_note.html', context={
            'form': NoteForm()
        })
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = Note.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status'],
            )
            return redirect('index')
        else:
            return render(request, 'create_new_note.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "GET":
        form = NoteForm(initial={
            'name': note.name,
            'email': note.email,
            'text': note.text,
            'status': note.status})
        return render(request, 'note_update.html', context={
            'form': form,
            'note': note
        })
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note.name = form.cleaned_data['name']
            note.email = form.cleaned_data['email']
            note.text = form.cleaned_data['text']
            note.status = form.cleaned_data['status']
            note.save()
            return redirect('index')
        else:
            return render(request, 'note_update.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])