import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dds', '0002_auto_20250518_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dds.category'),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dds.subcategory'),
        ),
    ]
