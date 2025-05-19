from django.db import migrations

def load_initial_data(apps, schema_editor):
    Status = apps.get_model('dds', 'Status')
    Type = apps.get_model('dds', 'Type')
    Category = apps.get_model('dds', 'Category')
    Subcategory = apps.get_model('dds', 'Subcategory')

    # Статусы
    for name in ["Бизнес", "Личное", "Налог"]:
        Status.objects.get_or_create(name=name)

    # Типы
    type_income, _ = Type.objects.get_or_create(name="Пополнение")
    type_expense, _ = Type.objects.get_or_create(name="Списание")

    # Категории и подкатегории
    cat1, _ = Category.objects.get_or_create(name="Инфраструктура", type=type_expense)
    Subcategory.objects.get_or_create(name="VPS", category=cat1)
    Subcategory.objects.get_or_create(name="Proxy", category=cat1)

    cat2, _ = Category.objects.get_or_create(name="Маркетинг", type=type_expense)
    Subcategory.objects.get_or_create(name="Farpost", category=cat2)
    Subcategory.objects.get_or_create(name="Avito", category=cat2)

class Migration(migrations.Migration):

    dependencies = [
        ("dds", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
