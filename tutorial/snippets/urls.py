from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
# from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# api/
OBJECT_URI_PREFIX= 'snippets'
USER_URI_PREFIX= 'users'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/snippets', views.SnippetViewSet)
router.register(r'api/users', views.UserViewSet)

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#   path(APP_NAME+'/', views.snippet_list),
#   path(APP_NAME+'<int:pk>/', views.snippet_detail),
# ]

urlpatterns = [
    # path('', views.api_root),
    # path(OBJECT_URI_PREFIX+'/', views.SnippetList.as_view(), name='snippet-list'),
    # path(OBJECT_URI_PREFIX+'/<int:pk>', views.SnippetDetail.as_view(), name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    # path(USER_URI_PREFIX+'/', views.UserList.as_view(), name='user-list'),
    # path(USER_URI_PREFIX+'/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # path('', api_root),
    # path(OBJECT_URI_PREFIX+'/', snippet_list, name='snippet-list'),
    # path(OBJECT_URI_PREFIX+'/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path(OBJECT_URI_PREFIX+'/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path(USER_URI_PREFIX+'/', user_list, name='user-list'),
    # path(USER_URI_PREFIX+'/<int:pk>/', user_detail, name='user-detail')

    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
