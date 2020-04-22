from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import RegistrationForm


class SignupView(CreateView):
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('account:signup-done')

    def form_valid(self, form):

        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password2'])
        new_user.save()

        return super().form_valid(form)


class SignupDoneView(TemplateView):

    template_name = 'account/registration_done.html'
