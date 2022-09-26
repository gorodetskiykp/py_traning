with session_scope() as s:

    questions = s.query(Question).filter(
        Question.topic_id == t1_id,
    ).order_by(Question.id.desc()).limit(10).all()

    # SELECT *
    # FROM
    # question
    # WHERE
    # topic_id = 1
    # ORDER
    # BY
    # id
    # DESC
    # LIMIT
    # 10;

    questions = s.query(Question).filter(
        Question.topic_id == 1,
        sa.or_(Question.text.ilike('%fart%'), ~Question.text.ilike('%dog%'))
    )

    questions = s.query(Question).filter(
        (Question.topic_id == 1) &
        (Question.text.ilike('%fart%') | ~Question.text.ilike('%dog%'))
    )

    for q in questions:
        print(q.id)

    # SELECT *
    # FROM
    # question
    # WHERE(
    #     topic_id=1
    # AND(
    #     text
    # ILIKE
    # '%fart%'
    # OR
    # NOT(text
    # ILIKE
    # '%dog%')
    # )
    # );

    # 2 запроса
    q = s.query(Question).filter(Question.id == 1).first()
    print(q.topic.title)

    # 1 запрос
    # Eager Loading
    # https://docs.sqlalchemy.org/en/13/orm/tutorial.html#eager-loading
    # https://docs.sqlalchemy.org/en/13/orm/loading_relationships.html
    q = s.query(Question).filter(
        Question.id == 1,
    ).options(joinedload(Question.topic)).first()
    print(q.topic.title)


with session_scope() as s:
    q = s.query(Question).filter(Question.id == 1).first()
print(q.topic.title)
# sqlalchemy.orm.exc.DetachedInstanceError: Parent instance <Question at 0x109dde470> is not bound to a Session; lazy load operation of attribute 'topic' cannot proceed


# 3 запроса (4.2, 4.3 - кэшируются, при возможности)
with session_scope() as s:
    for q in s.query(Question).filter(Question.topic_id == 1).all():  # sa.4.1
        print(q.topic.title)  # sa.4.2
        print(q.topic.image.name)  # sa.4.3

# 1 запрос
with session_scope() as s:
    for q in s.query(Question).options(
        joinedload('topic'),
        joinedload('topic.image'),
    ).filter(Question.topic_id == 1).all():  # sa.4.4
        print(q.topic.title)  # sa.4.5
        print(q.topic.image.name)  # sa.4.6


for t in s.query(Topic).filter(Topic.id.in_([1, 2])).all():  # sa.5.1
    print([q.text for q in t.questions])  # sa.5.2

for t in s.query(Topic).options(joinedload('questions')).filter(Topic.id.in_([1, 2])).all():
    print([q.text for q in t.questions])


q_stmt = s.query(Question).filter(Question.text.ilike('%fart%')).subquery()  # sa.6.1
alias = aliased(Question, q_stmt)  # sa.6.2

filtered_topics = s.query(Topic).outerjoin(  # sa.6.3
    Topic.questions.of_type(alias),  # sa.6.4
).options(
    contains_eager(Topic.questions.of_type(alias)),  # sa.6.5
)

for t in filtered_topics:
    print(f'{t.title}')
    for q in t.questions:
        print(f' --- {q.text}')


topic_ids = s.query(
    Question.topic_id.label('topic_id'),
).group_by(Question.topic_id).having(
    sa.func.count(Question.id) > 1,
)

topics = s.query(Topic).filter(Topic.id.in_(topic_ids))

for t in topics:
    print(f'{t.title}')


topic_ids = s.query(Question.topic_id.label('topic_id')).filter(
    Question.text.ilike('%best%'),
).group_by(Question.topic_id).having(
    sa.func.count(Question.id) > 10,
).cte(name='topic_ids')

topics = s.query(Topic).filter(Topic.id.in_(sa.select([topic_ids.c.topic_id])))
print(', '.join(t.title for t in topics))


for t in s.query(Topic).all():  # sa.9.1
    names = ', '.join(u.name for u in t.users)   # sa.9.2
    print(f'Topic[{t.title}]: {names}')

for t in s.query(Topic).options(
        joinedload('users'),
).all():
    names = ', '.join(u.name for u in t.users)
    print(f'Topic[{t.title}]: {names}')