from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('serie', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('memoria', models.CharField(max_length=20)),
                ('pantalla', models.DecimalField(decimal_places=1, max_digits=2)),
                ('camara', models.DecimalField(decimal_places=1, max_digits=3)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
