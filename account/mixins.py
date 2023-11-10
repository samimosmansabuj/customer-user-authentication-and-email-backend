from django.shortcuts import redirect

class LogoutRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(LogoutRequiredMixin, self).dispatch(*args, **kwargs)