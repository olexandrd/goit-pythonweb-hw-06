"""
Database models
"""

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    DateTime,
    func,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    """
    Base ORM class
    """

    __abstract__ = True


class Student(Base):
    """
    Student table
    """

    __tablename__ = "student"
    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = mapped_column(String, nullable=False)
    group_id = mapped_column(
        Integer, ForeignKey("group.id", ondelete="CASCADE"), nullable=False
    )
    group = relationship("Group", back_populates="student")
    mark = relationship("Mark", back_populates="student")


class Group(Base):
    """
    Group table
    """

    __tablename__ = "group"
    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = mapped_column(String, nullable=False)
    student = relationship("Student", back_populates="group")


class Teacher(Base):
    """
    Teacher table
    """

    __tablename__ = "teacher"
    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = mapped_column(String, nullable=False)
    subject = relationship("Subject", back_populates="teacher")


class Subject(Base):
    """
    Subject table
    """

    __tablename__ = "subject"
    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = mapped_column(String, nullable=False)
    teacher_id = mapped_column(
        Integer, ForeignKey("teacher.id", ondelete="CASCADE"), nullable=False
    )
    teacher = relationship("Teacher", back_populates="subject")
    mark = relationship("Mark", back_populates="subject")


class Mark(Base):
    """
    Marks table
    """

    __tablename__ = "mark"
    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    student_id = mapped_column(
        Integer, ForeignKey("student.id", ondelete="CASCADE"), nullable=False
    )
    subject_id = mapped_column(
        Integer, ForeignKey("subject.id", ondelete="CASCADE"), nullable=False
    )
    mark = mapped_column(Integer, nullable=False)
    student = relationship("Student", back_populates="mark")
    subject = relationship("Subject", back_populates="mark")
    date = mapped_column(DateTime, default=func.now, nullable=False)
