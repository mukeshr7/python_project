from django.urls import path
from .views import list_contact, create_contact, detail_contact, edit_contact, delete_contact

app_name = 'Phone_Book'

urlpatterns = [
    path('', list_contact, name='list_contact'),
    path('create/', create_contact, name='create_contact'),
    path('<int:contact_id>/', detail_contact, name='detail_contact'),
    path('<int:contact_id>/edit/', edit_contact, name='edit_contact'),  # Make sure this line is present
    path('<int:contact_id>/delete/', delete_contact, name='delete_contact'),
]
