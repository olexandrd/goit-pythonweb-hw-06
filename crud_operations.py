from sqlalchemy import func
from sqlalchemy.orm.exc import UnmappedInstanceError
from db_models import Group, Teacher, Student, Subject, Mark
from logger_config import logger
from error_handler import SQLError


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
            date=func.now(),  # pylint: disable=not-callable
        )
        session.add(mark)
        session.commit()
        logger.info(
            f"Added mark: {mark} for student_id: {student_id} and subject_id: {subject_id}"
        )


def list_(session, **kwargs):
    """
    List all records
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
    """
    Update a record
    """
    model = kwargs.get("model")
    name = kwargs.get("name")
    mark = kwargs.get("mark")
    student_id = kwargs.get("student_id")
    subject_id = kwargs.get("subject_id")
    group_id = kwargs.get("group_id")
    teacher_id = kwargs.get("teacher_id")
    mark_id = kwargs.get("mark_id")
    try:
        if model == "Student":
            student = session.query(Student).filter_by(id=student_id).first()
            student.name = name
            student.group_id = group_id
            session.commit()
            logger.info(f"Updated student: {name}")
        elif model == "Teacher":
            teacher = session.query(Teacher).filter_by(id=teacher_id).first()
            teacher.name = name
            session.commit()
            logger.info(f"Updated teacher: {name}")
        elif model == "Group":
            group = session.query(Group).filter_by(id=group_id).first()
            group.name = name
            session.commit()
            logger.info(f"Updated group: {name}")
        elif model == "Subject":
            subject = session.query(Subject).filter_by(id=subject_id).first()
            subject.name = name
            subject.teacher_id = teacher_id
            session.commit()
            logger.info(f"Updated subject: {name}")
        elif model == "Mark":
            mark = session.query(Mark).filter_by(id=mark_id).first()
            mark.mark = mark
            mark.student_id = student_id
            mark.subject_id = subject_id
            session.commit()
            logger.info(f"Updated mark: {mark}")
    except (AttributeError, UnmappedInstanceError):
        logger.error("Record not found")
        session.rollback()


def remove(session, **kwargs):
    """
    Remove a record
    """
    model = kwargs.get("model")
    mark = kwargs.get("mark")
    student_id = kwargs.get("student_id")
    subject_id = kwargs.get("subject_id")
    group_id = kwargs.get("group_id")
    teacher_id = kwargs.get("teacher_id")
    mark_id = kwargs.get("mark_id")
    try:
        if model == "Student":
            student = session.query(Student).filter_by(id=student_id).first()
            session.delete(student)
            session.commit()
            logger.info(f"Deleted student: {student.name}")
        elif model == "Teacher":
            teacher = session.query(Teacher).filter_by(id=teacher_id).first()
            session.delete(teacher)
            session.commit()
            logger.info(f"Deleted teacher: {teacher.name}")
        elif model == "Group":
            group = session.query(Group).filter_by(id=group_id).first()
            session.delete(group)
            session.commit()
            logger.info(f"Deleted group: {group.name}")
        elif model == "Subject":
            subject = session.query(Subject).filter_by(id=subject_id).first()
            session.delete(subject)
            session.commit()
            logger.info(f"Deleted subject: {subject.name}")
        elif model == "Mark":
            mark = session.query(Mark).filter_by(id=mark_id).first()
            session.delete(mark)
            session.commit()
            logger.info(f"Deleted mark: {mark.mark}")
    except (AttributeError, UnmappedInstanceError):
        logger.error("Record not found")
        session.rollback()
