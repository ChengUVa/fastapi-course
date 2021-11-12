"""create post table

Revision ID: 0bd89bee98c1
Revises: 
Create Date: 2021-11-11 23:49:40.043725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bd89bee98c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('title', sa.String, nullable=False))


def downgrade():
    op.drop_table('posts')
