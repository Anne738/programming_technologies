import grades_management as gm

data ={ ('8-A','Soroka I.I.'):{'Math':[12, 10, 8, 9],
                         'Ukr literature':[9, 7],
                         'Chemistry':[6, 8, 7],
                         'Physics':[11, 12, 11, 12],
                         'PE':[10, 10, 10, 10]
                         },
        ('8-A','Nikson A.V.'):{'Math':[12, 11, 10, 7],
                         'Ukr literature':[10, 11],
                         'Chemistry':[9, 8, 10],
                         'Physics':[10, 10, 7, 6],
                         'PE':[7, 8, 9, 10]
                         },
       ('5-C','Kozak A.S.'):{'Math':[9, 10, 10, 10],
                         'Ukr literature':[9, 10],
                         'History':[6, 10, 11, 8],
                         'English':[5, 12, 10, 11],
                         'PE':[9, 8, 6, 4]
                         },
       ('5-B','Moliga T.P.'):{'Math':[11, 11, 11, 10],
                         'Ukr literature':[12, 10, 11],
                         'History':[10, 10, 11, 12],
                         'English':[11, 10, 12, 10, 11],
                         'PE':[10, 10, 10, 10]
                         },
       ('5-C','Vinnichenko D.R.'):{'Math':[10, 10, 10, 10],
                         'Ukr literature':[11, 10],
                         'History':[9, 10, 11, 12],
                         'English':[11, 12, 7, 9, 10],
                         'PE':[5, 5, 8, 9]
                         }
}

one_more = ('8-B','Sobchuk A.P.')
k = gm.add_child(data, one_more)
print(data)
print(' ')
print('Amount of children ',k)
print(' ')

k = gm.add_child_subjects(data, one_more, ['Math', 'Ukr literature', 'Chemistry', 'Physics', 'PE'])
print(data)
print(' ')
print('Amount of subjects became ',k)
print(' ')

k = gm.add_child_grades(data, one_more, 'Native language', [12, 10, 11, 8, 5, 12])
print(data)
print(' ')
print('Amount of grades became ',k)
print(' ')

k = gm.add_child_grades(data, one_more, 'Native language', [11, 11])
print(data)
print(' ')
print('Amount of grades became ',k)
print(' ')


child = ('5-C','Vinnichenko D.R.')
subj = 'History'
print('AVG for {0} on {1} is {2}'.format(child, subj, gm.calcucale_avg(data, child, subj)))
print(' ')

child_name = 'Vinnichenko D.R.'
print('{0} stydies at {1} class'.format(child_name, gm.class_by_name(data, child_name)))
print(' ')
child_name = 'Nikson A.V.'
print('{0} stydies at {1} class'.format(child_name, gm.class_by_name(data, child_name)))
print(' ')

print('AVG_ALL for ', child)
print(gm.calcucale_avg_all(data, child))
print(' ')

print(f'Subject(s) whith max grade for {child} is')
print(gm.subject_max_grade(data, child))
print(' ')

print(f'Subject(s) whith min grade for {child} is')
print(gm.subject_min_grade(data, child))
print(' ')

subject = 'Math'
print(f'Subject AVG on {subject} is ')
print(gm.subject_avg(data, subject))
print(' ')

class_name = '5-C'
print(f'{class_name} list of children:')
print(gm.children_list(data, class_name))
print(' ')

print(f'The best student(s) at {subject} is(are):')
print(gm.subject_best_children(data, subject))
print(' ')

print(f'The best student(s) at {subj} is(are):')
print(gm.subject_best_children(data, subj))
print(' ')

subj = 'None'
print(f'The best student(s) at {subj} is(are):')
print(gm.subject_best_children(data, subj))

print(' ')
print('Is {0} excellent student: {1}'.format(child, gm.is_excellent_student(data, child)))
print(' ')
child = ('8-A','Nikson A.V.')
print('Is {0} excellent student: {1}'.format(child, gm.is_excellent_student(data, child)))
print(' ')
child = ('5-B','Moliga T.P.')
print('Is {0} excellent student: {1}'.format(child, gm.is_excellent_student(data, child)))
print(' ')
child = one_more
print('Is {0} excellent student: {1}'.format(child, gm.is_excellent_student(data, child)))

