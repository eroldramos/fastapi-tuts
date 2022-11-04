"""add content column to post table

Revision ID: 0aeb0b55fa94
Revises: 4535fe2c89f9
Create Date: 2022-11-03 16:06:45.018315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aeb0b55fa94'
down_revision = '4535fe2c89f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
