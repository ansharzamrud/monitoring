# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 Deepchecks (https://www.deepchecks.com)
#
# This file is part of Deepchecks.
# Deepchecks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with Deepchecks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
"""remove monitors table deletion triggers

Revision ID: 14daeddd99d6
Revises: 6b5bc12a5659
Create Date: 2022-10-25 18:08:17.457014

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '14daeddd99d6'
down_revision = '6b5bc12a5659'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP TRIGGER IF EXISTS trigger_model_version_delete ON model_versions;")
    op.execute("DROP FUNCTION IF EXISTS drop_model_version_tables;")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    from deepchecks_monitoring.schema_models.model_version import PGDataTableDropFunc, PGDataTableDropTrigger
    PGDataTableDropFunc.execute(bind=op.get_bind())
    PGDataTableDropTrigger.execute(bind=op.get_bind())
    # ### end Alembic commands ###
