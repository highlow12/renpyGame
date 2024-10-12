label chapter_13:
    "제목: 최대의 용기"

    scene bg tower in
    play music "bgm/romantic5.mp3"
    "비극적인 삶 그 자체였던 녹스의 과거 이야기."

    "그가 먼저 자신의 이야기를 꺼낸 건 이번이 처음이었다."

    "불현듯, 황실에서 처음으로 그를 마주했던 기억이 떠올랐다."

    "그때는 이렇게나 가까워질 줄은 상상하지도 못했는데."

    s "네 이야기 잘 들었어. "

    s "여기까지 말하는 데에 용기가 필요했던 거지?"

    show char n default def at top
    n "용기는 무슨···."

    s "그냥 너라서 말한 거야."

    show char n default def at top
    n "너라서."

    s "···나라서?"

    show char n default defr at top
    n "어···."

    hide char
    "녹스답지 않게 얼굴이 붉어졌다."

    "그는 자신도 자각하지 못한 채로 말을 꺼내 버린 것 같았다."

    "꼭 나를 특별하게 생각하는 것처럼 느껴졌다."

    "연구 실험체로서의 것 외의 특별함을."

    "그리고, 마치 나를 향한 고백처럼 들리기도 했다."

    s "그래, 알았어."

    show char n default defr at top
    n "뭐가 그래야. 나도 모르는 걸 네가 어떻게 알아."
    
    menu .m0:
        
        "그는 또다시 애처럼 굴기 시작했다."
            
        "네가 나를 특별하게 생각한다는 말이잖아.":
            $ persistant.Likeability['nox'] += 3
            show char n default embr at top
            n "뭐?"
            s "몰랐어?"

            hide char
            "꽤 용기 내서, 내가 느낀 점을 말했지만, 그는 많이 놀란 듯했다."

            "분위기가 어색해진 것 같아, 말을 무마해야 할 것 같았다."

            s "장난 좀 쳐봤어."

            s "나 너무 좋아하지는 말란 말이야."

            s "이렇게 불쑥불쑥 날 소환하지 말고."

            "녹스는 꽤 진지한 표정을 짓고 있으면서도 웃고 있었다."

            "다른 생각을 하는 것 같기도 했다."

            show char n default defr at top
            n "그래, 알았어."

            hide char
            "억지로 만든 분위기를 빨리 깨고 싶었다."

        "사실 잘 모르겠어.":
            $ persistant.Likeability['nox'] += 9
            s "···그러니까 네가 알아봐. 아마 잘 알고 있을 것 같으니까."
            s "그리고 다음에 나한테 알려줘."

            show char n default def at top
            n "자꾸 터무니없는 걸 나한테 원하네."

            s "너도 나한테 그러잖아."

            show char n default smi at top
            n "그래, 알았어. 숙제 열심히 해야겠네."

            hide char
            "녹스는 진지한 듯싶으면서도, 슬며시 웃고 있었다."

            "그 웃음이 처음 만났을 때처럼, 꽤 매혹적으로 느껴졌다."

            "그를 더 쳐다보면 위험할 것 같다고 생각했다."

    s "아무튼 이젠 정말 가야 해. 지금 상황이 별로 안 좋거든."
    show char n default def at top
    n "아, 그거 말이지."

    hide char
    "당황한 듯 시선을 피하는 녹스."

    "매사에 당당함을 유지하던 자만감은 어디로 갔는지, 말을 한참이나 머뭇거렸다."

    s "무슨 문제라도 있는 거야?"

    show char n default def at top
    n "내가 직접 텔레포트로 데려다주고 싶긴 하지만···."

    show char n default def at top
    n "저번에 말했잖아. 내 마법은 너한테 안 통한다고."

    s "아."

    hide char
    "완전히 까먹고 있었다."

    "녹스가 그것 때문에 내게 관심을 두기 시작했던 건데도."

    s "그럼 난 어떻게 해야 해?"

    s "설마 말을 끌고 기사단까지 가야 하는 건가?"

    "말을 타고 가면 적어도 사흘이었다."

    show char n default def at top
    n "걱정하지 마. 마도구는 되잖아."

    show char n default def at top
    n "네가 여기 어떻게 온 줄 잊었어?"

    hide char
    "나는 뒷머리를 긁적거렸다."

    "그는 제 주머니에 손을 넣어 물건 하나를 꺼냈다."

    show char n default def at top
    n "이걸 누군가에게 주게 될 줄은 몰랐는데."

    hide char
    "녹스가 꺼낸 건 마도구였다. "

    "조금 특이한 점이라면, 마탑주가 내어준 것치고는 꽤 초라해 보인다는 것."

    s "이건 뭐야?"

    show char n default def at top
    n "내가 처음으로 만들었던 텔레포트 마도구."

    s "처음으로?"

    show char n default def at top
    n "어."

    show char n default def at top
    n "눈을 뜬 이후로 연구실에 갇혀 살다가, 처음으로 세상 밖을 나와 만든 거야."

    show char n default def at top
    n "그때는 마법만큼 재밌는 게 없었지. "

    show char n default def at top
    n "그게 내게 허락된 유일한 자유이기도 했고."

    show char n default def at top
    n "이건 지금도 마찬가지야."

    s "그럼, 너한테 꽤 소중한 거 아냐?"

    show char n default def at top
    n "됐어. 나한테는 필요도 없고."

    show char n default def at top
    n "네가 갖고 있는 게 더 나아."

    s "흠. 그래?"

    hide char
    "생각해 보면, 그에게 꽤 여러 도움을 받았었다."

    "그런데도 나는 고맙다는 말 한마디도 하지 않았던 것 같다."

    "그의 행동들이 괘씸해서 그랬던 게 컸지만."

    menu .m1:
        "하지만 이제는 그가 딱히 괘씸하지 않았다."
        "웃으며 장난친다.":
            s "그럼, 평생 갖고 있어야겠다."
            show char n default def at top
            n "그러든가."

            hide char
            "생각과는 달리, 그는 덤덤하게 나왔다."

        "고맙다는 말을 전한다.":
            $ persistant.Likeability['nox'] += 9
            s "고마워. 여태 내 힘 신경 써줬던 것도, 지금 이것도."
            show char n default smi at top
            n "알고 있으면, 나한테 잘해줘."

    hide char
    "녹스는 제 특유의 나른한 표정을 지으며 나를 응시했다."
    "나는 그의 표정을 보는 것이 왠지 부끄러워 녹스의 손에 있던 마도구를 가로챘다."

    s "됐고! 난 이제 가볼게."

    show char n default def at top
    n "어. 네가 말해준 대로, 마탑 좀 정리하고 상황 봐서 너한테 갈게."

    show char n default def at top
    n "마탑 일에서 손 뗀지 좀 돼서, 시간은 꽤 걸릴지도 모르겠네."

    show char n default def at top
    n "조심하고."

    hide char
    "녹스의 은근한 걱정은 여전했다."

    "그에게 고마움도 느끼면서, 그가 기특하다는 생각도 들었다."

    "그래서 나도 모르게 손을 뻗어버렸다."

    "그렇게, 나는 녹스의 머리를 쓰다듬었다."

    show char n default embr at top
    n "···!"

    show char n default embr at top
    n "너 뭐 하는···."

    hide char
    "녹스가 놀란 것 같았다. 한편으로는 부끄러워하는 것 같았다."

    "그에게 한 방 먹인 것 같은 기분에 뿌듯하기도 했다."

    s "진짜 안녕. 다음에 봐."

    "그렇게 나는 녹스에게 인사를 건넨 뒤, 마도구를 눌렀다."

    "다음에 그를 볼 때는, 꽤 다른 모습을 마주할 것 같다고 생각했다."

    "마도구는 이전에는 들어본 적 없던 잔잔한 물소리가 울려 퍼지더니,"

    "광활한 빛과 함께 내 위치를 이동시켰다."

    show white at fadeInOut
    scene white

    scene bg camp out night
    play music "bgm/dis.mp3"
    "녹스의 마도구 덕분에 순식간에 기사단에 도착할 수 있었다."

    "황제의 갑작스러운 죽음, 분명 모두 혼란스러워할 것이 분명했다."

    "아니, 분명 그럴 것이라고 생각했다."

    "그래서 걸음을 재촉해서 달려왔건만···."

    s "이 사람들 왜 이렇게 평화로운 거야?"

    "놀라울 정도로 기사단 분위기는 평화로웠다."

    "기사들은 수련하고 있거나, 검을 재단장하고 있었다."

    "나는 기사단의 무리에 다가가 물었다."

    s "너희, 뭐 들은 거 없는 거야?"

    show char knight default at top
    Character('기사') "세, 세레나님! 돌아오셨군요. "

    s "인사치레는 됐고, 너희 왜 이렇게 태평해? 전쟁 끝났다 이거야?"

    show char knight default at top
    Character('기사') "다음 정복 전쟁 명령이 떨어지기 전까지는 쉬라고 하셔서···."

    hide char
    "기사의 말을 듣는 순간, 무언가 잘못되었음을 직감했다."

    "나는 방향을 틀어 전쟁 통솔자가 있는 막사로 향했다."

    s "아직 이들은 황제가 죽었다는 걸 모르는 게 분명해."

    "지휘자가 머무는 막사로 향하는 동안, 머릿속에는 수많은 생각들이 뒤엉켰다. "

    "만약 내가 황실에 복귀한다면, 후계자의 자리를 두고 벌어질 문제를 막기 위해 이 소식을 전하지 않은 것일까."

    "헤안이 아니었다면, 나는 황제가 죽었다는 것조차 알지 못했을 게 분명했다."

    s "그들이 나를 의도적으로 배제한 거야···."

    "생각 이상으로 황실은 치밀했다."

    "황제의 죽음을 내가 속한 기사단에 전령으로 보내지 않은 황실의 태도와 의도가"

    "정말 역겨웠다."

    "그리고 두려워졌다."

    s "설마, 사생아인 나를 의식하고 이런 일을 벌이는 건가."

    scene bg camp in
    "그렇게 복잡한 생각을 하다 보니, 금세 막사에 도착했다."

    "나는 망설임 없이 그곳에 들어갔다."

    s "지휘관 있습니까?"

    show char commander at top
    Character('지휘관') "누가, 허락도 없이 내 막사에 들어와?"

    show char commander at top
    Character('지휘관') "세레나님?"

    s "급한 일이라 실례했습니다."

    show char commander at top
    Character('지휘관') "실언했습니다. 다만 어쩐 일로 오신 겁니까?"

    hide char
    "묘하게 나를 적대하는 듯한 그의 태도가 여과 없이 느껴졌다."

    "하지만, 여기서 그의 태도를 지적해 봤자 크게 달라질 것 같지 않았다."

    "나는 애써 그를 무시한 채 지휘관이 안내하는 경로를 따라 자리에 앉았다."

    s "중요한 이야기를 나누고 싶습니다."

    show char commander at top
    Character('지휘관') "어떤 말씀이신 겁니까?"

    hide char
    "나는 깊은숨을 들이쉬고 말했다."

    s "황제의 서거 소식이 아직 기사단에 전해지지 않았다는 것을 알게 되었습니다."

    s "이런 중요한 소식이 왜 저희에게 전해지지 않은 건가요?"

    "지휘관은 당황한 표정을 짓더니, 이내 말을 이었다."

    show char commander at top
    Character('지휘관') "저 역시, 그 소식을 들은 건 얼마 되지 않았습니다."

    show char commander at top
    Character('지휘관') "하지만 이제라도 알면 된 것 아닙니까?"

    hide char
    "황제의 사람이었기에 나를 좋아하지 않는 것 정도는 눈치채고 있었다."

    "하지만, 이렇게까지 노골적인 태도를 보인 적은 없었다."

    "그의 태도가 바뀐 건 황제의 죽음과 연관이 있는 걸까?"

    s "그게 무슨 뜻인 거죠?"

    show char commander at top
    Character('지휘관') "우리 기사단에 소식이 늦게 전달된 데는 이유가 있을 거라고 생각합니다."

    show char commander at top
    Character('지휘관') "소식통이 늦어진 걸 수도 있고, 아님 뭐···."

    show char commander at top
    Character('지휘관') "아닙니다. 아무튼 다른 소식이 전해지면 바로 전달해 드리도록 하겠습니다."

    s "지휘관, 지금 생각해야 할 건 어째서 우리 기사단에만 그 소식이 전달되지 않았던 거냐는 겁니다."

    s "이곳은 제국의 기사단장인 제가 있는 기사단인 데도요."

    s "어쩌면 제게 의도적으로 전달하지 않은 것일 수도 있지 않습니까?"

    hide char
    "나는 단호한 표정을 지으며 지휘관을 응시했다."

    "그보다 내 서열이 높다곤 하지만, 그건 어디까지나 보여주기식일 뿐."

    "실제로는 일개 지휘관보다 권력이 없는 것이 내 자리의 실체였다."

    "지휘관은 멈칫거리더니, 이내 조심스럽게 입을 열었다."

    show char commander at top
    Character('지휘관') "세레나님께서 과대 해석을 하시는 건 아닐지···.
"

    show char commander at top
    Character('지휘관') "그리고 제게 따지셔봤자 해결되는 건 없습니다. 저도 단장님처럼 아는 게 없거든요."

    s "······."

    hide char
    "이곳에 오면 내 의문이 조금이라도 해결될 줄 알았는데."

    "오히려 머릿속만 복잡해질 뿐이었다."

    "나는 허탈한 마음을 감추지 못하고, 한숨을 내쉬었다."

    s "하아···."

    show char commander at top
    Character('지휘관') "죄송합니다. 도움이 되지 못한 것 같군요."

    s "저는 이만 자리에서 일어나겠습니다."

    show char commander at top
    Character('지휘관') "조심히 들어가시길 바랍니다. 밤은 위험하니까요."

    s "충고 감사합니다."

    scene bg camp out night
    play music "bgm/comfort7.mp3"
    hide char
    "황제 서거 소식이 전해지지 않는 이유는 알아내지 못했다."

    "하지만 한 가지 확실한 건, 황실 소속인 지휘관이 내게 노골적인 태도를 보이고 있다는 것이다."

    "이상할 정도로 타이밍이 절묘했다."

    "일단 생각을 정리할 시간이 필요했다. "

    "나는 내 막사로 향하는 길로 방향을 꺾었다."

    s "이곳도 참 오랜만에 오네."

    "그때 내 막사 앞에서 익숙한 인영이 보였다."
    show char e default def
    play music "bgm/ereon3.mp3"
    "에런 스노우, 내 스승님이었다."

    s "스승님께서 대체 왜 여기 계신 거지···?"

    menu .m2:
        "당황스러운 마음을 감춘 채 나는 스승님께 말을 걸었다."
            
        "에런 스승님?":
            $ persistant.Likeability['eren'] += 5
            show char e default emb at top
            e "세레나?"
            s "오랜만에 뵙네요. 그동안 잘 지내셨습니까?"

            show char e default smi at top
            e "나야 잘 지냈지. 다만, 세레나가 돌아왔다고 하길래 얼굴 볼 겸 들렸어."

            s "제 얼굴을 왜···."

            show char e default smi at top
            e "그동안 고생하지 않을까 싶어서. 막사 안에 들어가서 얘기할까?"

            s "···네."

            show char e default smi at top
        "스승님께서 제 막사 앞에는 왜 계시는 거죠?":
            $ persistant.Likeability['eren'] += 2
            e "세레나 네가 걱정되어서 계속 기다리고 있었어."
            show char e default smi at top
            e "그런데 공작가에서 돌아왔다는 소식을 듣고, 바로 달려왔지."

            s "···굳이 오실 필요는 없었던 것 같습니다."

            s "저는 이미 제 할 일만으로도 벅차서요."

            show char e default des at top
            e "세레나 부디 나에게 선을 긋지 말아줘."

            show char e default des at top
            e "네가 그렇게 말하면 나는 어떻게 말해야 할지 모르겠어."

            s "······."

            hide char
            "처음 보는 스승님의 표정이었다."

            "저 표정은 마치, 제 연인을 한껏 그리워하다 못해 사무친 표정."

            show char e default smi at top
            e "막사 안에서 대화하자. 오래 서 있으면 다리 아플 거야."

    hide char
    "막사 안으로는 그 누구도 초대하고 싶지 않았지만···."
    "스승님의 얼굴을 보니 차마 거절할 수 없었다."

    "게다가 저렇게 다정하게 말씀하시면, 나에겐 거부할 수 있는 선택권 따위 있을 리가."

    show char e default smi at top
    scene bg camp in
    e "이렇게 대화하는 것도 참 오랜만이구나."

    show char e default smi at top
    e "네가 공작가에 가기 위해 기사단을 떠난 이후로, 정식으로 만나는 건 지금이 처음이니까."

    s "제가 공작가로 간 건 어떻게 아신 겁니까?"

    show char e default def at top
    e "헤안과 함께 사라진 걸 봤다. 그래서 대충 추측할 수 있었지."

    s "그렇군요··· 그동안 어떻게 지내셨습니까?"

    show char e default def at top
    e "기사단의 일을 수습하는 것만으로도 벅찼다. 제국의 공격 이후로, 보급품은 제대로 지급되지 않아서 "

    show char e default def at top
    e "여러모로 골머리를 앓았지."

    hide char
    "내가 없는 동안 기사단이 잘 유지될 수 있었던 건, 전부 스승님 덕분이었구나."

    "하지만···."

    s "죄송하지만, 제가 돌아온 지 얼마 안 되어서 컨디션이 좋지 않네요. 대화는 이쯤이면 될 것 같습니다."

    show char e default def at top
    e "하긴, 세레나 너도 피곤하겠지."

    s "용건이 없으시다면 이만 돌아가 주세요."

    hide char
    "사실 맘껏 어리광 부리고 싶었다."

    "힘들었다고, 포기하고 싶었던 순간 역시 수없이 많았다고."

    "그리고, 그 무엇보다 보고 싶었다고."

    "나는 전할 수 없는 말들을 겨우 삼키며 마음에도 없는 말을 내뱉었다."

    s "앞으로 하실 말씀이 있다면, 사람을 통해 전해주세요."

    s "그것이 서로에게 더 효율적인 겁니다."

    "여기서 더 가까워지면, 내가 스승님께 기대하게 되어버리고 만다."

    "지금 이렇게 찾아와준 것도 단지 제자로서 내가 걱정돼서일 텐데···."

    "단지 그뿐일 텐데."

    show char e default def at top
    e "세레나."

    s "네, 스승님."

    show char e default def at top
    e "요새 잠은 잘 자는 거니?"

    s "못 자지는 않습니다. 걱정하실 정도는 아니에요."

    show char e default def at top
    e "내가 잠 못 잘 때, 먹던 수면제가 있어서 챙겨왔어. 잠이 오지 않으면 챙겨 먹도록 해."

    s "이런 건 괜찮습니다. 다시 가져가 주세요."

    show char e default def at top
    e "아니야. 난 이미 많이 있어서. 받아줬으면 좋겠어."

    hide char
    "한사코 거절해도 스승님은 고집을 꺾지 않았다."

    s "일단 돌아가 주세요. 제가 지금 컨디션이 좋지 않아서요. 죄송합니다."

    show char e default def at top
    e "세레나."

    s "네, 스승님."

    show char e default def at top
    e "···힘들면 언제든지 기대도 된다. 나는 언제나 네 편이니까."

    hide char
    "다정한 말투와 온화한 미소."

    "내가 알던 스승님, 에런 스노우의 모습이었다."

    "내가 좋아하는··· 내 스승님."

    s "감사합니다. 힘든 일이 생기면 말씀드리죠."

    s "이젠 진짜 가주세요. 눕고 싶어요."

    show char e default smi at top
    e "여긴 너의 막사니, 편한 대로 하도록 해."

    hide char
    "나는 스승님을 뒤로한 채 침대에 누웠다."

    "하지만, 그분의 얼굴을 마주하기 싫어 고개를 돌렸다."

    "이쯤 되면 스승님께서 돌아갈 것이라고 생각했는데···."

    "어떤 이유에선지 스승님께서는 여전히 그 자리에 머물고 계셨다."

    s "안 돌아가십니까?"

    show char e default def at top
    e "네가 자는 것만 보고 갈게."

    show char e default des at top
    e "그것만은 부디 허락해 주면 안 될까?"

    s "···마음대로 하세요."

    hide char
    "더는 물러날 것 같지 않은 모습에, 내가 물러서 주기로 했다."

    "나는 천천히 눈을 감았다."

    "스승님은 침대 끝에 앉았는지 그 끝에 인기척이 느껴졌다."

    "잘 때까지 안 나가실 생각이 분명했다."

    "나는 스승님이 나가시기 전까지 어떻게든 정신을 부여잡으려고 했지만,"

    scene black
    "오래도록 누적된 몸의 피로도를 이기는 건 무리였던 것 같다."

    "그렇게 나는, 잠에 들었다."

    
    scene bg camp in
    show char e default def at top
    e "······."

    hide char
    "에런은 곤히 잠에 든 세레나를 무표정으로 응시했다."

    show char e default def at top
    e "너에 관해선 다 알고 있다고 생각했는데···."

    show char e default def at top
    e "난 아직 아무것도 모르는 것 같구나."

    hide char
    "에런은 조용히 손을 뻗어 세레나의 머리를 쓰다듬었다."

    "마치 작은 아기라도 만지는 듯 그의 손길은 조심스러웠다."

    show char e default smi at top
    e "보고 싶었어, 세레나."

    hide char
    "에런은 세레나의 머리끝을 잡아 그곳에 입을 맞췄다."

    "그것은 에런이 세레나에게 할 수 있는 최대의 용기였다."

    $ persistent.ClaerChapter = max(14,persistent.ClaerChapter)
    return
