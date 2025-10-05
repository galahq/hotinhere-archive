import os
from urllib import request, error
import socket



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
A function that accesses the contents of a blog post file.
'''
def read_file (blog_post):
    with open("blog/" + blog_post + "/index.md", encoding = "utf-8") as blog_content:
        blog_content = blog_content.read()

    return blog_content



'''
A function that reads through the contents of a blog post file, checks for
links, and then collects them.
'''
def check_for_links (blog_entries):
    is_tracking_a_link = False
    '''
    used to determine whether a link is currently being recorded while iterating
    through every character in a blog post
    '''
    links = []
    new_link = ""
    entry = ""
    entry_content = ""
    danger_zone = 0
    '''
    used to stop the first if statement in the while loop from looking past the
    end and getting an out of index error
    '''
    blog_post_length = 0
    character_value = 0
    '''
    used for acessing each successive character in the blog entry content to
    check if a word starts with http or https
    '''
    for entry in blog_entries:
        'iterates through every blog entry in the registry'
        character_value = 0
        entry_content = read_file(entry)
        blog_post_length = len(entry_content)
        danger_zone = blog_post_length - 4
        while character_value < blog_post_length:
            'iterates through every character in a blog post'
            if (character_value <= danger_zone and entry_content[character_value] == 'h' and entry_content[character_value + 1] == 't' and entry_content[character_value + 2] == 't' and entry_content[character_value + 3] == 'p'):
                is_tracking_a_link = True
                'checks for a fragment beginning with http and raises a flag'
            if (is_tracking_a_link == True and entry_content[character_value] != ']' and entry_content[character_value] != ')' and entry_content[character_value] != ' ' and entry_content[character_value] != '"' and entry_content[character_value] != "\n"):
                new_link += entry_content[character_value]
                '''
                checks for the http flag and records the content as part of a
                new link, also checks the character isnt a link-ending
                character, preventing the link-ending character from being
                recorded with the link before the flag is lowered
                '''
            if (is_tracking_a_link == True and (entry_content[character_value] == ']' or entry_content[character_value] == ')' or entry_content[character_value] == ' ' or entry_content[character_value] == '"' or entry_content[character_value] == "\n")):
                is_tracking_a_link = False
                links.append(new_link)
                new_link = ""
                '''
                lowers the flag when a link-ending character is reached, also
                checks that the flag is actually raised to avoid entering blank
                links whenever theres a link-ending character in the text that
                isnt denoting the end of a link
                '''
            character_value += 1

    return links



'''
A function which strips punctuation should it apear at the end of a link.
'''
def punctuation_stripper (link_list):
    link_length = 0
    link_last_index_position = 0
    for link in link_list:
        link_length = len(link)
        link_last_index_position = link_length - 1
        if (link[link_last_index_position] == '!' or link[link_last_index_position] == ';' or link[link_last_index_position] == ':' or link[link_last_index_position] == ',' or link[link_last_index_position] == '.' or link[link_last_index_position] == '?'):
            link = link[0:-1]
    return link_list



'''
A function which tries all of the collected links in a list.
'''
def try_links (link_list):
    link_list = punctuation_stripper (link_list)
    number_of_successes = 0
    number_of_links = 0
    for link in link_list:
        print(link)
        totally_a_human = request.Request(
            link,
            headers = {"User-Agent": "Mozilla/5.0"}
            )
        '''
        makes the link access seem more human to cut down on the number of
        403s
        '''
        try:
            number_of_links += 1
            with request.urlopen(totally_a_human, timeout = 45):
                number_of_successes += 1
                print("Success")
        except error.HTTPError as error_code:
            if error_code.code == 404:
                print("Error 404, the page no longer exists")
            elif error_code.code == 301:
                print("Error 301, the page has been moved permanently")
            elif error_code.code == 307:
                print("Error 307, the page has a temporary redirect")
            elif error_code.code == 308:
                print("Error 308, the page has a permanent redirect")
            elif error_code.code == 400:
                print("Error 400, bad request")
            elif error_code.code == 401:
                print("Error 401, unauthorized")
            elif error_code.code == 402:
                print("Error 402, payment required")
            elif error_code.code == 403:
                print("Error 403, forbidden-- could be paywalled, auto-redirect, or they know you're a bot")
            elif error_code.code == 408:
                print("Error 408, the request took too long")
            else:
                print("Http error")
        except error.URLError:
            print("Url error, page is inaccessable without a redirect")
        except ConnectionResetError:
            print("Connection terminated by the website, they don't want you poking around here")
        except socket.timeout:
            print("Timed out")
        except Exception:
            print("unusual error, could be an improperly formatted link")

        print("Successes:", number_of_successes)
        print("Links tried:", number_of_links)

    return 0



'''
A function which drives the program.
'''
def main ():
    list_of_all_links = []
    number_of_links = 0
    number_of_blog_entries = 0
    blog_entries = []
    'a list of all folders inside blog'
    blog_folder = "blog"
    '''
    if the name of the folder where the blog materials are kept is ever changed,
    this string too will have to be changed
    '''
    blog_entries = open_folder(blog_folder)
    print("ALL BLOG FOLDERS:")
    print(blog_entries)
    number_of_blog_entries = len(blog_entries)
    print("NUMBER OF BLOG ENTRIES:")
    print(number_of_blog_entries)
    list_of_all_links = check_for_links(blog_entries)
    number_of_links = len(list_of_all_links)
    print("ALL", number_of_links, "LINKS:")
    print(list_of_all_links)
    try_links(list_of_all_links)
    print("DONE")



main()
