from pytube import YouTube

# Directory to save the downloaded files
D_F = "/storage/emulated/Zender/files"

# Input the URL of the YouTube video
url = input('Enter URL: ')

# Create a YouTube object
vid = YouTube(url)

# Get the title of the video
vd_name = vid.title
print("Title:", vd_name)

# Get all available video streams
vd_qt = vid.streams.all()
vd_lt = list(enumerate(vd_qt))

# Print available video streams
print("Available video streams:")
for i in vd_lt:
    print(i)

# Choose the video quality to download
video = int(input('Enter the number corresponding to the desired video quality: '))

# Download the selected video stream
vd_qt[video].download(output_path=D_F)
print('Download successful')