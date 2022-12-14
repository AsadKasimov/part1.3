from classes.cl40 import Person, Employee

person = Person('Katy', 30)
person.age = 35
person.print_info()


employee = Employee('Nick', 30)
employee.print_info()
employee.more_info()

# наследование это когда есть класс родитель у него там обьекты у них параметры и нам надо скопировать
# их. можно скопировать дедовским методом можно просто в скобках наследника указать родителя