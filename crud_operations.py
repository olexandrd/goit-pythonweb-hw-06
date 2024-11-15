from sqlalchemy import func, select, desc
from db_models import Group, Teacher, Student, Subject, Mark
from logger_config import logger


def create(session, **kwargs):
    """
    Create a new record
    """
    model = kwargs.get("model")
    name = kwargs.get("name")
    mark = kwargs.get("mark")
    student_id = kwargs.get("student_id")
    subject_id = kwargs.get("subject_id")
    group_id = kwargs.get("group_id")
    teacher_id = kwargs.get("teacher_id")
    if model == "Student":
        student = Student(name=name, group_id=group_id)
        session.add(student)
        session.commit()
        logger.info(f"Added student: {name} to group_id: {group_id}")
    elif model == "Teacher":
        teacher = Teacher(name=name)
        session.add(teacher)
        session.commit()
        logger.info(f"Added teacher: {name}")
    elif model == "Group":
        group = Group(name=name)
        session.add(group)
        session.commit()
        logger.info(f"Added group: {name}")
    elif model == "Subject":
        subject = Subject(name=name, teacher_id=teacher_id)
        session.add(subject)
        session.commit()
        logger.info(f"Added subject: {name}")
    elif model == "Mark":
        mark = Mark(
            mark=mark,
            student_id=student_id,
            subject_id=subject_id,
            date=func.now(),
        )
        session.add(mark)
        session.commit()
        logger.info(
            f"Added mark: {mark} for student_id: {student_id} and subject_id: {subject_id}"
        )


def list_(session, **kwargs):
    """
    List records
    """
    model = kwargs.get("model")
    if model == "Student":
        students = session.query(Student).all()
        for student in students:
            logger.info("Student id: {:<5} {}".format(student.id, student.name))
    elif model == "Teacher":
        teachers = session.query(Teacher).all()
        for teacher in teachers:
            logger.info("Teacher id: {:<5} {}".format(teacher.id, teacher.name))
    elif model == "Group":
        groups = session.query(Group).all()
        for group in groups:
            logger.info("Group id: {:<5} {}".format(group.id, group.name))
    elif model == "Subject":
        subjects = session.query(Subject).join(Teacher).all()
        for subject in subjects:
            logger.info(
                "Subject id: {:<5} {:<12} teacher_id: {:<5} {}".format(
                    subject.id, subject.name, subject.teacher_id, subject.teacher.name
                )
            )
    elif model == "Mark":
        marks = session.query(Mark).join(Student).join(Subject).all()
        for mark in marks:
            logger.info(
                "Mark id: {:<5} student: {:<19} subject: {:<12} mark: {:<5} date: {}".format(
                    mark.id, mark.student.name, mark.subject.name, mark.mark, mark.date
                )
            )


def update(session, **kwargs):
    pass


def remove(session, **kwargs):
    pass
