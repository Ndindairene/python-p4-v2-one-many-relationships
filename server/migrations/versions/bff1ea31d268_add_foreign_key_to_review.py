from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'bff1ea31d268'
down_revision = '1c8ebf45ba6b'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reviews_employee_id', 'employees', ['employee_id'], ['id'])

def downgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id', type_='foreignkey')
        batch_op.drop_column('employee_id')
