"""Proper OnDelete settings (3)

Revision ID: 399aa4e5a4df
Revises: 796398e8d291
Create Date: 2024-11-16 14:40:45.114715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '399aa4e5a4df'
down_revision: Union[str, None] = '796398e8d291'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
