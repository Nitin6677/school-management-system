from django.core.management.base import BaseCommand
from faker import Faker
from api.models import StudentInfo
import random

fake = Faker()

class Command(BaseCommand):
    help = "Insert 1 million student records"

    def handle(self, *args, **kwargs):
        students = []
        batch_size = 10_000  # IMPORTANT for memory

        for i in range(1_000_000):
            students.append(
                StudentInfo(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    date_of_birth=fake.date_of_birth(minimum_age=5, maximum_age=18),
                    city_name=fake.city(),
                    roll_number=100 + i,
                    school_name=fake.company() + " School",
                    class_name=random.choice(
                        ["1st", "2nd", "3rd", "4th", "5th",
                         "6th", "7th", "8th", "9th", "10th"]
                    ),
                    email=fake.email(),
                    phone_number=fake.phone_number(),
                    address=fake.address(),
                    year_in_school=random.choice(
                        ["2020", "2021", "2022", "2023", "2024"]
                    ),
                )
            )

            if len(students) == batch_size:
                StudentInfo.objects.bulk_create(students)
                students.clear()
                self.stdout.write(f"Inserted {i + 1} records")

        # Insert remaining records
        if students:
            StudentInfo.objects.bulk_create(students)

        self.stdout.write(self.style.SUCCESS("✅ 1 Million Student Records Inserted"))
