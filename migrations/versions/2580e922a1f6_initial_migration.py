"""initial migration

Revision ID: 2580e922a1f6
Revises: 
Create Date: 2024-04-23 16:29:16.837897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2580e922a1f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('username', sa.String(length=255), nullable=False),
                    sa.Column('hashed_password', sa.String(length=255), nullable=False),
                    sa.Column('date_joined', sa.TIMESTAMP(), nullable=False),
                    sa.Column('last_created', sa.TIMESTAMP(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.Column('roles_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['roles_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
