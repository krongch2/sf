import os
import youtube_dl
import re
import json

def tt(s):
    # convert time string, e.g. '01:43:59', to seconds
    m = re.search('(\d\d)\:(\d\d):(\d\d)', s)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))

def cut(fin, t1, t2, fout):
    d = {'input': fin, 'start': tt(t1), 'duration': tt(t2) - tt(t1), 'output': fout}
    os.system('ffmpeg -y -i "{input}" -vcodec copy -acodec copy -ss {start} -t {duration} "{output}"'.format(**d))

def ytdl(urls):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'playliststart': 1,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(urls, download=False)
        fn = f'{result["title"]}-{result["id"]}.mp4'
        print(urls)
        ydl.download(urls)
    return fn

with open('data.json') as f:
    data = json.load(f)
for tourney in data:
    if tourney['directory'] != 'Topanga World League 2':
        continue
    if not os.path.exists(tourney['directory']):
        os.makedirs(tourney['directory'])
    os.chdir(tourney['directory'])
    fn = ytdl(tourney['url'])
    for match in tourney['matches']:
        if not os.path.exists(match[2]):
            cut(fn, match[0], match[1], match[2])
    os.chdir('..')

def dl_all():
    # dl('Final Round 18', [
    #     'https://www.youtube.com/playlist?list=PLUc6xMPBhaWPJatAr05IkqGn2u-G720nF',
    #     'https://www.youtube.com/watch?v=W1etj4EOXo4'
    # ])
    pass

dl_all()
