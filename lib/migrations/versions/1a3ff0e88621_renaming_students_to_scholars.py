"""Renaming students to scholars

Revision ID: 1a3ff0e88621
Revises: 791279dd0760
Create Date: 2023-06-03 11:28:45.354532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a3ff0e88621'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')