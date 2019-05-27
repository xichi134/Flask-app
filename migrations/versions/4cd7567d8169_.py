"""empty message

Revision ID: 4cd7567d8169
Revises: 450c094cadc7
Create Date: 2019-05-19 15:46:27.448457

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4cd7567d8169'
down_revision = '450c094cadc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ih_area_info', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.drop_column('ih_area_info', 'updata_time')
    op.add_column('ih_facility_info', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.drop_column('ih_facility_info', 'updata_time')
    op.add_column('ih_house_image', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.drop_column('ih_house_image', 'updata_time')
    op.add_column('ih_house_info', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.drop_column('ih_house_info', 'updata_time')
    op.add_column('ih_order_info', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.drop_column('ih_order_info', 'updata_time')
    op.add_column('ih_user_profile', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.drop_column('ih_user_profile', 'updata_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ih_user_profile', sa.Column('updata_time', mysql.DATETIME(), nullable=True))
    op.drop_column('ih_user_profile', 'update_time')
    op.add_column('ih_order_info', sa.Column('updata_time', mysql.DATETIME(), nullable=True))
    op.drop_column('ih_order_info', 'update_time')
    op.add_column('ih_house_info', sa.Column('updata_time', mysql.DATETIME(), nullable=True))
    op.drop_column('ih_house_info', 'update_time')
    op.add_column('ih_house_image', sa.Column('updata_time', mysql.DATETIME(), nullable=True))
    op.drop_column('ih_house_image', 'update_time')
    op.add_column('ih_facility_info', sa.Column('updata_time', mysql.DATETIME(), nullable=True))
    op.drop_column('ih_facility_info', 'update_time')
    op.add_column('ih_area_info', sa.Column('updata_time', mysql.DATETIME(), nullable=True))
    op.drop_column('ih_area_info', 'update_time')
    # ### end Alembic commands ###
