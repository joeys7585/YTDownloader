from pytube import YouTube
from pytube.cli import on_progress

#input link
print('Enter the URL of the video')
link = input()

#link to the API
yt = YouTube(link,on_progress_callback=on_progress)

#progressandconfirm
def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('|{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

#Extract and display information
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length)


#download
down = yt.streams.get_highest_resolution()

down.download('/Users/josephs/Code/Videos')





