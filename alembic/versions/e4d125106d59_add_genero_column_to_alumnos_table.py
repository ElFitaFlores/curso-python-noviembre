"""Add genero column to alumnos table

Revision ID: e4d125106d59
Revises: 591bcb6bde3b
Create Date: 2022-12-15 18:46:45.688154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4d125106d59'
down_revision = '591bcb6bde3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('alumnos',
        sa.Column('genero', sa.String())
    )


def downgrade() -> None:
    op.drop_column('alumnos', 'genero')
