"""create

Revision ID: 0a86e02234fa
Revises: 
Create Date: 2022-02-17 01:31:59.139094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a86e02234fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cards',
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_shot_date', sa.DateTime(), nullable=True),
    sa.Column('second_shot_date', sa.DateTime(), nullable=True),
    sa.Column('vaccine_name', sa.String(), nullable=False),
    sa.Column('health_unit_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('cpf'),
    sa.UniqueConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_cards')
    # ### end Alembic commands ###
