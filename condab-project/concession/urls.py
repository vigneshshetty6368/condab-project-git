from django.urls import path
from . import views

#app_name='concession'
urlpatterns = [
    path('', views.index,name='index'),
    path('help/', views.help),
    path('create/', views.createcon,name='createcon'),
    path('<int:nmn>/detail', views.detail,name='detail'),
    path('<int:nmn>/update', views.update,name='update'),
    path('<int:nmn>/delete', views.delete,name='delete'),
    path('<int:nmn>/item/create', views.createitem,name='createitem'),
    path('item/<int:nmn>/detail', views.detailitem,name='detailitem'),
    path('item/<int:nmn>/update', views.updateitem,name='updateitem'),
    path('item/<int:nmn>/delete', views.deleteitem,name='deleteitem'),
    path('database', views.database, name='database'),
    path('about', views.about, name='about'),
    # path('condab', views.condab, name='condab'),
    #path('<int:nmn>/item/<int:avn>', views.createitem,name='createitem'),
    #path('<int:nmn>//', views.saveas,name='saveas'),
    #path('formview/', views.form_view),
    ]
