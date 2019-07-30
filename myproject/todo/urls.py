from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addTodo,name='add'),
    path('done/<todo_id>',views.addDone,name='done'),
    path('delDone',views.delDone,name='delDone'),
    path('delAll',views.delAll,name='delAll'),
]
