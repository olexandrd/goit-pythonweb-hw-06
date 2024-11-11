"""
Fixtures for seeding the database with data.
"""

from faker import Faker
from faker.providers import DynamicProvider
from connect import session
from db_models import Group, Teacher, Student, Subject, Mark

subjects_provider = DynamicProvider(
    provider_name="subjects",
    elements=["Math", "Physics", "Chemistry", "Biology", "History", "Geography"],
)

fake = Faker()

fake.add_provider(subjects_provider)


def seed():
    """
    Seed the database with data
    """

    for _ in range(3):
        group = Group(name=fake.word())
        session.add(group)
        session.commit()

        teacher = Teacher(name=fake.first_name(), surname=fake.last_name())
        session.add(teacher)
        session.commit()

        for _ in range(2):
            subject = Subject(name=fake.subjects(), teacher_id=teacher.id)
            session.add(subject)
            session.commit()

        for _ in range(10):
            student = Student(
                name=fake.first_name(),
                surname=fake.last_name(),
                group_id=group.id,
            )
            session.add(student)
            session.commit()

            mark = Mark(
                student_id=student.id,
                subject_id=subject.id,
                mark=fake.random_int(min=1, max=12),
                date=fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            )
            session.add(mark)
            session.commit()


if __name__ == "__main__":
    seed()
    print("Database seeded successfully")
