"""Add db relationships

Revision ID: b1654316ff87
Revises: 53c22090f46a
Create Date: 2021-04-20 10:38:15.241911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1654316ff87'
down_revision = '53c22090f46a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'notes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.drop_column('notes', 'user_id')
    # ### end Alembic commands ###