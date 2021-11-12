"""add content column to  post table

Revision ID: 73527f359599
Revises: 0bd89bee98c1
Create Date: 2021-11-11 23:59:17.983044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73527f359599'
down_revision = '0bd89bee98c1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
