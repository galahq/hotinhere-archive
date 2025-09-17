import os



'''
A function that opens a folder.
'''
def open_folder (folder_name):
    blog_entry_folders = []
    if os.path.isdir(folder_name):
        print("the folder name is correct")
        print("folders:")
        for folder in os.listdir(folder_name):
            print(folder)
            blog_entry_folders += folder
    else:
        print("the folder name is incorrect or there's some other problem")

    return 

    

'''

'''
'''
def read_file ():
    with open("")
'''


'''
A function which drives the program.
'''
def main ():
    blog_entries = []
    'a list of all folders inside blog'
    blog_folder = "blog"
    '''
    if the name of the folder where the blog materials are kept is ever changed,
    this string too will have to be changed.
    '''
    blog_entries = open_folder(blog_folder)
    print("ALL BLOG FOLDERS")
    print(blog_entries)
