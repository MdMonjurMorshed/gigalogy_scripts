from contextlib import contextmanager


@contextmanager
def fileOpener(path,mode):\

"""
{<value>:<fill><align><width>}
:.^50
after colon fill then align like left(<) or right(>) or all(^)
width in pixel size like (50)
"""
    print(f"{f'[{path}]':.^50}")
    file = open(path,mode)
    try:
        print('file open')
        yield file
    finally:
        f.close()



path = '/home/morshed/Documents/personal_user.txt'

with fileOpener(path,'w') as f:
    
    f.write('some thing writter in the file')