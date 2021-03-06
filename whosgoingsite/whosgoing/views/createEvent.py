from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from whosgoing.models import Event, EventMember


class CreateEventView(CreateView):
    model = Event
    fields = ['name', 'description']

    def form_valid(self, form):
        out = super().form_valid(form)
        self.object.add_member(self.request.user)
        return out

createEventView = login_required(CreateEventView.as_view())
