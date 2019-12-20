import pymongo
from bson.objectid import ObjectId
MONGODB_URL = 'mongodb://localhost:27017/'
MONGODB_DB_NAME = 'testdb'  # 数据库名

# 数据库名和url的名字是有默认值的，但是每次的表名是要重新定义的。
def connect_mongodb(col_name, db_name=MONGODB_DB_NAME, db_url=MONGODB_URL):
    """连接到mongodb数据库"""
    myclient = pymongo.MongoClient(db_url)
    mydb = myclient[db_name]
    mycol = mydb[col_name]
    return mycol

if __name__ == '__main__':
    # 连接user数据库
    muser_col = connect_mongodb(col_name="user")

    插入一条数据
    user1 = {
        "name":"qingwen",
        "age":16
        }

    a = muser_col.insert_one(user1)

    print(type(a)) # <class 'pymongo.results.InsertOneResult'>
    print(dir(a))  # 查看a的属性和方法
    print(a.inserted_id) # 5dfc7a441b7199965474fa3c 实际上就是ObjectId("5dfc7a441b7199965474fa3c")


    mbook_col = connect_mongodb(col_name = "book")

    book1 = {
         "userid":a.inserted_id,
         "name": "how to learn python",
         "price":15
        }
    
    book2 = {
         "userid":a.inserted_id,
         "name": "how to learn java",
         "price":28
     }

    book3 = {
         "userid":a.inserted_id,
         "name": "how to learn c++",
         "price":56
     }
    #插入操作
    b = mbook_col.insert_many([book1,book2,book3])
    print(type(b))
    print(b.inserted_ids)
    for id in b.inserted_ids:
        print(id)


    查询操作(结果只有一条)
    res = muser_col.find_one({"name":"qingwen","age":16})
    print(type(res))   # <class 'dict'>
    print(dir(res))

    user_id = res["_id"]
    print(user_id)

    查询操作，结果不只一条
    我们再插入一条数据
    user2 = {
        "name":"qingwen",
        "age":18
        }
    muser_col.insert_one(user2)

    res = muser_col.find({"name":"qingwen"})
    print(type(res))   
    print(dir(res))
    for book in res:
        print(book)

    查询操作，外键约束
    user_id = muser_col.find_one({"name":"qingwen"})["_id"]

    books = mbook_col.find({"userid":ObjectId(user_id)})

    for b in books:
        print(b)

    计数
    num = mbook_col.count_documents({"price":{'$gt':27}})
    print(num)
    
    更新数据（仅更改一条）
    res = muser_col.update_one({"name":"qingwen"},{"$set":{"age":"22"}})
    print(type(res))
    print(res)
    print(res.matched_count, res.modified_count)

    更新数据(所有符合条件的语句)
    res = muser_col.update_many({"name":"qingwen"},{"$set":{"age":"23"}})
    print(type(res))
    print(dir(res))
    print(res.matched_count, res.modified_count)

    # 删除数据(一条数据)
    res = mbook_col.delete_one({"price":28})
    print(type(res))
    print(dir(res))
    print(res.deleted_count)

    # 删除符合条件的所有的条目。
    res = mbook_col.delete_many({"price":28})



    
