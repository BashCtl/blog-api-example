"""update comments table

Revision ID: 8926245ea8ed
Revises: 533b8090c25b
Create Date: 2023-09-04 11:04:03.748715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8926245ea8ed'
down_revision: Union[str, None] = '533b8090c25b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))
    op.add_column('comments', sa.Column('author_id', sa.Integer(), nullable=False))
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'comments', 'accounts', ['author_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'post_id')
    op.drop_column('comments', 'author_id')
    op.drop_column('comments', 'created_at')
    # ### end Alembic commands ###
