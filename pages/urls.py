from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_page, name='pages-home'),
	path('portofolio/', views.portofolio, name='portofolio'),
	path('project/details/<str:pk>/', views.details_project, name='details-project'),

	path('project/create/', views.create_project, name='create_project'),
	path('project/update/<str:pk>/', views.update_project, name='update-project'),
    path('project/delete/<str:pk>/', views.delete_project, name='delete-project'),

    path('contact/', views.contact, name='contact'),

    path('certificates/', views.certificates, name='certificates'),
    path('certificates/create/', views.create_certificate, name='create_certificate'),
    path('certificates/delete/<str:pk>', views.delete_certificate, name='delete_certificate'),
    path('certificates/update/<str:pk>', views.update_certificate, name='update_certificate'),
    path('certificates/details/<int:pk>', views.certificate_details, name='certificate_details'),
	]