sample_list=['cook','wash','iron']
for task in sample_list:
    print(f'The task at hand is to {task}')

sample_list.append('mop')
print(sample_list)

sample_list.pop(1)
print(sample_list)

print("\nYour Tasks:")         
for index ,task in enumerate(sample_list,start=1):
    print(f'{index}.{task}')

show_tasks=[f'\n{index}:{task}' for index ,task in enumerate (sample_list,start=1)]
print(show_tasks)