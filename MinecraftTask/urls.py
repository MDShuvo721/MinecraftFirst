from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(pattern_name='home:home')),  # Redirect root URL to home page
    path('auth/', include('SignLog.urls')),
    path('world/', include('ToDoList.urls')),
    path('articles/', include('Article.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)