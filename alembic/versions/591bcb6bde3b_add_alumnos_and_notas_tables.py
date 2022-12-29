"""Add alumnos and notas tables

Revision ID: 591bcb6bde3b
Revises: 
Create Date: 2022-12-15 18:33:24.040336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '591bcb6bde3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumnos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(), nullable=False),
    sa.Column('apellidos', sa.String(), nullable=False),
    sa.Column('carnet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('carnet')
    )
    op.create_table('notas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curso', sa.String(), nullable=False),
    sa.Column('alumno_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['alumno_id'], ['alumnos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notas')
    op.drop_table('alumnos')
    # ### end Alembic commands ###