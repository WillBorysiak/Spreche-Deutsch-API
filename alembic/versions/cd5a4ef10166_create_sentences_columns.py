"""create sentences columns

Revision ID: cd5a4ef10166
Revises: 0778c1a6ed64
Create Date: 2023-03-06 18:30:40.828913

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "cd5a4ef10166"
down_revision = "0778c1a6ed64"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("sentences", sa.Column("index", sa.Integer(), primary_key=True))
    op.add_column("sentences", sa.Column("german", sa.String(), nullable=False))
    op.add_column("sentences", sa.Column("english", sa.String(), nullable=False))
    op.add_column("sentences", sa.Column("category", sa.String(), nullable=False))


def downgrade():
    op.drop_column("sentences", "index")
    op.drop_column("sentences", "german")
    op.drop_column("sentences", "english")
    op.drop_column("sentences", "category")
