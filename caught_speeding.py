speed=40
is_birthday=False
if speed<31 or is_birthday and speed<36:
    print('no ticket')
elif speed>30 and speed<51 or is_birthday and speed>35 and speed<56:
    print('small ticket')
else:
    print('big ticket')

