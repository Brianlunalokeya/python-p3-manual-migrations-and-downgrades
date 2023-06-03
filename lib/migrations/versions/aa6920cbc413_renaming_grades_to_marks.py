"""Renaming grades to marks

Revision ID: aa6920cbc413
Revises: 1a3ff0e88621
Create Date: 2023-06-03 15:24:45.306388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa6920cbc413'
down_revision = '1a3ff0e88621'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('student', 'grades', new_column_name='marks', existing_type=sa.Integer)

def downgrade() -> None:
    op.alter_column('student', 'marks', new_column_name='grades', existing_type=sa.Integer)