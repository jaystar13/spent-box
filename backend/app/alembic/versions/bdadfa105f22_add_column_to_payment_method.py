"""add column to payment-method

Revision ID: bdadfa105f22
Revises: 1a1faf4277d9
Create Date: 2025-06-14 21:39:13.817297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdadfa105f22'
down_revision: Union[str, None] = '1a1faf4277d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment_method', sa.Column('user_id', sa.Uuid(), nullable=False))
    op.add_column('payment_method', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.create_foreign_key(None, 'payment_method', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payment_method', type_='foreignkey')
    op.drop_column('payment_method', 'created_at')
    op.drop_column('payment_method', 'user_id')
    # ### end Alembic commands ###
