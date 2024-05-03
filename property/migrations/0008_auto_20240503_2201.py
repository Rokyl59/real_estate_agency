from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_number = flat.owners_phonenumber
        try:
            parsed_phone = phonenumbers.parse(phone_number, 'RU')
            if phonenumbers.is_valid_number(parsed_phone):
                formatted_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
                flat.owner_pure_phone = formatted_phone
                flat.save(update_fields=['owner_pure_phone'])
        except phonenumbers.NumberParseException:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
