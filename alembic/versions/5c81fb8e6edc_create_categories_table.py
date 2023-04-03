"""create categories table

Revision ID: 5c81fb8e6edc
Revises: cd5a4ef10166
Create Date: 2023-04-03 18:55:21.635358

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "5c81fb8e6edc"
down_revision = "cd5a4ef10166"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("categories")


def downgrade():
    op.drop_table("categories")
