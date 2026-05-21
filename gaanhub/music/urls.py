from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logged-out/', views.logged_out_page, name='logged_out'),
    path('switch-mode/', views.switch_mode, name='switch_mode'),

    path('songs/', views.song_list, name='songs'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),
    path('songs/<int:pk>/download/', views.download_song, name='download_song'),
    path('api/search/', views.search_songs, name='search_songs'),
    path('search/', views.global_search, name='global_search'),
    path('create/', views.create_song, name='create_song'),
    path('update/<int:pk>/', views.update_song, name='update_song'),
    path('delete/<int:pk>/', views.delete_song, name='delete_song'),
    path('like/<int:pk>/', views.like_song, name='like_song'),
    path('record-play/<int:pk>/', views.record_play, name='record_play'),

    path('songs/<int:song_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('playlists/', views.my_playlists, name='playlists'),
    path('playlists/<int:pk>/', views.playlist_detail, name='playlist_detail'),
    path('playlists/<int:pk>/delete/', views.delete_playlist, name='delete_playlist'),
    path('playlist/add/<int:song_id>/', views.add_to_playlist, name='add_to_playlist'),
    path('playlists/<int:playlist_id>/remove/<int:song_id>/', views.remove_from_playlist, name='remove_from_playlist'),

    path('history/', views.play_history, name='history'),
    path('queue/', views.get_queue, name='get_queue'),

    path('charts/', views.top_charts, name='charts'),
    path('genres/', views.browse_genres, name='genres'),
    path('genres/<int:genre_id>/', views.genre_songs, name='genre_songs'),

    path('artists/', views.all_artists, name='all_artists'),
    path('follow/<int:artist_id>/', views.follow_artist, name='follow_artist'),
    path('artist/<int:artist_id>/page/', views.artist_page, name='artist_page'),

    path('profile/', views.user_profile, name='my_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),

    path('notifications/', views.notifications, name='notifications'),
    path('notifications/count/', views.unread_notification_count, name='notif_count'),

    path('artist/', views.artist_panel, name='artist_panel'),
    path('become-artist/', views.become_artist, name='become_artist'),

    path('buy/<int:pk>/', views.buy_song, name='buy_song'),
    path('payment/success/<int:purchase_id>/', views.payment_success, name='payment_success'),
    path('payment/fail/', views.payment_fail, name='payment_fail'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),

    path('subscription/', views.subscription_plans, name='subscription_plans'),
    path('subscription/subscribe/<str:plan>/', views.subscribe, name='subscribe'),
    path('subscription/success/<int:subscription_id>/', views.subscription_success, name='subscription_success'),
    path('subscription/fail/', views.subscription_fail, name='subscription_fail'),
    path('subscription/cancel/', views.subscription_cancel_payment, name='subscription_cancel_payment'),
    path('subscription/dashboard/', views.subscription_dashboard, name='subscription_dashboard'),
    path('subscription/cancel-plan/', views.cancel_subscription, name='cancel_subscription'),

    path('wallet/', views.wallet_dashboard, name='wallet_dashboard'),
    path('wallet/withdraw/', views.request_withdrawal, name='request_withdrawal'),

    path('pay/<str:purpose>/<int:ref_id>/', views.payment_gateway_select, name='payment_gateway_select'),
    path('pay/<str:purpose>/<int:ref_id>/submit/', views.payment_manual_submit, name='payment_manual_submit'),
]
