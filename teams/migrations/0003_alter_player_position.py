# Generated by Django 5.1.4 on 2024-12-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_player_is_selected_player_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('Goalkeeper', 'Goalkeeper'), ('Attacker', 'Attacker'), ('Defender', 'Defender'), ('Player', 'Player')], default='Player', max_length=50),
        ),
    ]