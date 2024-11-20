from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core.models import Visit
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from .forms import VisitUpdateForm, AdminVisitCreateForm
from .forms import BootstrapAuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse_lazy

CABINET_MENU = [
    {'title': 'Новые заявки', 'url': '/cabinet/new-visits/', 'icon': 'bi-bell', 'active': False},
    {'title': 'Подтвержденные заявки', 'url': '/cabinet/all-visits/', 'icon': 'bi-list-ul', 'active': False},
    {'title': 'Создать заявку', 'url': '/cabinet/create-visit/', 'icon': 'bi-plus-circle', 'active': False},
    {'title': 'Архив заявок', 'url': '/cabinet/visit-archive/', 'icon': 'bi-archive', 'active': False},
    {'title': 'Сменить пароль', 'url': '/cabinet/change-password/', 'icon': 'bi-key', 'active': False},
    {'title': 'Выйти', 'url': '/cabinet/logout/', 'icon': 'bi-box-arrow-right', 'active': False},
]


def get_cabinet_menu_context(current_url: str) -> dict:
    menu = []
    new_visits_count = Visit.objects.filter(status=0).count()
    confirmed_visits_count = Visit.objects.filter(status=1).count()

    for item in CABINET_MENU:
        menu_item = {
            'title': item['title'],
            'url': item['url'],
            'icon': item['icon'],
            'active': item['url'] == current_url,
            'badge_count': 0
        }

        if item['url'] == '/cabinet/new-visits/':
            menu_item['badge_count'] = new_visits_count
        elif item['url'] == '/cabinet/all-visits/':
            menu_item['badge_count'] = confirmed_visits_count

        menu.append(menu_item)

    return {"cabinet_menu": menu}


class LoginView(BaseLoginView):
    template_name = 'login.html'
    form_class = BootstrapAuthenticationForm
    next_page = reverse_lazy('cabinet:new_visits')
    redirect_authenticated_user = True


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('main'))


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Visit
    template_name = 'visits_list.html'
    context_object_name = 'visits'

    def get_queryset(self):
        visit_type = self.kwargs.get('visit_type')
        queryset = Visit.objects.all()

        if visit_type == 'new':
            queryset = queryset.filter(status=0)
            self.page_title = 'Новые заявки'
        elif visit_type == 'archive':
            queryset = queryset.filter(status__in=[2, 3])
            self.page_title = 'Архив заявок'
        else:
            queryset = queryset.filter(status=1)
            self.page_title = 'Подтвержденные заявки'

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context.update(get_cabinet_menu_context(self.request.path))
        return context


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('cabinet:all_visits')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_cabinet_menu_context(self.request.path))
        return context


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = 'visit_detail.html'
    context_object_name = 'visit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_cabinet_menu_context(self.request.path))
        return context


class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Visit
    success_url = reverse_lazy('cabinet:all_visits')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Visit
    form_class = VisitUpdateForm
    template_name = 'visit_update.html'

    def get_success_url(self):
        return reverse_lazy('cabinet:visit_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_cabinet_menu_context(self.request.path))
        return context


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Visit
    form_class = AdminVisitCreateForm
    template_name = 'visit_create.html'
    success_url = reverse_lazy('cabinet:all_visits')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_cabinet_menu_context(self.request.path))
        return context
