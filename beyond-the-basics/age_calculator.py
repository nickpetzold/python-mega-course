from datetime import datetime

delta = datetime.now() - datetime(1989, 11, 24)
print(f'You are {delta.days} days old!')
# print(f'You are {delta.months} months old!')
print(f'You are {delta.days/365} years old!')
