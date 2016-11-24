"""empty message

Revision ID: 394d2764bdbb
Revises: 
Create Date: 2016-11-24 12:01:23.787987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '394d2764bdbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    ### end Alembic commands ###