# 모듈 같은 경로에 있어야함
# import theater_module

# theater_module.price(3)
# theater_module.price_morning(3)
# theater_module.price_soldier(3)


# import theater_module as mv

# mv.price(3)
# mv.price_morning(5)
# mv.price_soldier(2)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price, price_morning
price(3)
price_morning(5)


from theater_module import price_soldier as aa
aa(10)