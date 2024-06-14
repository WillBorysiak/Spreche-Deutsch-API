"""create sentences

Revision ID: 5116f7ec1969
Revises: c3e77c7f8487
Create Date: 2024-05-15 09:33:55.699389

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '5116f7ec1969'
down_revision: Union[str, None] = 'c3e77c7f8487'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("sentences")
    op.add_column("sentences", sa.Column("index", sa.Integer(), primary_key=True))
    op.add_column("sentences", sa.Column("german", sa.String(), nullable=False))
    op.add_column("sentences", sa.Column("english", sa.String(), nullable=False))
    op.add_column("sentences", sa.Column("category", sa.String(), nullable=False))

    
def downgrade():
    op.drop_table("sentences")
