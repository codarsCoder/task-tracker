from django.urls import path, include
from rest_framework import routers

from .views import (
    todo_list_create,
    todo_home,
    todo_detail,
    Todos,
    TodoDetail,
    TodoMVS
)

router = routers.DefaultRouter()
# todo/ todo/path  todo/<int:pk>  todo/<int:pk>/path
router.register('todo', TodoMVS)

urlpatterns = [
    path('', todo_home),
    # path('list-create/', todo_list_create),
    # path('detail/<int:id>', todo_detail),
    path('list-create/', Todos.as_view()), ## burada id pk olarak alınıyor  yukarıda ise serbest id olarak almışız viewde de id olarak çekeriz
    path('detail/<int:pk>', TodoDetail.as_view()),  ##BURASI NORMAL CLASS VİEW İÇİN LAZIM AS_VİEW BURADA ŞART
    path('', include(router.urls)) ##BURASI İSE VİEWSET İÇİN LAZIM VİEWSET İÇİN ARTI OLARAK YUKARIDAKİ ROUTER KURULMALI
]

# urlpatterns += router.urls
