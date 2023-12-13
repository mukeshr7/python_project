from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phone_book/', include('Phone_Book.urls')),
    path('', RedirectView.as_view(url='phone_book/', permanent=False)),  # Redirect to 'phone_book/'
]
