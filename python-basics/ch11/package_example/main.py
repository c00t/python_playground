# main.py
# 引入mypackage
# import mypackage.module1, mypackage.module2
from mypackage import module2, module1
from mypackage.mysubpackage.module3 import people


module1.greet("123")
module2.depart("456")

for person in people:
    print(person)