from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celular',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='celular',
            name='fechaPublicacion',
        ),
    ]
