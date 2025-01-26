"""Add sales_returns table

Revision ID: 689517ec5db6
Revises: 81aad297734a
Create Date: 2025-01-23 16:58:55.671995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '689517ec5db6'
down_revision = '81aad297734a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales_returns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.Column('sale', sa.String(length=255), nullable=True),
    sa.Column('return_item', sa.String(length=255), nullable=True),
    sa.Column('retail_sale_amount', sa.Float(), nullable=True),
    sa.Column('wholesale_sale_amount', sa.Float(), nullable=True),
    sa.Column('return_amount', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales_returns')
    # ### end Alembic commands ###
