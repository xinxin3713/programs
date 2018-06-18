class Suger:
    price = 3
    name = "ice"
    @classmethod
    def add_suger_pritce(cls,fun):
        def get_price(*args, **kwargs):
            org = fun(*args, **kwargs)
            new_price =  cls.price + org
            return new_price
        return get_price
    @classmethod
    def add_suger_name(cls,fun):
        def get_name(*args, **kwargs):
            name = fun(*args, **kwargs)
            new_name = name +'with'+cls.name
            return new_name
        return get_name