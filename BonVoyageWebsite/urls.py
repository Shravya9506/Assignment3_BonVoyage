from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('', include(('bonvoyage.urls','bonvoyage'),namespace='bonvoyage')),
    path('', include(('vacations.urls', 'vacations'), namespace='vacations')),
    path('account/', include('django.contrib.auth.urls')),

]

admin.site.site_header = 'Bon voyage Administration' # default: "Django Administration"
admin.site.index_title = 'Bon voyage Site Administration'        # default: "Site administration"
admin.site.site_title = 'Bon voyage site admin'                  # default: "Django site admin"

