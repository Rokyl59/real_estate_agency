from django.db import migrations
import phonenumbers


def create_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        phone_number = flat.owners_phonenumber
        normalized_phone = None
        if phone_number:
            try:
                parsed_phone = phonenumbers.parse(phone_number, 'RU')
                if phonenumbers.is_valid_number(parsed_phone):
                    normalized_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
            except phonenumbers.NumberParseException:
                pass
        owner, created = Owner.objects.get_or_create(
            name=flat.owner,
            defaults={'phonenumber': phone_number, 'owner_pure_phone': normalized_phone}
        )
        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(create_owners),
    ]
