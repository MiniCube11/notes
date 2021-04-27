"""Add admin user

Revision ID: 9b5c6b2e9d0f
Revises: fca47933e1f8
Create Date: 2021-04-24 14:41:21.350060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b5c6b2e9d0f'
down_revision = 'fca47933e1f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_users_is_admin'), 'users', ['is_admin'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_is_admin'), table_name='users')
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###