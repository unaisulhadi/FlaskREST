"""empty message

Revision ID: 211b3e57cdde
Revises: 62d34cb1123b
Create Date: 2022-11-23 15:54:32.144004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '211b3e57cdde'
down_revision = '62d34cb1123b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
