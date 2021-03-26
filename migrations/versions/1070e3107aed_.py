"""empty message

Revision ID: 1070e3107aed
Revises: 8ef6a68418ee
Create Date: 2021-03-24 13:53:33.516033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1070e3107aed'
down_revision = '8ef6a68418ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_name', sa.String(), nullable=True),
    sa.Column('song_rank', sa.Integer(), nullable=True),
    sa.Column('song_artist', sa.String(), nullable=True),
    sa.Column('song_this_week', sa.String(), nullable=True),
    sa.Column('song_last_week', sa.String(), nullable=True),
    sa.Column('song_artist_peak_rank', sa.String(), nullable=True),
    sa.Column('song_artist_weeks_on_chart', sa.String(), nullable=True),
    sa.Column('song_picture', sa.String(), nullable=True),
    sa.Column('start_of_week_date', sa.DateTime(), nullable=False),
    sa.Column('song_name_artist_combined', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    # ### end Alembic commands ###