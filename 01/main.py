"""
Main entry point for the application
"""

import subprocess
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


def main():
    run_migrations()
    generate_fixtures()
    selects()


if __name__ == "__main__":
    main()
