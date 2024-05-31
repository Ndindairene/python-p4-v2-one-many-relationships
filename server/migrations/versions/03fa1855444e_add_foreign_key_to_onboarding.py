# migrations/versions/03fa1855444e_add_foreign_key_to_onboarding.py
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '03fa1855444e'
down_revision = 'bff1ea31d268'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_onboardings_employee_id', 'employees', ['employee_id'], ['id'])

def downgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id', type_='foreignkey')
        batch_op.drop_column('employee_id')
