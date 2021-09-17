"""change blob

Revision ID: 9a91325da470
Revises: d268d699fb9d
Create Date: 2021-09-16 01:35:39.088312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9a91325da470"
down_revision = "d268d699fb9d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "file", sa.Column("data", sa.LargeBinary(length=12071628), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("file", "data")
    # ### end Alembic commands ###
