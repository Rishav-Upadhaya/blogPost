from django.urls import path
from . import views

urlpatterns = [
    path("",views.bloghome, name="bloghome"),
    path("post/<str:t>",views.post, name="post"),
    path("author/<str:writer>",views.author, name="author"),
    path("create",views.createpost, name="create"),
    path("delete",views.delete_user, name="delete"),
    path("comment",views.comment, name="comment"),
]
