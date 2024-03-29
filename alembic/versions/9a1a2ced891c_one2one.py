"""one2one

Revision ID: 9a1a2ced891c
Revises: 24f611877210
Create Date: 2024-03-29 11:53:57.518007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a1a2ced891c'
down_revision: Union[str, None] = '24f611877210'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('visa_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['visa_id'], ['visas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('visa_number', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visas')
    op.drop_table('users')
    # ### end Alembic commands ###