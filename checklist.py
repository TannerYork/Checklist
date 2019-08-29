checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# Destroy
def destroy(index):
    checklist.pop(index)

def test ():
    create('purple sox')
    create('red cloaks')

    print(read(0))
    print(read(1))

    update(0, 'purple socks')
    destroy(1)

    print(read(0))
    print(read(1))

test()


