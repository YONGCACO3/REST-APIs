"""empty message

Revision ID: 1d8d916e81d8
Revises: 86e943d74d1d
Create Date: 2023-12-21 15:21:17.928098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d8d916e81d8'
down_revision = '86e943d74d1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint('email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('email', type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
