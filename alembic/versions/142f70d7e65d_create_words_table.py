"""create words table

Revision ID: 142f70d7e65d
Revises: 
Create Date: 2023-02-25 18:00:36.803751

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "142f70d7e65d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("words")


def downgrade() -> None:
    pass
