# -*- coding: utf-8 -*-

paragraph = '''
Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well.

In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation.

Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update.
'''

print(paragraph)

# Q1: 印出這個段落的長度
# Q2: 把文章裡 'GraphQL' 這個單字變全大寫, 其餘單字變全小寫
# Q3: 印出這個段落有多少個英文單字(不含標點符號與空白)
