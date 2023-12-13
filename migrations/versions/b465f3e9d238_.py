"""empty message

Revision ID: b465f3e9d238
Revises: e5f4b1604060
Create Date: 2023-12-13 19:44:00.831479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b465f3e9d238'
down_revision = 'e5f4b1604060'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=250),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=250),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
