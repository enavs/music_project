"""empty message

Revision ID: 58d2f6b31955
Revises: ccd39f619cb1
Create Date: 2021-03-25 15:22:18.510297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58d2f6b31955'
down_revision = 'ccd39f619cb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('price', sa.Float(), nullable=True))
    op.add_column('product', sa.Column('song_name_artist_combined', sa.String(), nullable=True))
    op.add_column('product', sa.Column('song_picture', sa.String(), nullable=True))
    op.add_column('product', sa.Column('tax', sa.Float(), nullable=True))
    op.create_unique_constraint(None, 'song', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'song', type_='unique')
    op.drop_column('product', 'tax')
    op.drop_column('product', 'song_picture')
    op.drop_column('product', 'song_name_artist_combined')
    op.drop_column('product', 'price')
    # ### end Alembic commands ###