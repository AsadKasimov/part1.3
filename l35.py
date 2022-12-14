try:
    num = 100 / 0
except ZeroDivisionError:
    num = 0
except TypeError:
    num = 1
# узнал про как делать так ятобы код работал даже если у какой то части будут ошибки о которых
# вы предпологаете
