from django.urls import path, include

from .views import (BuyerDashboard,
                    BuyerSettings,
                    BuyerDelete,
                    BuyerPasswordChange,
                    BuyerRole,
                    BuyerLikeList)

urlpatterns = [
    path('account/user/', BuyerDashboard.as_view(),
         name='buyer_dashboard'),
    path('account/user/settings/', BuyerSettings.as_view(),
         name='buyer_settings'),
    path('account/user/delete/', BuyerDelete.as_view(), name='buyer_delete'),
    path('account/user/password/', BuyerPasswordChange.as_view(),
         name='buyer_change_password'),
    path('account/user/role/', BuyerRole.as_view(),
         name='buyer_role'),
    path('account/user/likes/', BuyerLikeList.as_view(),
         name='buyer_all_likes'),

]
