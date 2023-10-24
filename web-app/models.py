from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question', sa.String),
        sa.Column('answer', sa.String),
        sa.Column('created_at', sa.DateTime)
    )

def downgrade():
    op.drop_table('questions')
