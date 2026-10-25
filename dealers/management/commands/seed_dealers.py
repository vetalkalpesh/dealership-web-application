from django.core.management.base import BaseCommand
from dealers.models import Dealer

SAMPLE = [
    ("Prairie Motors", "Wichita", "Kansas", "100 Main Street", "+1-316-555-0101"),
    ("Sunflower Auto Group", "Topeka", "Kansas", "200 State Street", "+1-785-555-0102"),
    ("Lone Star Cars", "Dallas", "Texas", "300 Market Road", "+1-214-555-0103"),
    ("Golden Gate Auto", "San Jose", "California", "400 Bay Avenue", "+1-408-555-0104"),
]
class Command(BaseCommand):
    help = "Add demo dealership records"
    def handle(self, *args, **options):
        for name, city, state, address, phone in SAMPLE:
            Dealer.objects.get_or_create(name=name, city=city, state=state,
                                         defaults={"address": address, "phone": phone})
        self.stdout.write(self.style.SUCCESS("Demo dealers seeded."))
