"""file table

Revision ID: 5ee31c27d8ad
Revises: 5c743ed11e31
Create Date: 2021-09-16 00:22:50.935264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5ee31c27d8ad"
down_revision = "5c743ed11e31"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "file",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column(
            "extension",
            sa.Enum("mp4", "jpg", "png", name="allowedextensions"),
            nullable=True,
        ),
        sa.Column("updated_time", sa.DateTime(), nullable=True),
        sa.Column("data", sa.BLOB(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("file")
    # ### end Alembic commands ###
