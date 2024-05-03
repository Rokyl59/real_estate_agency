from django.db import migrations
import phonenumbers

def correct_phone_number(phone):
    if phone.startswith('8'):
        phone = '+7' + phone[1:]
    return phone

def link_owners_to_flats(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        phone_number = correct_phone_number(flat.owners_phonenumber)
        try:
            parsed_phone = phonenumbers.parse(phone_number, 'RU')
            normalized_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164) if phonenumbers.is_valid_number(parsed_phone) else None
        except phonenumbers.NumberParseException:
            normalized_phone = None

        owner, created = Owner.objects.get_or_create(
            name=flat.owner,
            defaults={'phonenumber': normalized_phone}
        )
        owner.flats.add(flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20240503_2255'),
    ]

    operations = [
        migrations.RunPython(link_owners_to_flats),
    ]
