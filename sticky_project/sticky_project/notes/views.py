from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator


# List Notes
@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'note_list.html', {'notes': notes})

# Create Note
@login_required
def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.owner = request.user
        note.save()
        return redirect('note_list')
    return render(request, 'note_form.html', {'form': form})

# Edit Note
@login_required
def note_edit(request, id):
    note = get_object_or_404(Note, id=id, owner=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'note_form.html', {'form': form})

# Delete Note
@login_required
def note_delete(request, id):
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})

# Register
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('note_list')
    return render(request, 'register.html', {'form': form})



def note_list(request):
    query = request.GET.get('q')
    notes = Note.objects.filter(owner=request.user).order_by('-is_pinned', '-created_at')

    if query:
        notes = notes.filter(title__icontains=query) | notes.filter(content__icontains=query)

    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'note_list.html', {'page_obj': page_obj})