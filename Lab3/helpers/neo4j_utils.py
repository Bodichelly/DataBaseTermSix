from neo4j import GraphDatabase


def db_add_user(tx, user_data):
    users_in_db = tx.run('MATCH (user:User {username: $username}) RETURN user', username=user_data['username'])
    for user in users_in_db:
        existing_username = user['user']['username']
        print(existing_username, user_data['username'])
        if existing_username == user_data['username']:
            return
    tx.run(
        "MERGE (user:User {username: $username})",
        username=user_data['username'],
    )


def db_add_message(tx, message_data):
    tags = message_data['tags'].split(',')
    # esli sho text nada ubrat
    query = ["CREATE (msg:Message {id: $id, text: $text} )"]
    for idx, tag in enumerate(tags):
        if tag != '' and tag is not None:
            query.append(f"MERGE (tag{idx}:Tag {{ name: '{tag}' }})")
            query.append(f"CREATE (msg)-[:HAS_TAG]->(tag{idx})")
    query.append("MERGE (sender:User {username: $senderName})")
    query.append("MERGE (receiver:User {username: $receiverName})")
    query.append("MERGE (sender)-[:SENT {to: $receiverName}]->(msg)")
    query.append("MERGE (msg)-[:TO {from: $senderName}]->(receiver)")
    query_string = '\n'.join(query)
    # print('\n' + query_string + '\n')
    # esli sho text nada ubrat
    tx.run(
        query_string,
        id=message_data['id'],
        text=message_data['text'],
        senderName=message_data['sender_id'],
        receiverName=message_data['receiver_id']
    )


class Neo4j:
    def __init__(self):
        self.db_driver = GraphDatabase.driver("bolt://localhost:11003", auth=("neo4j", "password"))

    def add_message(self, message_data):
        with self.db_driver.session() as session:
            session.write_transaction(db_add_message, message_data)

    def register_user(self, user_data):
        with self.db_driver.session() as session:
            session.write_transaction(db_add_user, user_data)


db = Neo4j()


# WITH ['fun', 'forecast'] as tags
# MATCH (u:User)
# WHERE u.name in tags
# WITH collect(u) as users
# WITH head(users) as head, tail(users) as users
# MATCH (head)-[:HAS_TAG]->(m:Movie)
# WHERE ALL(p in persons WHERE (p)-[:ACTED_IN]->(m))
# RETURN m

# WITH ['fun', 'forecast'] as tags
# MATCH (tag:Tag)
# WHERE tag.name in tags
# WITH collect(tag) as tags
# MATCH (msg:Message)
# WHERE ALL(t in tag WHERE (msg)-[:HAS_TAG]->(t))
# MATCH (user:User)-[:SENT|TO]->(msg)
# RETURN user as Users