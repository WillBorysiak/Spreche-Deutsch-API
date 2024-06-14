"""create words

Revision ID: c3e77c7f8487
Revises: 432d832645b5
Create Date: 2024-05-15 09:31:38.379455

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c3e77c7f8487'
down_revision: Union[str, None] = '432d832645b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("words")
    op.add_column("words", sa.Column("index", sa.Integer(), primary_key=True))
    op.add_column("words", sa.Column("german", sa.String(), nullable=False))
    op.add_column("words", sa.Column("english", sa.String(), nullable=False))
    op.add_column("words", sa.Column("category", sa.String(), nullable=False))
    op.add_column("words", sa.Column("gender", sa.String(), nullable=False))


def downgrade():
    op.drop_table("words")
