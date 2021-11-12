"""add last few columns to posts table

Revision ID: 6f566c79e942
Revises: 3881bc99fc6f
Create Date: 2021-11-12 11:19:17.320269

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '6f566c79e942'
down_revision = '3881bc99fc6f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
