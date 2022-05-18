class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link

def read_videos():
    number_video = int(input("number video:"))
    list_video = []
    for i in range(number_video):
        print("_________Enter video "+ str(i + 1) + "_________")
        title = input("enter title:")
        link = input("enter link:")
        video = Video(title, link)
        list_video.append(video)
    return list_video

def print_videos(videos):
    print("______________ read videos ______________")
    for i in range(len(videos)):
        print("_________data "+ str(i + 1) + "_________")
        print("video title:" + videos[i].title)
        print("video url:" + videos[i].link)

def write(video, f):
    f.write(video.title + "\n")
    f.write(video.link + "\n")
def write_videos(videos):
    with open("practive.txt", "w") as f:
        f.write(str(len(videos)) + "\n")
        for i in videos:
            write(i, f)

def read_video_txt(f):
    title = f.readline().replace("\n", "")
    link = f.readline().replace("\n", "")
    return Video(title, link)
def read_videos_txt():
    videos = []
    with open("practive.txt", "r") as f:
        number_videos = f.readline()     
        videos_txt = []
        for i in range(int(number_videos)):
            videos = read_video_txt(f)
            videos_txt.append(videos)
    return videos_txt

def main():
    
    videos = read_videos()
    write_videos(videos)
    read_videos_txt1 = read_videos_txt()
    print_videos(read_videos_txt1)



main()  