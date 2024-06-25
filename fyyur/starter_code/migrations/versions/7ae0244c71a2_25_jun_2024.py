"""25-Jun-2024

Revision ID: 7ae0244c71a2
Revises: f8e0473befc0
Create Date: 2024-06-26 00:24:31.627741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ae0244c71a2'
down_revision = 'f8e0473befc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))

    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.drop_column('genres')

    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.drop_column('genres')

    # ### end Alembic commands ###