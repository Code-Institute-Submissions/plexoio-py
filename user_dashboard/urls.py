from django.urls import path, include

from .views import (BuyerDashboard,
                    BuyerSettings,
                    BuyerDelete,
                    BuyerPasswordChange,
                    BuyerRole,
                    BuyerLikeList,
                    BuyerCommentList)

urlpatterns = [
    # User Dashboard
    path('account/user/', BuyerDashboard.as_view(),
         name='buyer_dashboard'),

    # User Settings
    path('account/user/settings/', BuyerSettings.as_view(),
         name='buyer_settings'),
    path('account/user/delete/', BuyerDelete.as_view(), name='buyer_delete'),
    path('account/user/password/', BuyerPasswordChange.as_view(),
         name='buyer_change_password'),

    # User Role
    path('account/user/role/', BuyerRole.as_view(),
         name='buyer_role'),

    #  User Likes
    path('account/user/likes/', BuyerLikeList.as_view(),
         name='buyer_all_likes'),

    # User Comments
    path('account/user/comments/', BuyerCommentList.as_view(),
         name='buyer_all_comments'),
]
