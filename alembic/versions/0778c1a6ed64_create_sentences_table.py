"""create sentences table

Revision ID: 0778c1a6ed64
Revises: 84b8bce2ada0
Create Date: 2023-03-06 18:28:24.968230

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "0778c1a6ed64"
down_revision = "84b8bce2ada0"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("sentences")


def downgrade():
    op.drop_table("sentences")
