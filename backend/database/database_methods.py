from .connector import engine

"""
The main purpose of writing this Database class is to avoid calls to the MongoDB engine.
In the future, complex operations which might require two or more engine operations might be
needed and in such event, we can confine them into a class method here.
"""


class Database:
    def __init__(self, collection):
        self.collection = collection

    async def find_one(self, condition):
        item = await engine.find_one(self.collection, condition)
        return item

    async def find(self, ):
        items = await engine.find(self.collection)
        return items

    async def paginate(self, no_of_items, limit):
        start = no_of_items * limit
        items = await engine.find(self.collection, skip=start, limit=limit)
        return items

    async def save(self, item):
        inserted_item = await engine.save(item)

        return inserted_item.id

    async def delete(self, item):
        await engine.delete(item)

        return