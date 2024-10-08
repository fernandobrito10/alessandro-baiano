"""Adiciona relação de usuário nos atendimentos

Revision ID: f27bf5b8e269
Revises: 
Create Date: 2024-09-27 09:41:42.720383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f27bf5b8e269'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('atendimento', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.alter_column('data',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=8),
               existing_nullable=False)
        batch_op.alter_column('hora',
               existing_type=sa.VARCHAR(length=5),
               type_=sa.String(length=6),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('atendimento', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('hora',
               existing_type=sa.String(length=6),
               type_=sa.VARCHAR(length=5),
               existing_nullable=False)
        batch_op.alter_column('data',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
