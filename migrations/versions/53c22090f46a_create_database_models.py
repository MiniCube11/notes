"""Create database models

Revision ID: 53c22090f46a
Revises: 
Create Date: 2021-04-20 09:13:33.710785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53c22090f46a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('is_public', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notes_body'), 'notes', ['body'], unique=False)
    op.create_index(op.f('ix_notes_is_public'), 'notes', ['is_public'], unique=False)
    op.create_index(op.f('ix_notes_key'), 'notes', ['key'], unique=True)
    op.create_index(op.f('ix_notes_title'), 'notes', ['title'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('userid', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_userid'), 'users', ['userid'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_userid'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_notes_title'), table_name='notes')
    op.drop_index(op.f('ix_notes_key'), table_name='notes')
    op.drop_index(op.f('ix_notes_is_public'), table_name='notes')
    op.drop_index(op.f('ix_notes_body'), table_name='notes')
    op.drop_table('notes')
    # ### end Alembic commands ###
