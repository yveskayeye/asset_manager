"""empty message

Revision ID: 2dee7061f424
Revises: 
Create Date: 2022-02-11 20:52:09.088953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dee7061f424'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assets',
    sa.Column('asset_tag', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=False),
    sa.Column('item_discription', sa.String(length=80), nullable=False),
    sa.Column('condition', sa.String(length=80), nullable=False),
    sa.Column('serial', sa.String(length=80), nullable=False),
    sa.Column('date_manufactured', sa.String(length=80), nullable=False),
    sa.Column('cost', sa.String(length=80), nullable=False),
    sa.Column('purchase_date', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('asset_tag'),
    sa.UniqueConstraint('condition'),
    sa.UniqueConstraint('cost'),
    sa.UniqueConstraint('date_manufactured'),
    sa.UniqueConstraint('item_discription'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('purchase_date'),
    sa.UniqueConstraint('serial'),
    sa.UniqueConstraint('type')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('assets')
    # ### end Alembic commands ###
