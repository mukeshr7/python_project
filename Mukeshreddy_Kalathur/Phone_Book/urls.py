
from django.urls import path
from .views import list_contact, create_contact, update_contact, edit_contact, delete_contact

urlpatterns = [
    path('', list_contact, name='list_contact'),
    path('create/', create_contact, name='create_contact'),
    path('<int:contact_id>/', update_contact, name='update_contact'),
    path('<int:contact_id>/edit/', edit_contact, name='edit_contact'),
    path('<int:contact_id>/delete/', delete_contact, name='delete_contact'),
]
