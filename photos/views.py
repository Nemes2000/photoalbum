from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Photo
from .forms import PhotoForm, UserRegisterForm

class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'
    context_object_name = 'photos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', '-upload_date')
        if sort_by == 'name':
            return queryset.order_by('name')
        elif sort_by == '-name':
            return queryset.order_by('-name')
        elif sort_by == 'upload_date':
            return queryset.order_by('upload_date')
        else:  # Default to newest first
            return queryset.order_by('-upload_date')

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo_detail.html'
    context_object_name = 'photo'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photos/photo_form.html'
    success_url = reverse_lazy('photo_list')

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        messages.success(self.request, 'A kép sikeresen feltöltve!')
        return super().form_valid(form)

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo_list')
    template_name = 'photos/photo_confirm_delete.html'

    def get_queryset(self):
        # Only allow users to delete their own photos
        return Photo.objects.filter(uploader=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'A kép sikeresen törölve!')
        return super().delete(request, *args, **kwargs)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Sikeresen regisztráltál, {username}! Most már bejelentkezhetsz.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
