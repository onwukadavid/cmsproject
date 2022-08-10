from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.addTemplate, name="addtemplate"),
    path('edit/<id>', views.editTemplate, name="editTemplate"),
    path('template/create', views.saveTemplate, name="create_template"),
    path('editTemplate/<id>', views.editTemplateContent, name="editTemplateContent"),
    path('preview/<id>', views.previewTemplate, name="previewtemplate")
]