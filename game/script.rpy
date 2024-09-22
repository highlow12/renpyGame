
# 스크립트 주소: https://drive.google.com/drive/folders/15qKpp3tOqMbnlgXqVcoKP79p84-P8uoU?usp=drive_link

# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image black = '#000'
image white_bg = '#fff'
image red = Image("gui/fade_outline_red.png")
image white = Image("gui/fade_outline_white.png")
#image serena = Image("serena.png", oversample= 2)
#image adrian = Image('adrian.png', oversample= 2)

# 게임에서 사용할 캐릭터를 정의합니다.

define q = Character('???')

define s = Character('세레나', color="#3D5265")

define a = Character('아드리안', color="#f3dd1b")
define n = Character('녹스', color="#c197c7")
define h = Character('헤안', color="#05163a")
define e = Character('에런', color="#800808")

define Q = Character('황후')
define K = Character('에프탈 제국 황제')

define R = Character('로더릭 단장')
define H = Character('힐다')
define T = Character('타나')
define v1 = Character('마을주민 1')
define v2 = Character('마을주민 2')
define v3 = Character('마을주민 3')

define shake = vpunch

default persistent.ClaerChapter = 0

transform fadeInOut:
    alpha 0.0
    linear 0.5 alpha 1.0
    pause 0.0
    linear 0.5 alpha 0.0
    alpha 0.0


