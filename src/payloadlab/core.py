def normalize(item):
    return {"name": str(item.get("name", "unnamed")), "category": str(item.get("category", "generic")), "description": str(item.get("description", ""))}

def catalog(items, category=None):
    records = [normalize(i) for i in items]
    if category is None:
        return records
    return [i for i in records if i["category"].lower() == category.lower()]
