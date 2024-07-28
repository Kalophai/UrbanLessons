immutable_var = (1, True, 0.5, 'Hello')
print(immutable_var)
#immutable_var[0] = 999
#Кортеж нельзя изменить. При попытке выдает ошибку об отсутствии поддержки обращения к элементам.
muttable_list = [1, True, 0.5, 'Hello']
muttable_list[1] = False
print(muttable_list)