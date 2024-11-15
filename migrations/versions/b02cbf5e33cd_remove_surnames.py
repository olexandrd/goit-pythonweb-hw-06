"""Remove surnames

Revision ID: b02cbf5e33cd
Revises: 1d969bc98546
Create Date: 2024-11-15 22:56:53.740270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b02cbf5e33cd'
down_revision: Union[str, None] = '1d969bc98546'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'surname')
    op.drop_column('teacher', 'surname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('student', sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
