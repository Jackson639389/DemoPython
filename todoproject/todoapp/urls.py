from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:todo_id>/',views.delete,name='delete'),
    path('update/<int:do_id>/',views.update,name='update'),
    path('abvhome/',views.TodoList.as_view(),name='TodoList'),
    path('abvdetail/<int:pk>/',views.TodoDetail.as_view(),name='TodoDetail'),
    path('abvupdate/<int:pk>/',views.TodoUpdate.as_view(),name='TodoUpdate'),
    path('abvdelete/<int:pk>/',views.TodoDelete.as_view(),name='TodoDelete'),

]
