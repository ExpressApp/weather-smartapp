"""user city

Revision ID: 0a9e32426de3
Revises: c630e92c23e1
Create Date: 2021-03-25 12:20:02.260680

Doc: https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

revision = "0a9e32426de3"
down_revision = "c630e92c23e1"
branch_labels = None
depends_on = None


def create_lastrequest():
    op.create_table(
        "lastrequest",
        sa.Column("city", sa.Text),
        sa.Column(
            "user", UUID, sa.ForeignKey("botxuser.user_huid", ondelete="SET NULL")
        ),
    )


def add_last_city_for_user():
    op.add_column("botxuser", sa.Column("last_city_request", sa.Text))


def drop_lastrequest():
    op.drop_table("lastrequest")


def upgrade():
    add_last_city_for_user()


def downgrade():
    op.drop_column("botxuser", "last_city_request")
