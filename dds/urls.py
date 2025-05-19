from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_record, name="create_record"),
    path("edit/<int:pk>/", views.edit_record, name="edit_record"),
    path("delete/<int:pk>/", views.delete_record, name="delete_record"),
    path("get_subcategories/", views.get_subcategories, name="get_subcategories"),
    path("get_categories/", views.get_categories, name="get_categories"),
    path("dictionaries/", views.dictionaries, name="dictionaries"),
]
