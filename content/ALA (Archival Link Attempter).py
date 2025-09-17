import os



'''
A function that opens a folder.
'''
def open_folder (folder_name):
    blog_entry_folders = []
    non_blog_entry_folders = []
    if os.path.isdir(folder_name):
        print("the folder name is correct")
        print("FOLDERS:")
        for folder in os.listdir(folder_name):
            print(folder)
            if (folder[0] == '2' and folder[1] == '0'):
                folder = ''.join(folder)
                'to turn it from a list of chars into a string'
                blog_entry_folders.append(folder)
            else:
                non_blog_entry_folders.append(folder)
    else:
        print("the folder name is incorrect or there's some other problem")
    print("EXCLUDED FOLDERS:")
    print(non_blog_entry_folders)
    
    return blog_entry_folders

    

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
    number_of_blog_entries = 0
    blog_entries = []
    'a list of all folders inside blog'
    blog_folder = "blog"
    '''
    if the name of the folder where the blog materials are kept is ever changed,
    this string too will have to be changed.
    '''
    blog_entries = open_folder(blog_folder)
    print("ALL BLOG FOLDERS:")
    print(blog_entries)
    number_of_blog_entries = len(blog_entries)
    print("NUMBER OF BLOG ENTRIES:")
    print(number_of_blog_entries)



main()
