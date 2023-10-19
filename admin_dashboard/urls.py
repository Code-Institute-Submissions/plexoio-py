# Django Imports

from django.urls import path, include

# Local Imports
from .views import (AdminDashboard, AdminSettingsView,
                    AdminPasswordChange, AdminRole, AdminDownloadCreation,
                    DownloadWithToken,
                    DownloadList, AdminUpdateDownloadView, DownloadDelete,
                    PendingOrderDeletionView, CommentList,
                    AdminUpdateCommentView, CommentDelete,
                    LikeList, AdminUpdateLikeView, LikeDelete,)


urlpatterns = [
    # Dashboard
    path('account/admin/', AdminDashboard.as_view(),
         name='admin_dashboard'),

    # Settings
    path('account/admin/settings/', AdminSettingsView.as_view(),
         name='admin_settings'),
    path('account/admin/password/', AdminPasswordChange.as_view(),
         name='admin_change_password'),
    path('account/admin/role/', AdminRole.as_view(),
         name='admin_role'),

    # Download
    path('account/admin/download/create/', AdminDownloadCreation.as_view(),
         name='admin_download_create'),
    path('account/admin/download/all/', DownloadList.as_view(),
         name='admin_all_downloads'),
    path('account/admin/download/file/<int:item_id>/',
         AdminUpdateDownloadView.as_view(),
         name='admin_update_download'),
    path('account/admin/download/file/delete/<int:item_id>/',
         DownloadDelete.as_view(), name='admin_delete_download'),
    path('media/downloads/<str:download_token>/', DownloadWithToken.as_view(),
         name='download_with_token'),

    # Orders Delete
    path('account/admin/orders/delete/', PendingOrderDeletionView.as_view(),
         name='orders_delete'),

    # Comments
    path('account/admin/comments/', CommentList.as_view(),
         name='admin_all_comments'),
    path('account/admin/comments/<int:comment_id>/',
         AdminUpdateCommentView.as_view(),
         name='admin_update_comment'),
    path('account/admin/comments/delete/<int:comment_id>/',
         CommentDelete.as_view(), name='comment_delete'),

    # Likes
    path('account/admin/likes/', LikeList.as_view(),
         name='admin_all_likes'),
    path('account/admin/likes/<int:like_id>/',
         AdminUpdateLikeView.as_view(),
         name='admin_update_like'),
    path('account/admin/likes/delete/<int:like_id>/',
         LikeDelete.as_view(), name='like_delete'),
]
