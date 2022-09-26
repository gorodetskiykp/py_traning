from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

main_engine = sa.create_engine(
    # 'postgres://localhost:5432/habr_sql?sslmode=disable',
    'sqlite:///foo.db',  # https://docs.sqlalchemy.org/en/14/core/engines.html
    echo=True,
)

DBSession = sessionmaker(
    binds={
        Base: main_engine,
    },
    expire_on_commit=False,
)


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

if __name__ == '__main__':
    with session_scope() as s:
        <actual_code>