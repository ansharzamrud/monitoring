# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 Deepchecks (https://www.deepchecks.com)
#
# This file is part of Deepchecks.
# Deepchecks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with Deepchecks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
"""added/modified cascade

Revision ID: b75212c5da00
Revises: 4cd3c6e0688d
Create Date: 2022-09-06 23:39:41.832853

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b75212c5da00'
down_revision = '4cd3c6e0688d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('alert_rules_monitor_id_fkey', 'alert_rules', type_='foreignkey')
    op.create_foreign_key(None, 'alert_rules', 'monitors', ['monitor_id'], ['id'], onupdate='RESTRICT', ondelete='CASCADE')
    op.drop_constraint('alerts_alert_rule_id_fkey', 'alerts', type_='foreignkey')
    op.create_foreign_key(None, 'alerts', 'alert_rules', ['alert_rule_id'], ['id'], onupdate='RESTRICT', ondelete='CASCADE')
    op.alter_column('checks', 'model_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('checks_model_id_fkey', 'checks', type_='foreignkey')
    op.create_foreign_key(None, 'checks', 'models', ['model_id'], ['id'], onupdate='RESTRICT', ondelete='CASCADE')
    op.drop_constraint('ingestion_errors_model_version_id_fkey', 'ingestion_errors', type_='foreignkey')
    op.create_foreign_key(None, 'ingestion_errors', 'model_versions', ['model_version_id'], ['id'], onupdate='RESTRICT', ondelete='CASCADE')
    op.alter_column('model_versions', 'model_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('model_versions_model_id_fkey', 'model_versions', type_='foreignkey')
    op.create_foreign_key(None, 'model_versions', 'models', ['model_id'], ['id'], onupdate='RESTRICT', ondelete='CASCADE')
    op.drop_constraint('monitors_dashboard_id_fkey', 'monitors', type_='foreignkey')
    op.drop_constraint('monitors_check_id_fkey', 'monitors', type_='foreignkey')
    op.create_foreign_key(None, 'monitors', 'dashboards', ['dashboard_id'], ['id'], onupdate='RESTRICT', ondelete='SET NULL')
    op.create_foreign_key(None, 'monitors', 'checks', ['check_id'], ['id'], onupdate='RESTRICT', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'monitors', type_='foreignkey')
    op.drop_constraint(None, 'monitors', type_='foreignkey')
    op.create_foreign_key('monitors_check_id_fkey', 'monitors', 'checks', ['check_id'], ['id'])
    op.create_foreign_key('monitors_dashboard_id_fkey', 'monitors', 'dashboards', ['dashboard_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint(None, 'model_versions', type_='foreignkey')
    op.create_foreign_key('model_versions_model_id_fkey', 'model_versions', 'models', ['model_id'], ['id'])
    op.alter_column('model_versions', 'model_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint(None, 'ingestion_errors', type_='foreignkey')
    op.create_foreign_key('ingestion_errors_model_version_id_fkey', 'ingestion_errors', 'model_versions', ['model_version_id'], ['id'])
    op.drop_constraint(None, 'checks', type_='foreignkey')
    op.create_foreign_key('checks_model_id_fkey', 'checks', 'models', ['model_id'], ['id'])
    op.alter_column('checks', 'model_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint(None, 'alerts', type_='foreignkey')
    op.create_foreign_key('alerts_alert_rule_id_fkey', 'alerts', 'alert_rules', ['alert_rule_id'], ['id'])
    op.drop_constraint(None, 'alert_rules', type_='foreignkey')
    op.create_foreign_key('alert_rules_monitor_id_fkey', 'alert_rules', 'monitors', ['monitor_id'], ['id'])
    # ### end Alembic commands ###