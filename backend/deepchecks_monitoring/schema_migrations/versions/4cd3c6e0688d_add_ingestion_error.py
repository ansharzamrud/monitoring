# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 Deepchecks (https://www.deepchecks.com)
#
# This file is part of Deepchecks.
# Deepchecks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with Deepchecks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
"""add ingestion error

Revision ID: 4cd3c6e0688d
Revises: e0ec67ddf099
Create Date: 2022-08-31 14:45:25.696775

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '4cd3c6e0688d'
down_revision = 'e0ec67ddf099'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingestion_errors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('samples_ids', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('samples', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('error', sa.String(), nullable=True),
        sa.Column('model_version_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['model_version_id'], ['model_versions.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ingestion_errors')
    # ### end Alembic commands ###