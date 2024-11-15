"""
Main entry point for the application
"""

import sys
import subprocess
import argparse
from logger_config import logger
from db_models import Student
from seed import seed
from connect import Session
from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)
from crud_operations import create, list_, update, remove


def validate_args(arguments):
    """
    Check if model is specified when action is specified
    """
    if arguments.action and not arguments.model:
        parser.error("When using --action (-a), you must also specify --model (-m).")


parser = argparse.ArgumentParser(description="CRUD operations for models.")

parser.add_argument(
    "-a",
    "--action",
    choices=["create", "list", "update", "remove"],
    help="Specify the CRUD action to perform (create, list, update, remove).",
)
parser.add_argument(
    "-m",
    "--model",
    choices=["Teacher", "Student", "Subject", "Group", "Mark"],
    help="Specify the model to perform the action on.",
)
parser.add_argument("--id", type=int, help="Specify the ID of the record.")
parser.add_argument("--group-id", type=int, help="Specify the group ID.")
parser.add_argument("--student-id", type=int, help="Specify the student ID.")
parser.add_argument("--subject-id", type=int, help="Specify the subject ID.")
parser.add_argument("--teacher-id", type=int, help="Specify the teacher ID.")
parser.add_argument(
    "--name", type=str, help="Specify the name for create or update operations."
)
parser.add_argument("--mark", type=int, help="Specify the mark.")
parser.add_argument("--fixtures", help="Generate fixtures", action="store_true")
parser.add_argument("--no-migrate", help="Do not run migrations", action="store_true")
parser.add_argument("--queries", help="Run predefined queries", action="store_true")
args = parser.parse_args()
validate_args(args)


def run_migrations():
    """
    Execute database migrations
    """

    result = subprocess.run(
        ["alembic", "upgrade", "head"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    if result.returncode == 0:
        logger.info("Migrations applied successfully")
    else:
        logger.error("Migration failed: %s", result.stderr.decode())


def generate_fixtures():
    """
    Check if database is seeded
    """
    with Session() as s:
        if not s.query(Student).first():
            seed()
            logger.info("Database seeded")
        else:
            logger.info("Database already seeded")


def selects():
    """
    Execute all select queries
    """
    with Session() as s:
        select_1(s)
        select_2(s)
        select_3(s)
        select_4(s)
        select_5(s)
        select_6(s, 2)
        select_7(s, 1, "Biology")
        select_8(s)
        select_9(s, 2)
        select_10(s, 1, 1)


def crud():
    """
    Execute CRUD operations
    """
    with Session() as s:
        if args.action == "create":
            create(
                s,
                model=args.model,
                name=args.name,
                mark=args.mark,
                student_id=args.student_id,
                subject_id=args.subject_id,
                group_id=args.group_id,
                teacher_id=args.teacher_id,
            )
        elif args.action == "list":
            list_(
                s,
                model=args.model,
                name=args.name,
                mark=args.mark,
                student_id=args.student_id,
                subject_id=args.subject_id,
                group_id=args.group_id,
                teacher_id=args.teacher_id,
            )
        elif args.action == "update":
            update(s)
        elif args.action == "remove":
            remove(s)


def main():
    """
    Main entry point logic
    """
    if not args.no_migrate:
        run_migrations()
    if args.fixtures:
        generate_fixtures()
    if args.queries:
        selects()
    if args.action:
        crud()


if __name__ == "__main__":
    main()
