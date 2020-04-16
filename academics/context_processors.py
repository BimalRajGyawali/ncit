from .models import Program
from notices.models import Notice


def get_context_global_variable(request):
    programs = Program.objects.all()
    side_bar_notices = Notice.get_notices_by_date()[:5]

    context = {
        'programs': programs,
        'side_bar_notices': side_bar_notices,
    }
    return context
