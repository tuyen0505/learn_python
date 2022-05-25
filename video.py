# import
import subprocess as sp
import time

# atributions class:
class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link

class Playlist(Video):
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos
        
# create video
def create_videos():
    number_video = int(input("number video:"))
    list_video = []
    for i in range(number_video):
        print("_________Enter video "+ str(i + 1) + "_________")
        title = input("enter title:")
        link = input("enter link:")
        video = Video(title, link)
        list_video.append(video)
    return list_video

# output video
def print_videos(videos):
    print("______________ read videos ______________")
    for i in range(len(videos)):
        print("_________data "+ str(i + 1) + "_________")
        print("video title:" + videos[i].title)
        print("video url:" + videos[i].link)

# write the video
def write(video, f):
    f.write(video.title + "\n")
    f.write(video.link + "\n")

def write_videos(videos, f):
    f.write(str(len(videos)) + "\n")
    for i in videos:
        write(i, f)

#read_video_txt
def read_video_txt(f):
    title = f.readline().replace("\n", "")
    link = f.readline().replace("\n", "")
    return Video(title, link)

def read_videos_txt(f):
    number_videos = f.readline()     
    videos_txt = []
    for i in range(int(number_videos)):
        videos = read_video_txt(f)
        videos_txt.append(videos)
    return videos_txt

# create playlist:
def create_playlist():
    list_playists = []
    number_playlist = int(input("enter the number of playlists: "))
    for i in range(number_playlist):
        name = input("enter name:")
        description = input("enter description:")
        rating = input("enter rating (1-5):")
        videos = create_videos()
        playlist = Playlist(name, description, rating, videos)
        list_playists.append(playlist)
    return list_playists
# write playlists:

def write_playlist(playlist, f):
   
        f.write(playlist.name + "\n")
        f.write(playlist.description + "\n")
        f.write(str(playlist.rating) + "\n")
        write_videos(playlist.videos, f)

def write_playlists(playlists):
    with open("video.txt", "w") as f:
        f.write(str(len(playlists)) + "\n")
        for i in range(len(playlists)):
            write_playlist(playlists[i], f)

# read playlist:
def read_playlist_txt():
    list_playlists = []
    with open("video.txt", "r") as f:
        number_playlist = f.readline()
        for i in range(int(number_playlist)):
            name = f.readline().replace("\n", "")
            description = f.readline().replace("\n", "")
            rating = f.readline().replace("\n", "")
            videos = read_videos_txt(f)
            playlist = Playlist(name, description, rating, videos)
            list_playlists.append(playlist)
    return list_playlists

# print playlist:

def print_playlist(playlist):
    print("print name playlist:" + playlist.name)
    print("print descripton playlist:" + playlist.description)
    print("print rating playlist:" + playlist.rating)
    print_videos(playlist.videos)

def print_playlists(playlists):
    for i in range(len(playlists)):
        print("____________ playlist " + str(i + 1) + "___________" )
        print_playlist(playlists[i])

# play a playlist:
def print_list_playlists(playlists):
    print(f"__selection index of playlist (1, {len(playlists)})___")
    for i in range(len(playlists)):
        print(f"playlist {i + 1}: {playlists[i].name}")
    return selestion_a_range("selection playlists of you: ", 1, len(playlists))

def print_videos_playlists(videos):
    print(f"___selection index of videos (1, {len(videos)})___")
    for i in range(len(videos)):
        print(f"video {i + 1}: {videos[i].title}")
    return selestion_a_range("enter idx videos: ", 1, len(videos))

def play_a_playlist(link):
    print(link)
    chill = sp.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", link])

# show menu:
def show_menu():
        print("________________________________")
        print("Opption 1: Create playlist")
        print("Opption 2: Show playlist")
        print("Opption 3: Play a playlist")
        print("Opption 4: Add a playlist")
        print("Opption 5: Update playlist")
        print("Opption 6: Delete playlist")
        print("Opption 7: save and exit playlist")
        print("_________________________________")    

# selection in range:
def selestion_a_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    return int(choice)


def main():

    while True:

        try :
            playlists = read_playlist_txt()
            print("Loaded Data Successfully !!!!")
        except :
            print("playlists none!")
        
        show_menu()

        selection = selestion_a_range("enter selestion a range (1, 7): ", 1, 7)

        if selection == 1:
            playlists = create_playlist()
            write_playlists(playlists)
        elif selection == 2:
            print_playlists(playlists)
            time.sleep(10)
        elif selection == 3:
            idx_playlist = print_list_playlists(playlists) - 1
            idx_videos = print_videos_playlists(playlists[idx_playlist].videos) - 1
            play_a_playlist(playlists[idx_playlist].videos[idx_videos].link)
        # elif selection == 4:
        #     add_a_playlist()
        # elif selection == 5:
        #     update_playlist()
        # elif selection == 6:
        #     delete_playlist()
        elif selection == 7:
            print("successfully write add playlist!")
            break
        else :
            print("wrong input, exit")
            break


main()  