from django.contrib import admin
from .models import (
    Artist, Album, Genre, Song, Playlist, Purchase,
    PlayHistory, Follow, Notification, SongComment, UserProfile,
    PremiumSubscription, ArtistWallet, WalletTransaction,
    WithdrawalRequest, PaymentLog,
)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'is_premium', 'price', 'play_count', 'created_at')
    list_filter = ('is_premium', 'genres', 'created_at')
    search_fields = ('title', 'artist__name')
    list_editable = ('is_premium', 'price')


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'follower_count')
    search_fields = ('name', 'user__username')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'amount', 'status', 'transaction_id', 'paid_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'song__title', 'transaction_id')


@admin.register(PremiumSubscription)
class PremiumSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'amount_paid', 'expires_at', 'auto_renew')
    list_filter = ('plan', 'status')
    search_fields = ('user__username',)


@admin.register(ArtistWallet)
class ArtistWalletAdmin(admin.ModelAdmin):
    list_display = ('artist', 'balance', 'total_earned', 'total_withdrawn', 'last_updated')
    search_fields = ('artist__name',)


@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'transaction_type', 'source', 'amount', 'description', 'created_at')
    list_filter = ('transaction_type', 'source')


@admin.register(WithdrawalRequest)
class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'amount', 'method', 'status', 'requested_at')
    list_filter = ('method', 'status')
    list_editable = ('status',)


@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'gateway', 'amount', 'purpose', 'status', 'created_at')
    list_filter = ('gateway', 'status', 'purpose')


admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(PlayHistory)
admin.site.register(Follow)
admin.site.register(Notification)
admin.site.register(SongComment)
admin.site.register(UserProfile)
