"""create words columns

Revision ID: 84b8bce2ada0
Revises: 142f70d7e65d
Create Date: 2023-02-25 18:44:29.969667

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "84b8bce2ada0"
down_revision = "142f70d7e65d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("words", sa.Column("index", sa.Integer(), primary_key=True))
    op.add_column("words", sa.Column("german", sa.String(), nullable=False))
    op.add_column("words", sa.Column("english", sa.String(), nullable=False))
    op.add_column("words", sa.Column("gender", sa.String(), nullable=False))
    op.add_column("words", sa.Column("category", sa.String(), nullable=False))


def downgrade():
    op.drop_column("words", "index")
    op.drop_column("words", "german")
    op.drop_column("words", "english")
    op.drop_column("words", "gender")
    op.drop_column("words", "category")
