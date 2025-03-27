# https://school.programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    m = transfer_scale(m)
    correct_music = False
    for music in musicinfos:
        start, end, name, song = music.split(',')
        time = time_to_minute(end) - time_to_minute(start)
        song = transfer_scale(song)
        real_song = ''
        for minute in range(time):
            real_song += song[minute % len(song)]
        if m in real_song:
            if correct_music and correct_music[1] < time:
                correct_music = [name, time]
            elif not correct_music:
                correct_music = [name, time]

    if correct_music:
        return correct_music[0]
    return '(None)'


def transfer_scale(song):
    trans_song = []
    for scale in song:
        if scale == '#':
            shop_scale = trans_song.pop()
            trans_song.append(chr(ord(shop_scale) + 7))
        else:
            trans_song.append(scale)

    return ''.join(trans_song)


def time_to_minute(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)


solution("ABCDEFG", ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"])
