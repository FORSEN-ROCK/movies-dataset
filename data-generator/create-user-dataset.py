import random


LAST_NAMES = [
    'Bob',
    'Jim',
    'Holdon',
    'Pole',
    'Steve',
    'Alex',
    'Jony',
    'Elton',
    'Ozzy'
]

FIRST_NAMES = [
    'Marilyn',
    'Manson',
    'Smith',
    'Jon',
    'Gibson',
    'Martin',
    'Jackson',
    'Davis',
    'Williams'
]

def load_user_ids(filename=r'./../dataset/ratings.csv'):
    """This function takes onu unnessosery argument filename
        Returns list of user_id
    """

    file = open(filename, 'r')
    user_ids = set()

    for record in file:
        parts = record.split(',')

        if (len(parts) > 0 and parts[0] != 'userId'):
            user_ids.add(parts[0])

    file.close()

    return user_ids
    
def create_user_dataset(user_ids, filename=r'./../dataset/users.csv'):
    """This function creates user dataset
       It takes set of user ids 
       Returns nothink
    """

    file = open(filename, 'w')
    user_template = '%s,%s,%s@example.com,%s,%s,,123\n'
    users = []

    ## It needs definitions of tabel field in the first line
    file.write('userId,login,email,firstName,lastName,dirthdate,password\n')
    
    for user_id in user_ids:
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        fullname = first_name + last_name

        record = user_template %(user_id, fullname, fullname, first_name, last_name)

        file.write(record)

    file.close()

def main():
   user_ids = load_user_ids()
   create_user_dataset(user_ids)
   
if __name__ == '__main__':
    main()