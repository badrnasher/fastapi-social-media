"""create post tables

Revision ID: fc02f43f181b
Revises: 
Create Date: 2023-09-20 14:16:49.646995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc02f43f181b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False), sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
