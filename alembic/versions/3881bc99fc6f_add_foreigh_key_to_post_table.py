"""add foreigh-key to post table

Revision ID: 3881bc99fc6f
Revises: 702dbb20ebde
Create Date: 2021-11-12 11:14:23.382872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3881bc99fc6f'
down_revision = '702dbb20ebde'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', 
                            local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')

