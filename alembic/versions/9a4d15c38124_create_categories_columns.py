"""create categories columns

Revision ID: 9a4d15c38124
Revises: 5c81fb8e6edc
Create Date: 2023-04-03 18:59:10.394006

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9a4d15c38124"
down_revision = "5c81fb8e6edc"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("categories", sa.Column("index", sa.Integer(), primary_key=True))
    op.add_column("categories", sa.Column("name", sa.String(), nullable=False))
    op.add_column("categories", sa.Column("type", sa.String(), nullable=False))
    op.add_column("categories", sa.Column("route", sa.String(), nullable=False))


def downgrade():
    op.drop_column("categories", "index")
    op.drop_column("categories", "name")
    op.drop_column("categories", "type")
    op.drop_column("categories", "route")
