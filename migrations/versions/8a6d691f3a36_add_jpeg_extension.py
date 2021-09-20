"""add jpeg extension

Revision ID: 8a6d691f3a36
Revises: ab5b51940dfc
Create Date: 2021-09-20 15:31:56.042402

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8a6d691f3a36'
down_revision = 'ab5b51940dfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'extension')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('extension', mysql.ENUM('mp4', 'jpg', 'png', collation='utf8_bin'), nullable=True))
    # ### end Alembic commands ###