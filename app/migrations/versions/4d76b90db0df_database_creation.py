"""Database creation

Revision ID: 4d76b90db0df
Revises: 
Create Date: 2024-06-26 22:45:03.835712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4d76b90db0df'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('name')
                    )
    op.create_index(op.f('ix_author_id'), 'author', ['id'], unique=False)
    op.create_table('category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_table('tag',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_index(op.f('ix_tag_id'), 'tag', ['id'], unique=False)
    op.create_table('post',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.Text(), nullable=False),
                    sa.Column('author_id', sa.Integer(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
                    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_post_id'), 'post', ['id'], unique=False)
    op.create_table('posts_tags',
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.Column('tag_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
                    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
                    sa.PrimaryKeyConstraint('post_id', 'tag_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts_tags')
    op.drop_index(op.f('ix_post_id'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_tag_id'), table_name='tag')
    op.drop_table('tag')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    op.drop_index(op.f('ix_author_id'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
