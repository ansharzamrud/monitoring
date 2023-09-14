"""create initial models

Revision ID: 54e5bc18581b
Revises:
Create Date: 2022-08-24 11:22:58.317786

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '54e5bc18581b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organisations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('schema_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('schema_name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=False),
    sa.Column('picture_url', sa.String(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('last_login', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.Column('api_token', sa.String(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['organisations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('organisations')
    # ### end Alembic commands ###