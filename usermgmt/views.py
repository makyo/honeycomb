from django.contrib.auth import (
    authenticate,
    login,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import (
    render,
)
from django.views.generic import FormView

from .forms import (
    RegisterForm,
    UpdateProfileForm,
)
from .models import (
    Profile,
)


class Register(FormView):
    template_name = 'registration/new.html'
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
        new_profile = Profile(user=new_user)
        new_profile.save()
        login(self.request, new_user)
        return super(Register, self).form_valid(form)

    def get_success_url(self):
        return self.request.POST.get(
            'next', self.request.GET.get('next', reverse('front')))

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['title'] = 'Register'
        return context


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user.profile)
        form.save()
    form = UpdateProfileForm(instance=request.user.profile)
    return render(request,
                  'update_profile.html',
                  {'title': 'Update profile', 'form': form})


def view_profile(request, username):
    user = User.objects.get(username=username)
    watched = blocked = blocked_by = False
    if request.user.is_authenticated:
        watched = user in request.user.profile.watched_users.all()
        blocked = user in request.user.profile.blocked_users.all()
        blocked_by = request.user in user.profile.blocked_users.all()
    subtitle = ''
    display_name = user.profile.get_display_name()
    if watched:
        display_name = '&#x2606; {}'.format(display_name)
        subtitle = "following"
    if blocked:
        display_name = '&#x20e0; {}'.format(display_name)
        subtitle = "blocked"
    return render(request,
                  'view_profile.html',
                  {
                      'title': display_name,
                      'subtitle': subtitle,
                      'user_profile': user,
                      'watched': watched,
                      'blocked': blocked,
                      'blocked_by': blocked_by,
                  })
