# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 Deepchecks (https://www.deepchecks.com)
#
# This file is part of Deepchecks.
# Deepchecks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with Deepchecks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
"""monitors schemas update

Revision ID: 0d2eb31dab85
Revises: 320b2ed2c803
Create Date: 2023-02-20 15:33:01.266416

"""
from copy import copy

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision = '0d2eb31dab85'
down_revision = '320b2ed2c803'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    perform_action(upgrade_json_schema)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    perform_action(downgrade_json_schema)
    # ### end Alembic commands ###


def upgrade_json_schema(schema):
    schema_copy = copy(schema)

    for k in schema_copy["properties"]:
        kind = schema_copy["properties"][k]["type"]
        if kind == "integer":
            schema_copy["properties"][k] = {"type": "integer", "maximum": 2147483647, "minimum": -2147483648}
        if isinstance(kind, list) and set(kind) == {"null", "integer"}:
            schema_copy["properties"][k] = {"type": ["integer", "null"], "maximum": 2147483647, "minimum": -2147483648}

    return schema_copy


def downgrade_json_schema(schema):
    schema_copy = copy(schema)

    for k in schema_copy["properties"]:
        kind = schema_copy["properties"][k]["type"]
        if kind == "integer" or isinstance(kind, list) and set(kind) == {"null", "integer"}:
            schema_copy["properties"][k].pop("maximum", None)
            schema_copy["properties"][k].pop("minimum", None)

    return schema_copy


def perform_action(action):
    # NOTE:
    # it is not safe and correct to perform update operations, like below, in
    # read-commited isolation level but in current situation it is safe
    # because we never update models versions schemas

    model_version = sa.table(
        "model_versions",
        sa.column("id", sa.Integer),
        sa.column("monitor_json_schema", JSONB),
        sa.column("reference_json_schema", JSONB)
    )

    connection = op.get_bind()

    model_versions = connection.execute(
        sa.select(
            model_version.c.id,
            model_version.c.monitor_json_schema,
            model_version.c.reference_json_schema
        )
    ).all()

    for version in model_versions:
        connection.execute(
            sa.update(model_version)
            .where(model_version.c.id == version["id"])
            .values(
                monitor_json_schema=action(version["monitor_json_schema"]),
                reference_json_schema=action(version["reference_json_schema"])
            )
        )
