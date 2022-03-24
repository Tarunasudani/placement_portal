

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0002_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='applied_to',
            field=models.ManyToManyField(blank=True, null=True, to='placement.company'),
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='application',
            name='applied_in',
        ),
        migrations.RemoveField(
            model_name='application',
            name='status',
        ),
    ]
