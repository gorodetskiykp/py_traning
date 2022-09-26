from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Image(Base):
    __tablename__ = 'image'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text, nullable=False)


class Topic(Base):
    __tablename__ = 'topic'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.Text, nullable=False)
    image_id = sa.Column(sa.Integer, sa.ForeignKey('image.id'), nullable=False)
    image = sa.orm.relationship(Image)  # innerjoin=True для JOIN
    questions = sa.orm.relationship('Question')

    users = sa.orm.relationship('User', secondary='topic_user')
    # association
    # users = sa.orm.relationship('TopicUser', back_populates='topic')


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text, nullable=False)

    # association
    # topics = sa.orm.relationship('TopicUser', back_populates='user')


class TopicUser(Base):
    __tablename__ = 'topic_user'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    topic_id = sa.Column(sa.Integer, sa.ForeignKey('topic.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    role = sa.Column(sa.Text)

    # association
    # user = sa.orm.relationship(User, back_populates='topics')
    # topic = sa.orm.relationship(Topic, back_populates='users')


class Question(Base):
    __tablename__ = 'question'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    text = sa.Column(sa.Text)
    topic_id = sa.Column(sa.Integer, sa.ForeignKey('topic.id'), nullable=False)
    topic = sa.orm.relationship(Topic)  # innerjoin=True для использования JOIN вместо LEFT JOIN


with session_scope() as s:
    u = s.query(User).filter(User.id == 1).first()  # sa.9.3
    for t in u.topics:  # sa.9.4
        print(f'{u.name} is {t.role} in topic "{t.topic.title}"')  # sa.9.5

u = s.query(User).filter(User.id == 1).options(
    joinedload('topics'),
    selectinload('topics.topic'),
).first()

for t in u.topics:
    print(f'{u.name} is {t.role} in topic "{t.topic.title}"')


s.bulk_save_objects([
    Topic(title=f'topic {i}', image_id=1)
    for i in range(3)
])

s.bulk_update_mappings(
    User,
    [dict(id=1, name='new 1 name'), dict(id=2, name='new 2 name')]
)