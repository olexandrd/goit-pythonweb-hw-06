"""
Print data queries
"""

import logging
from sqlalchemy import func, select, desc
from db_models import Group, Teacher, Student, Subject, Mark
from connect import Session, session

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)


def log_seperator() -> None:
    """
    Print a log seperator
    """
    logging.info("#" * 80)


def select_1(session: Session) -> None:
    """
    Query 1: 5 students with the highest average mark
    """

    log_seperator()
    logging.info("Query 1: 5 students with the highest average mark")
    top_students_query = (
        select(
            Student.id,
            Student.name,
            Student.surname,
            func.avg(Mark.mark).label("average_mark"),
        )
        .join(Mark, Student.id == Mark.student_id)
        .group_by(Student.id, Student.name, Student.surname)
        .order_by(func.avg(Mark.mark).desc())
        .limit(5)
    )
    top_students = session.execute(top_students_query).all()
    for student in top_students:
        logging.info(
            "{:<15} {:<15} | {:.2f} |".format(
                student.name, student.surname, student.average_mark
            )
        )


def select_2(session: Session) -> None:
    """
    Query 2: students with the highest average for each subject
    """

    log_seperator()
    logging.info("Query 2: students with the highest average mark for each subject")
    subquery = (
        select(
            Mark.subject_id,
            Student.id.label("student_id"),
            func.avg(Mark.mark).label("average_mark"),
        )
        .join(Student, Student.id == Mark.student_id)
        .group_by(Mark.subject_id, Student.id)
        .subquery()
    )

    top_students_query = (
        select(
            Subject.id,
            Subject.name.label("subject_name"),
            subquery.c.student_id,
            Student.name.label("student_name"),
            Student.surname.label("student_surname"),
            subquery.c.average_mark,
        )
        .join(subquery, subquery.c.subject_id == Subject.id)
        .join(Student, Student.id == subquery.c.student_id)
        .order_by(subquery.c.subject_id, desc(subquery.c.average_mark))
        .distinct(subquery.c.subject_id)
    )
    top_students = session.execute(top_students_query).all()
    for student in top_students:
        logging.info(
            "{:<15} {:<15} | {:.2f} | {:<12} |".format(
                student.student_name,
                student.student_surname,
                student.average_mark,
                student.subject_name,
            )
        )


def select_3(session: Session) -> None:
    """
    Found average mark on groups for each subject
    """

    log_seperator()
    logging.info("Query 3: Found average mark on groups for each subject")
    average_marks_query = (
        select(
            Group.name.label("group_name"),
            Subject.name.label("subject_name"),
            func.avg(Mark.mark).label("average_mark"),
        )
        .join(Student, Student.group_id == Group.id)
        .join(Mark, Mark.student_id == Student.id)
        .join(Subject, Subject.id == Mark.subject_id)
        .group_by(Group.name, Subject.name)
    )

    average_mark = session.execute(average_marks_query).all()
    for mark in average_mark:
        logging.info(
            "{:<15} {:<15} | {:.2f} |".format(
                mark.group_name, mark.subject_name, mark.average_mark
            )
        )


def select_4(session: Session) -> None:
    """
    Avarege mark for all students
    """

    log_seperator()
    logging.info("Query 4: Avarege mark")
    average_marks_query = select(func.avg(Mark.mark).label("average_mark"))

    average_mark = session.execute(average_marks_query).all()
    for mark in average_mark:
        logging.info("Avarege mark: {:.2f}".format(mark.average_mark))


def select_5(session: Session) -> None:
    """
    Each teachers subjects
    """

    log_seperator()
    logging.info("Query 5: Each teachers subjects")
    teachers_query = (
        select(
            Teacher.name.label("teacher_name"),
            Teacher.surname.label("teacher_surname"),
            Subject.name.label("subject_name"),
        )
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .group_by(Teacher.name, Teacher.surname, Subject.name)
    )

    teachers = session.execute(teachers_query).all()
    for teacher in teachers:
        logging.info(
            "{:<15} {:<15} | {:<15} |".format(
                teacher.teacher_name, teacher.teacher_surname, teacher.subject_name
            )
        )


def select_6(session: Session, group_id: int) -> None:
    """
    List students from given group
    """

    log_seperator()
    logging.info("Query 6: List students from given group")
    students_query = select(
        Student.name.label("student_name"),
        Student.surname.label("student_surname"),
    ).filter(Student.group_id == group_id)

    students = session.execute(students_query).all()
    logging.info("Group id: %s", group_id)
    for student in students:
        logging.info(
            "{:<15} {:<15}".format(student.student_name, student.student_surname)
        )


def select_7(session: Session, group_id: int, subject: str) -> None:
    """
    List students marks from given group and subject
    """

    log_seperator()
    logging.info("Query 7: List students marks from given group and subject")
    students_query = (
        (
            select(
                Student.name.label("student_name"),
                Student.surname.label("student_surname"),
                Subject.name.label("subject_name"),
                Mark.mark.label("mark"),
            )
            .filter(Student.group_id == group_id)
            .filter(Subject.name.like(subject))
        )
        .join(Mark, Mark.student_id == Student.id)
        .join(Subject, Mark.subject_id == Subject.id)
    )

    students = session.execute(students_query).all()
    logging.info("Group id: %s", group_id)
    logging.info("Subject: %s", subject)
    for student in students:
        logging.info(
            "{:<15} {:<15} | {:<15} | {:<15}".format(
                student.student_name,
                student.student_surname,
                student.subject_name,
                student.mark,
            )
        )


def select_8(session: Session) -> None:
    """
    Average mark by each teacher
    """

    log_seperator()
    logging.info("Query 8: Average mark by each teacher")
    select_query = (
        select(
            Teacher.name.label("teacher_name"),
            Teacher.surname.label("teacher_surname"),
            func.avg(Mark.mark).label("average_mark"),
        )
        .join(Subject, Subject.teacher_id == Teacher.id)
        .join(Mark, Mark.subject_id == Subject.id)
        .group_by(Teacher.name, Teacher.surname)
    )

    teachers = session.execute(select_query).all()
    for teacher in teachers:
        logging.info(
            "{:<15} {:<15} | {:.2f} |".format(
                teacher.teacher_name, teacher.teacher_surname, teacher.average_mark
            )
        )


def select_9(session: Session, student_id: int) -> None:
    """
    Given student subject list
    """
    logging.info("Query 9: Given student subject list")

    log_seperator()
    select_query = (
        select(
            Student.name.label("student_name"),
            Student.surname.label("student_surname"),
            Subject.name.label("subject_name"),
        )
        .join(Mark, Mark.student_id == Student.id)
        .join(Subject, Subject.id == Mark.subject_id)
        .filter(Student.id == student_id)
    )

    students = session.execute(select_query).all()
    for student in students:
        logging.info(
            "{:<15} {:<15} | {:<15}".format(
                student.student_name, student.student_surname, student.subject_name
            )
        )


def select_10(session: Session, student_id: int, teacher_id: int) -> None:
    """
    Given student subject list by teacher
    """
    logging.info("Query 10: Given student subject list by teacher")

    log_seperator()
    select_query = (
        select(
            Student.name.label("student_name"),
            Student.surname.label("student_surname"),
            Subject.name.label("subject_name"),
            Teacher.name.label("teacher_name"),
            Teacher.surname.label("teacher_surname"),
        )
        .join(Mark, Mark.student_id == Student.id)
        .join(Subject, Subject.id == Mark.subject_id)
        .filter(Student.id == student_id)
        .filter(Subject.teacher_id == teacher_id)
    )

    list = session.execute(select_query).all()
    for i in list:
        logging.info(
            "Subject: {:<10} | Student: {:<15} {} | Teacher: {:<15} {:<15}".format(
                i.subject_name,
                i.student_name,
                i.student_surname,
                i.teacher_name,
                i.teacher_surname,
            )
        )


def main() -> None:
    """
    Run all queries
    """

    select_1(session=session)
    select_2(session=session)
    select_3(session=session)
    select_4(session=session)
    select_5(session=session)
    select_6(group_id=2, session=session)
    select_7(group_id=1, subject="Biology", session=session)
    select_8(session=session)
    select_9(student_id=2, session=session)
    select_10(student_id=1, teacher_id=1, session=session)


if __name__ == "__main__":
    main()
