from outdated_ami_function import get_old_ami_check,client,csv_create

value= client()
outdated_ami = get_old_ami_check(value)
csv_create(outdated_ami,'oldaminame.csv')
# print(outdated_ami)