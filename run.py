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
        result = ydl.extract_info(urls, download=True)
        fn = f'{result["title"]}-{result["id"]}.mp4'
    return fn

with open('data.json') as f:
    data = json.load(f)
for tourney in data:
    if not os.path.exists(tourney['directory']):
        os.makedirs(tourney['directory'])
    os.chdir(tourney['directory'])
    fn = ytdl(tourney['url'])
    for match in tourney['matches']:
        if not os.path.exists(match[2]):
            cut(fn, match[0], match[1], match[2])
    os.chdir('..')

def dl_all():
    # dl('Topanga League 3A', ['https://www.youtube.com/playlist?list=PLXpdXai2oNiOcdlro6J4luFSRvamw9ctU'])
    # dl('Topanga League 4A', ['https://www.youtube.com/playlist?list=PLXpdXai2oNiO6C0gcPCBxNicfr5Hf3vXA'])
    # dl('Topanga League 4B', ['https://www.youtube.com/playlist?list=PLXpdXai2oNiPAXJ6NG5R96ewlZjKXA4WZ'])
    # dl('Topanga League 5A', ['https://www.youtube.com/playlist?list=PLXpdXai2oNiMn1cCuyKyNdsE1am_4G1y4'])
    # dl('Topanga League 5B', ['https://www.youtube.com/playlist?list=PLXpdXai2oNiOADXSrIW_wDYdB4hKTPtHj'])
    # dl('Topanga World League', ['https://www.youtube.com/playlist?list=PLXpdXai2oNiMVsi9XBcr11U3yoxapC4JP'])
    # dl('Topanga World League 2', ['https://www.youtube.com/playlist?list=PLXpdXai2oNiPqJrbjJOECau_6zWmaGtGG'])
    # dl('Topanga World League 2', [
    #     'https://www.youtube.com/watch?v=7MEsgrytPKs', # R1B2
    #     'https://www.youtube.com/watch?v=pyjWh6RPXSg', # R1B3
    #     'https://www.youtube.com/watch?v=eHo0VZRIZSI', # R1B4
    #     'https://www.youtube.com/watch?v=j_MDIeThVVQ', # R1B6
    # ])
    # dl('Topanga Asia League', ['https://www.youtube.com/playlist?list=PLJGU2inEmVz0yc5ewu8LaDmwE1QNfkso0'])
    # dl('SF Pack - Akuma', [
    #     'https://www.youtube.com/watch?v=4f-af4AuPsU',
    #     'https://www.youtube.com/watch?v=ltM9ylWqFcI',
    #     'https://www.youtube.com/watch?v=sL6wclvP-TY',
    #     'https://www.youtube.com/watch?v=26vnI2xSxkQ',
    #     'https://www.youtube.com/watch?v=7TyaA4D3QZs',
    #     'https://www.youtube.com/watch?v=24a9ZjPGlR0',
    #     'https://www.youtube.com/watch?v=2khoDuN6NII',
    #     'https://www.youtube.com/watch?v=rKasnIAnz8A',
    #     'https://www.youtube.com/watch?v=5kGtZz7_9A8',
    #     'https://www.youtube.com/watch?v=SqiEiHuanWI',
    #     'https://www.youtube.com/watch?v=YAXNKu4sYNE',
    #     'https://www.youtube.com/watch?v=_0ttgvbRyxM',

    #     'https://www.youtube.com/watch?v=9df_RcUjol0',
    #     'https://www.youtube.com/watch?v=HMViGBXOXA0'

    # ])
    # dl('Final Round 18', [
    #     'https://www.youtube.com/playlist?list=PLUc6xMPBhaWPJatAr05IkqGn2u-G720nF',
    #     'https://www.youtube.com/watch?v=W1etj4EOXo4'
    # ])
    # dl('SEAM 2015', [
    #     'https://www.youtube.com/watch?v=D1ZTag0avuE',
    #     'https://www.youtube.com/watch?v=PmXlK5jVAWU',
    #     'https://www.youtube.com/watch?v=Kv4MxalEscU',
    #     'https://www.youtube.com/watch?v=uzAfc_K8HdA',
    #     'https://www.youtube.com/watch?v=KA-p1dBiZiU',
    # ])
    pass

dl_all()



# d = 'SEAM 2015/'
# fin = 'South East Asia Major 2015 pools [part 01]-D1ZTag0avuE.mp4'
# cut(d + fin, '00:10:36', '00:16:50', d + 'Z - Kyouso (Rose) vs. Xiaohu (Rose).mp4')
# cut(d + fin, '00:21:03', '00:25:50', d + 'Z - White Squall (Makoto) vs. Hyde (C. Viper).mp4')
# cut(d + fin, )