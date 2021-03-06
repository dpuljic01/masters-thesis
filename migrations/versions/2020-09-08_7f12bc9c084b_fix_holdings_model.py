"""fix holdings model

Revision ID: 7f12bc9c084b
Revises: 946565782411
Create Date: 2020-09-08 02:19:48.025352

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "7f12bc9c084b"
down_revision = "946565782411"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "holdings", sa.Column("shares", sa.Numeric(asdecimal=False), nullable=False)
    )
    op.add_column(
        "holdings", sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False)
    )
    op.create_foreign_key(
        op.f("fk_holdings_user_id_users"),
        "holdings",
        "users",
        ["user_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_holdings_user_id_users"), "holdings", type_="foreignkey"
    )
    op.drop_column("holdings", "user_id")
    op.drop_column("holdings", "shares")
    # ### end Alembic commands ###
