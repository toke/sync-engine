"""create sequence_number column

Revision ID: 606447e78e7
Revises:14692efd261b
Create Date: 2015-06-29 14:56:45.745668

"""

# revision identifiers, used by Alembic.
revision = '606447e78e7'
down_revision = '14692efd261b'

from alembic import op
from sqlalchemy.sql import text


def upgrade():
    conn = op.get_bind()
    conn.execute(text("set @@lock_wait_timeout = 20;"))
    conn.execute(text("ALTER TABLE event ADD COLUMN sequence_number int(11) DEFAULT '0', "
                      "ALGORITHM=inplace,LOCK=none"))
    conn.execute(text("UPDATE event SET sequence_number='0' "
                      "WHERE sequence_number is NULL"))


def downgrade():
    op.drop_column('event', 'sequence_number')
