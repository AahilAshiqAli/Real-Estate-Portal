from django.contrib import admin
from django.urls import path
from polls import views

admin.site.site_header = "Elite Estate Royce | Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Hello"

urlpatterns = [
    path('', views.index,name='home'),
    path('housing',views.housing,name='housing'),
    path('commercial',views.commercial, name="commercial"),
    path('upload',views.upload,name='upload'),
    path('contact',views.contact,name='contact'),
    path('login',views.loginUser,name = 'login'),
    path('logout',views.logoutUser,name = 'logout'),
    path('details/<int:house_id>/',views.details,name = 'details')
]