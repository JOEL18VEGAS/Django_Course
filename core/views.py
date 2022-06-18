from django.views.generic import View
from django.views.generic im

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')