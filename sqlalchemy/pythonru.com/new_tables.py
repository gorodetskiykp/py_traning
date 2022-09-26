from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from datetime import datetime

metadata = MetaData()

blog = Table('blog', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(), nullable=False),
    Column('published', Boolean(), default=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


"""
primary_key	
Булево. Если значение равно True, отмечает колонку как первичный ключ таблицы. Для создания составного ключа, 
нужно просто установить значение True для каждой колонки.

nullable	
Булево. Если False, то добавляет ограничение NOT NULL. Значение по умолчанию равно True.

default	
Определяет значение по умолчанию, если при вставке данных оно не было передано. Может быть как скалярное значение, 
так и вызываемое значение Python.

onupdate	
Значение по умолчанию для колонки, которое устанавливается, если ничего не было передано при обновлении записи. 
Может принимать то же значение, что и default.

unique	
Булево. Если True, следит за тем, чтобы значение было уникальным.

index	
Булево. Если True, создает индексируемую колонку. По умолчанию False.

auto_increment	
Добавляет параметр auto_increment для колонки. Значение по умолчанию равно auto. 
Это значит, что значение основного ключа будет увеличиваться каждый раз при добавлении новой записи. 
Если нужно увеличить значение для каждого элемента составного ключа, то этот параметр нужно задать как True 
для всех колонок ключа. Для отключения поведения нужно установить значение False
"""

"""
SQLAlchemy	    Python	            SQL
BigInteger	    int	                BIGINT
Boolean	        bool	            BOOLEAN или SMALLINT
Date	        datetime.date	    DATE
DateTime	    datetime.datetime	DATETIME
Integer	        int	                INTEGER
Float	        float	            FLOAT или REAL
Numeric	        decimal.Decimal	    NUMERIC
Text	        str	                TEXT
"""


from sqlalchemy import MetaData, Table, Column, Integer, ARRAY

metadata = MetaData()

employee = Table('employees', metadata,
    Column('id', Integer(), primary_key=True),
    Column('workday', ARRAY(Integer)),
)

# тип ARRAY поддерживается только PostgreSQL
# INET для хранения сетевых данных поддерживается только PostgreSQL

from sqlalchemy import MetaData, Table, Column, Integer
from sqlalchemy.dialects import postgresql

metadata = MetaData()

comments = Table('comments', metadata,
    Column('id', Integer(), primary_key=True),
    Column('ipaddress', postgresql.INET),
)