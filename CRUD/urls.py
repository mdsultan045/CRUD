from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path("add",views.add, name="add"),
    path("edit",views.edit,name="edit"),
    path("update/<str:id>",views.update,name="update"),
    path("delete/<str:id>",views.delete,name="delete"),
    path('delete_records/<str:id>', views.delete_records, name='delete_records'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)