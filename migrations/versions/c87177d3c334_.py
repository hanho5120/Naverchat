"""empty message

Revision ID: c87177d3c334
Revises: 
Create Date: 2021-03-05 12:56:38.369743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c87177d3c334'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('brand', sa.String(length=200), nullable=False),
    sa.Column('lprice', sa.String(length=200), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('buy_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rank',
    sa.Column('index', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('index')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rank')
    op.drop_table('buy')
    # ### end Alembic commands ###
