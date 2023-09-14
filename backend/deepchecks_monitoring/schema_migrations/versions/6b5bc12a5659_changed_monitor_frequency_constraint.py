# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 Deepchecks (https://www.deepchecks.com)
#
# This file is part of Deepchecks.
# Deepchecks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with Deepchecks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
"""changed monitor.frequency constraint

Revision ID: 6b5bc12a5659
Revises: c5d2ffb432e7
Create Date: 2022-09-28 16:27:08.641553

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6b5bc12a5659'
down_revision = 'c5d2ffb432e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TABLE monitors ADD CONSTRAINT only_positive_frequency CHECK(frequency > 0);")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TABLE monitors DROP CONSTRAINT only_positive_frequency;")
    # ### end Alembic commands ###