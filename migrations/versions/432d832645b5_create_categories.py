"""create categories

Revision ID: 432d832645b5
Revises: 
Create Date: 2024-05-07 19:06:40.060669

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '432d832645b5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("categories")
    op.add_column("categories", sa.Column("index", sa.Integer(), primary_key=True))
    op.add_column("categories", sa.Column("name", sa.String(), nullable=False))
    op.add_column("categories", sa.Column("type", sa.String(), nullable=False))
    op.add_column("categories", sa.Column("route", sa.String(), nullable=False))


def downgrade() -> None:
    pass
