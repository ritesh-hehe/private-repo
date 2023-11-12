# Modify the previous program such that only the users Alice and Bob are greeted with their names.
'''
print(f"Hi, nice to meet you!" if input('Please enter your name: ') in ['Alice', 'alice', 'Bob', 'bob'] else 'I do not recognize you')
'''
# Dayum that looks ugly...

name = input("Please enter your name: ")
if name in ['Alice', 'alice', 'Bob', 'bob']:
    print(f"Welcome {name}. I hope you are doing well!")
else:
    print(
        f"Dear {name}, this program is meant to be used by Alice and Bob. I apologize for the issue.")
