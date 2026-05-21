# Generated for GaanHub — Django 4.x/5.x compatible migration
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('bio', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='artists/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='albums/')),
                ('released_at', models.DateField(blank=True, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('audio_file', models.FileField(upload_to='songs/')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('is_premium', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('play_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='music.album')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='music.artist')),
                ('genres', models.ManyToManyField(blank=True, to='music.genre')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_songs', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_default', models.BooleanField(default=False)),
                ('songs', models.ManyToManyField(blank=True, to='music.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('status', models.CharField(choices=[('pending','Pending'),('completed','Completed'),('failed','Failed')], default='pending', max_length=20)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='music.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL)),
            ],
            options={'unique_together': {('user', 'song')}},
        ),
        migrations.CreateModel(
            name='PlayHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_at', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_entries', to='music.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='play_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-played_at']},
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='music.artist')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
            options={'unique_together': {('follower', 'artist')}},
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('link', models.CharField(blank=True, max_length=300)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='SongComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='music.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=300)),
                ('avatar_color', models.CharField(default='#1DB954', max_length=7)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PremiumSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('individual','Individual'),('student','Student'),('family','Family')], max_length=20)),
                ('status', models.CharField(choices=[('active','Active'),('expired','Expired'),('cancelled','Cancelled')], default='active', max_length=20)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
                ('transaction_id', models.CharField(blank=True, max_length=200)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('auto_renew', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-started_at']},
        ),
        migrations.CreateModel(
            name='ArtistWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_earned', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_withdrawn', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('credit','Credit'),('debit','Debit')], max_length=10)),
                ('source', models.CharField(choices=[('stream','Stream Royalty'),('sale','Song Sale'),('withdrawal','Withdrawal'),('bonus','Bonus')], default='stream', max_length=20)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='music.artistwallet')),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='WithdrawalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('method', models.CharField(choices=[('bkash','bKash'),('nagad','Nagad'),('rocket','Rocket'),('bank','Bank Transfer')], max_length=20)),
                ('status', models.CharField(choices=[('pending','Pending'),('processing','Processing'),('completed','Completed'),('rejected','Rejected')], default='pending', max_length=20)),
                ('mobile_number', models.CharField(blank=True, max_length=15)),
                ('account_name', models.CharField(blank=True, max_length=100)),
                ('bank_name', models.CharField(blank=True, max_length=100)),
                ('branch_name', models.CharField(blank=True, max_length=100)),
                ('account_number', models.CharField(blank=True, max_length=50)),
                ('routing_number', models.CharField(blank=True, max_length=50)),
                ('note', models.TextField(blank=True)),
                ('admin_note', models.TextField(blank=True)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('processed_at', models.DateTimeField(blank=True, null=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals', to='music.artistwallet')),
            ],
            options={'ordering': ['-requested_at']},
        ),
        migrations.CreateModel(
            name='PaymentLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gateway', models.CharField(choices=[('bkash','bKash'),('nagad','Nagad'),('rocket','Rocket'),('bank','Bank Transfer'),('sslcommerz','SSLCommerz')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=200, unique=True)),
                ('purpose', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('raw_response', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
