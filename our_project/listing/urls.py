from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.listings,name='listings'),
    path('<int:id>',views.listing_by_id,name='listing'),
    path('<title>',views.listing_by_title,name="listing_by_title")

    ]
