from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey

metadata = MetaData()

user = Table('users', metadata,
    Column('id', Integer(), primary_key=True),
    Column('user', String(200), nullable=False),
)

posts = Table('posts', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(),  nullable=False),
    Column('user_id', ForeignKey("users.id")),
    # Column('user_id', Integer(), ForeignKey(user.c.id),
)


from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey

metadata = MetaData()

employees = Table('employees', metadata,
    Column('employee_id', Integer(), primary_key=True),
    Column('first_name', String(200), nullable=False),
    Column('last_name', String(200), nullable=False),
    Column('dob', DateTime(), nullable=False),
    Column('designation', String(200), nullable=False),
)

employee_details = Table('employee_details', metadata,
    Column('employee_id', ForeignKey('employees.employee_id'), primary_key=True),
    Column('ssn', String(200), nullable=False),
    Column('salary', String(200), nullable=False),
    Column('blood_group', String(200), nullable=False),
    Column('residential_address', String(200), nullable=False),
)


from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey

metadata = MetaData()

posts = Table('posts', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(),  nullable=False),
)

tags = Table('tags', metadata,
    Column('id', Integer(), primary_key=True),
    Column('tag', String(200), nullable=False),
    Column('tag_slug', String(200),  nullable=False),
)

post_tags = Table('post_tags', metadata,
    Column('post_id', ForeignKey('posts.id')),
    Column('tag_id', ForeignKey('tags.id'))
)