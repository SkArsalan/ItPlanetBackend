"""date and purchase column added

Revision ID: 77ec5c8bb778
Revises: 185cf10b863c
Create Date: 2024-12-14 11:21:50.141221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77ec5c8bb778'
down_revision = '185cf10b863c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('purchase_price', sa.Float(), nullable=False),
    sa.Column('selling_price', sa.Float(), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('categories', sa.String(length=50), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('selling_price', sa.Float(), nullable=False),
    sa.Column('subtotal', sa.Float(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['inventory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoice_item')
    op.drop_table('inventory')
    # ### end Alembic commands ###