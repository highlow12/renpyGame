﻿label chapter_11:
    scene black
    "제목 : 혼란의 씨앗"

    play music "bgm/ptsd2.mp3"
    "황제가 서거하였다."

    scene black
    "그것이 전보의 내용이었다. "

    "나는 헤안과 함께 곧바로 공작의 집무실로 향했다."

    
    scene bg noble work
    show char hf default at top
    Character('레이워스 공작') "헤안에게 소식을 들으신 모양입니다, 황녀님."

    s "네···. 그렇습니다."

    show char hf default at top
    Character('레이워스 공작') "이미 눈치를 채셨을지 모르겠지만, 황제가 죽은 것 자체는 시간이 꽤 된 것 같습니다."

    show char hf default at top
    Character('레이워스 공작') "무슨 이유에선지는 모르겠지만 황실은 공작가를 끌어내고, 전쟁을 지속시키기 위해 이 사실을 숨겨왔던 모양입니다."

    hide char
    "최근 황실의 급한 행보들은 모두 황제의 죽음이 알려지기 전에 처리해야 할 것이었다."

    "그래야만, 정당성이 부여되는 일들이었으니까. 흩어져있던 퍼즐 조각이 하나둘씩 맞는 기분이었다."

    "황제는 이용당했다. 아마도 타살당했을 가능성이 높았다."

    "그럼, 그동안 있었던 전쟁은 황제의 짓이 아니었던 걸까? 그도 나처럼 꼭두각시인 채로 이용당했던 걸까."

    s "황제는 지금껏 누군가에게 이용 당해왔던 걸까요?"

    show char hf default at top
    Character('레이워스 공작') "그건 아닐 겁니다. 황제가 배신당했을 확률이 높습니다."

    show char hf default at top
    Character('레이워스 공작') "그가 이용당하거나, 연약한 성정은 아니니까요."

    hide char
    "공작의 말이 맞았다. 황제는 피해자보다는 가해자가 어울리는 사람이었다."

    menu .m0:
        "그렇다면, 황제를 시해한 범인은···"
        "'황후' 일 것이라고 추측한다.":
            s "그렇네요. 그럼, 황후가 황제를 배신한 거겠군요."
            show char hf default at top
            Character('레이워스 공작') "아니요. 그럴 리는 없을 겁니다."

            show char hf default at top
            Character('레이워스 공작') "제국민 모두가 알다시피, 황후의 황제 사랑은 유명한 이야기니까요."

            show char hf default at top
            Character('레이워스 공작') "저 또한 여태 직접 본 거에 의하면, 그녀가 그랬을 거라고는 생각 안 합니다."

            hide char
            "에프탈 제국 사람이라면 황후가 황제를 진심으로 사랑한다는 것쯤은 모를 수 없는 이야기였다."

            "둘의 애절한 사랑 이야기가 서적이나 연극으로도 팔릴 정도였으니 말이다."

            "무엇보다 황후가 황제를 죽여서 얻을 수 있는 것도 없었다. 어차피 본인의 아들이 훗날 차기 황제가 될 텐데, 굳이 서두를 필요가 없지 않은가."

            show char hf default at top
            Character('레이워스 공작') "오히려, 황태자 측이 황제를 배신했을 겁니다."

            hide char
            "황태자···. 그를 잊고 있었다."

            "야망과 욕심으로는 황제를 넘어서는 인물. 그는 항상 이 제국의 모든 것을 얻기 위해 안달이 나 있었다."

            "황태자라면 황권을 위해서라면 제 아비를 살해하고도 남을 인간이었다."

            s "제가 황태자를 잊고 있었군요···."

            s "그가 제1황위 계승자인데 말이죠."

            "헤안은 직접 대화에 참여하지는 않았지만, 고개를 끄덕였다."

            "그도 같은 생각을 하고 있는 듯했다."

        "'황태자'일 것이라고 추측한다.":
            $ persistant.Likeability['hean'] += 5
            s "그렇네요. 그럼, 역시 황태자밖에 없겠군요. "
            s "그는 황제의 죽음에서 가장 얻을 것이 많은 자니까요."

            show char hf default at top
            Character('레이워스 공작') "네, 제 생각도 그렇습니다. "

            show char hf default at top
            Character('레이워스 공작') "황태자가 황후 몰래 독단적으로 일을 벌였을 겁니다."

            hide char
            "헤안은 직접 대화에 참여하지는 않았지만, 고개를 끄덕였다."

            "그도 같은 생각을 하는 듯했다."

            "이번 일의 주동자가 황태자라고 여겨지는 것은 당연했다."

            "황태자는 늘 욕심이 많았으며, 이 제국의 모든 것을 얻기 위해 안달이 나 있는 사람이었다."

            "나와 공작은 용의자 후보에서 황후를 제외했다. "

            "에프탈 제국 사람이라면 황후가 황제를 진심으로 사랑한다는 것쯤은 모를 수 없는 이야기였다."

            "둘의 애절한 사랑 이야기가 서적이나 연극으로도 팔릴 정도였으니 말이다."

            "무엇보다 황후가 황제를 죽여서 얻을 수 있는 것도 없었다. 어차피 자기 아들이 훗날 차기 황제가 될 텐데, 굳이 서두를 필요가 없지 않은가."

    s "황제의 죽음이 지금 밝혀진 건, 이제 숨겨도 상관이 없거나···."
    show char hf default at top
    Character('레이워스 공작') "황후가 참다못해 밝혔을 수 있겠군요."

    s "네. 그렇게 되겠군요."

    show char hf default at top
    Character('레이워스 공작') "황태자가 집권을 시작하겠지만, 지금 당장은 황제의 장례 덕분에 공작가의 감사가 늦어질 것입니다."

    s "어찌 보면 시간을 번 셈이군요."

    
    hide char
    play music "bgm/comfort7.mp3"
    "황제의 죽음을 계기로 공작가에겐 기회가 찾아왔다. "

    "시간만 있다면, 공작가가 반역을 일으켰다는 누명 자체는 벗을 수 있을 터였다."

    "현재 처한 상황은 이래 보여도 레이워스 공작가는 제국 내 둘도 없는 명문 가문이었다. "

    "게다가 공작가의 역사와 명성은 황실에 준할 정도로 어마어마했다."

    show char hf default at top
    Character('레이워스 공작') "황녀님, 어제의 그 목표는 여전합니까?"

    hide char
    "갑자기 공작이 내게 다시금 목표를 물어왔다. "

    s "당연합니다."

    "황제가 사망했다고 해서, 황실 자체가 무너지는 것이 아니었다. 무엇보다 전쟁은 여전히 지속되고 있었다."

    "하지만, 왠지 힘이 들어가지 않았다."

    show char hf default at top
    Character('레이워스 공작') "제가 인사가 늦었습니다."

    s "···?"

    show char hf default at top
    Character('레이워스 공작') "감사합니다."

    show char hf default at top
    Character('레이워스 공작') "제 아들을 살려주신 것 말입니다."

    show char hf default at top
    Character('레이워스 공작') "덕분에 아이는 지금 안정을 취하고 있습니다."

    s "아, 아닙니다. "

    show char hf default at top
    Character('레이워스 공작') "이 은혜는 잊지 않겠습니다. 앞으로 레이워스가는 황녀님께 충성을 바칠 것을 맹세하겠습니다."

    hide char
    "나를 경계하던 공작의 태도가 하루아침에 변했다."

    "내 뒤에 레이워스 공작가가 있다는 사실만으로도 든든한 아군을 얻은 것만 같았다."

    scene bg noble way
    play music "bgm/hean1.mp3"
    "그렇게, 공작과 황실에 관한 이야기를 조금 더 나눈 후, 나는 헤안과 집무실을 나섰다."

    show char h default def at top
    h "산책이라도 조금 하시겠습니까?"

    hide char
    "헤안이 내게 말을 걸었다. 평소의 그라면 하지 않았을 행동을 하면서."

    s "그럴까요."

    "어제의 일이 떠올랐다. 분명 그때만 해도, 기분이 나쁘지 않았는데."

    "지금은 잘 모르겠다. 오늘 그의 얼굴을 제대로 본 적이 없는 것 같다."

    menu .m1:
        "그래서인지, 괜히 미안한 마음이 들어서 내가 먼저 입을 열었다."
        "기사단 복귀 관련 이야기를 꺼낸다.":
            s "헤안님은 충분히 여기가 정리되면, 복귀하셔도 괜찮을 것 같습니다."
            s "시간도 생겼으니까요."

            s "황제가 서거한 이상, 전쟁을 계속 밀어붙일 수는 없을 겁니다."

            s "기사단 쪽은 걱정하지 마세요."

        "사적인 이야기를 꺼낸다.":
            $ persistant.Likeability['hean'] += 5
            s "어제는 잘 들어가셨나요?"
            s "어제는 날이 괜찮았던 것 같은데, 오늘은 조금 춥네요."

            s "하하···."

            s "아! 헤안님께서는 여기가 정리되는 대로 바로 복귀하셔도 괜찮을 것 같습니다."

            "혼자 횡설수설 떠들어, 어색해진 분위기에 나는 화제를 돌렸다."

            s "시간도 생겼으니까요."

            s "황제가 서거한 이상, 전쟁을 계속 밀어붙일 수는 없을 겁니다."

            s "기사단 쪽은 걱정하지 마세요."

            "헤안은 내 말을 끊지 않고, 지긋이 나를 응시했다. "

            show char h default des at top
    h "···괜찮으신 겁니까?"
    hide char
    "그는 알겠다는 대답 대신, 물음으로 답했다."

    show char h default des at top
    h "표정이 좋지 않으셔서요."

    s "아···."

    s "분명, 목표가 달라질 건 없는데도 무언가를 잃어버린 기분이 듭니다."

    s "복잡하네요. 뭐부터 해야 맞을지···."

    hide char
    "그는 잠깐 생각하더니, 입을 열었다."

    show char h default def at top
    h "일단은 기사단으로 복귀하십시오."

    show char h default def at top
    h "혹여나 황궁으로 복귀할까 하신다면, 저는 반대하겠습니다."

    hide char
    "헤안이 내 생각을 뚫어본 것 같았다. "

    "황궁에 가서, 후계자에 관한 논쟁을 치러볼까도 생각했기 때문이었다."

    "그편이 목표를 실현하기에는 빠를 수 있을지 모른다는 생각이 있었다."

    s "예리하시군요."

    "나도 모르게 조급해져만 갔다. 황제의 죽음이 촉진제가 된 게 분명했다."

    show char h default def at top
    h "현재 황실에는 황태자 편이 가득할 겁니다."

    show char h default def at top
    h "세레나님께서 가봤자, 그곳엔 온갖 곳에 적이 가득할 겁니다."

    show char h default def at top
    h "황태자는 제 아비인 황제도 죽였는데, 세레나님이라고 예외는 아니겠죠."

    show char h default def at top
    h "오히려 지금은 전장이나 기사단이 훨씬 안전할 겁니다."

    s "하다못해 이곳엔 당신을 지켜줄 수 있는 에런과 기사단이 있으니까요."

    s "······."

    show char h default def at top
    h "아직 더 고민이 되는 부분이 있으시군요."

    s "현 황제가 죽었으니, 앞으로 저희의 목표는 황태자가 되겠죠?"

    s "황태자마저 죽이고, 혁명에 성공한다면 전 황제가 되겠고요. 제가 마지막 후계이니."

    show char h default def at top
    h "···예."

    s "사실, 그게 무섭습니다."

    s "혁명에 성공하고, 전쟁을 멈춘다까지만 생각해 봤지, 그 이후는 생각해 본 적이 없었습니다."

    s "하지만 이번 사건을 보니, 체감이 되더군요."

    s "황제의 자리는 얼마나 무거울까요?"

    hide char
    "나는 두려워졌다. 황제로서 살아갈 책임감이, 자신감이, 그리고 부족한 능력이."

    "분명 스스로를 믿어보기로 다짐했는데도."

    "눈앞에 일이 닥치니, 생각보다 주체가 되지 못한 것 같았다."

    s "오히려, 저보다는 야망 있고 욕심 있는 현 황태자가 좋을지 몰라요."

    s "그는 제대로 된 후계자 교육도 받았으니까요."

    show char h default def at top
    h "세레나님."

    hide char
    "헤안은 단호하게 내 이름을 불렀다."

    "그러고는 나와 눈을 맞췄다."

    show char h default def at top
    h "적어도, 제가 여태 본 세레나님은 자격이 충분하신 분입니다."

    show char h default def at top
    h "저는 군주에게 가장 중요한 것은 상냥한 마음이라고 생각합니다."

    show char h default def at top
    h "그 마음 하나가 제국민들을 평온케 만들 테니까요."

    show char h default def at top
    h "그리고 세레나 님은 이미 그 마음을 자주 보여주셨습니다."

    show char h default def at top
    h "그러니 마음을 다잡으세요."

    show char h default def at top
    h "황태자는 황제가 되더라도, 전쟁을 멈출 생각이 없습니다. 저희를 압박했던 때를 생각해 보십시오."

    show char h default def at top
    h "그런 자가 황제가 된다면, 제국은 어떻게 될까요?"

    show char h default def at top
    h "전 상상하기도 두렵습니다."

    hide char
    "헤안의 말이 모두 맞았다."

    "황제가 죽어도, 황실은 변하지 않는다. 내가 그걸 가장 잘 알고 있지 않던가. 지겹도록 살았던 곳인데."

    "내 목표는 바뀔 일이 없다. 황제가 누구든 상관없다."

    "나는 제국을 갈아엎어, 이 전쟁을 멈춰야만 한다."

    "그 이유는 거창하지 않았다. 내가 여태 만났던 모든 이들을 위한 마음에서 비롯된 거였으니까."

    s "알겠습니다. 일단 오늘 내로, 공작가로 전달되는 전보가 더 있는지 확인 후, 저는 내일 기사단으로 복귀하겠습니다."

    "나는 그에게 비로소 옅은 웃음을 보일 수 있었다."

    "헤안의 얼굴이 이제야 보이기 시작했다."
    show char h default smi at top
    "그 또한 내게 대답하는 웃음을 보였다."

    "하지만 그의 얼굴에는 걱정이 서려있었다. 아마도 나를 향한 것 같았다."

    "나는 그 걱정을 무시했다. "

    scene black
    "그렇게 짧게 인사를 건네고, 방으로 돌아갔다."

    scene bg noble bed yellow night
    play music "bgm/sad4.mp3"
    "분명 헤안과 헤어진 지 얼마 되지 않았던 것 같은데, 창문을 보며 멍 좀 때렸더니 해가 지고 있었다."

    s "아 벌써···."

    "저녁때가 된 것 같아, 일어나려 했다."

    "하지만, 발걸음이 쉽게 떨어지지 않았다."

    "왜일까. "

    "분명 목표에 대한 걱정도 다 해결이 되었는데도, 뭔가 답답했다."

    s "황제···."

    "제국의 최고 위치에 있으면서, 말 한마디면 뭐든 가능한 사람."

    "그와 동시에 전쟁을 일으키고, 학살을 일삼으며, 제국민을 사람 취급도 안 하는 사람."

    "그리고 하나가 더 있다."

    s "아버지···."

    "그에 대한 좋은 기억 하나 없지만, 어찌 되었든 그가 내 아버지임은 변하지 않았다."

    "그의 죽음에 대해서 추모하겠다거나, 슬프다는 생각이 들지는 않았다."

    "나를 괴롭혔던 사람에 대한 원망, 해방감이 더 크면 모를까."

    "그럼에도, 이 미묘함은 어쩔 수가 없었다."

    s "꼴이 좋으시네요, 아버지···."

    "처음 입 밖으로 아버지라는 단어를 꺼내봤다."

    "그리고, 알 수 없는 외로움이 몰려왔다."

    "그 누구도 쉽게 믿을 수 없었고, 늘 외로웠다. 그래서 오히려 나는 외로움 자체를 알 수 없었다."

    "하지만, 이번만큼은 외로웠다."

    s "이젠 정말 혼자네. 나도, 아버지도."

    s "어쩌면, 모든 게 다 이렇게 무의미한 관계가 될지도 몰라···."

    "나는 창밖을 한참 더 바라봤다. 저녁놀은 여전히 아름다웠다 ."

    play sound "sfx/knock.mp3"
    "또다시 시간이 얼마나 더 지났을까, 누군가 방문에 노크를 해왔다."

    s "···?"

    show char h default des at top
    h "헤안입니다. "

    show char h default des at top
    h "저녁을 안 드신 것 같아, 대충 끼니가 될 만한 거로 가져왔습니다."

    hide char
    "나는 직접 문을 열어주었다."

    "그리고 그를 올려다보았다."

    "헤안은 걱정이 가득한 눈빛이었다. 동시에 무거워 보이는 쟁반을 들고 있었다. "

    show char h default des at top
    h "들어가겠습니다."

    hide char
    "헤안은 나를 지나쳐, 쟁반을 방 안의 테이블 위에 올려두었다."

    "나는 괜히 눈치를 보며, 그를 뒤따랐다."

    "내가 헤안에게 다가가자, 그가 갑자기 뒤를 돌며 몸을 내 쪽으로 돌렸다."

    "나는 왠지 모르겠지만, 본능적으로 그와 마주치지 않기 위해 고개를 떨궜다."

    show char h default def at top
    h "대체 무엇이 당신을 그렇게 괴롭히는 겁니까?"

    show char h default def at top
    h "항상 밝을 수는 없겠지만, 전 당신이 웃을 때가 좋습니다."

    hide char
    "그의 목소리가 떨리고 있었다."

    "동시에 떨고 있는 두 손으로 내 양 볼을 잡아 떨궜던 고개를 들췄다."

    show char h default def at top
    h "이런··· 표정 말고."

    hide char
    "나조차 내 표정이 어떤지 모르겠을 뿐이었다."

    "하지만 그의 매초 달라지는 표정이,"

    "바라보는 눈빛과 떨리는 손,"

    "그리고 붉게 상기된 얼굴까지···."

    "그 모든 것이 오로지 나를 향하고 있다는 것을 알 수 있었다. "

    "나는 그가 내 볼에 올려놓은 손에, 내 손을 더했다."

    menu .m2:
        "그리고, 헤안에게 솔직해져야 할 것 같다고 생각을 했다."
        "저, 슬픈 것 같아요.":
            $ persistant.Likeability['hean'] += 2
            s "저, 아무래도 지금 슬픈 것 같아요."
            s "제가 그 사람을 가족이라고 여겼었나 봐요."

            s "물론 그럼에도 제 목표는 변함없습니다, 걱정하지 마세요."

            "나는 최대한 의연하게 지금의 감정을 전달했다."

            "슬픈 사람치고는 덤덤한 말을 이어간 걸지도 모르겠다."

            show char h default def at top
            h "세레나님···."

            hide char
            "오히려 헤안이 나보다 더 슬퍼 보였다."

            show char h default def at top
            h "지금만은 목표에 사로잡히지 않으셔도 됩니다."

            show char h default def at top
            h "오히려, 제가 계속 세레나님을 괴롭게 했던 건 아닌지 죄송스럽습니다."

            show char h default def at top
            h "슬퍼하는 것 또한 이겨내기 위한 하나의 과정이라고 생각합니다."

            show char h default def at top
            h "마음껏 슬퍼하십시오. 제가 당신의 곁에 있겠습니다."

            hide char
            "헤안의 말 한마디 한마디가 무겁게 느껴졌다."

            show char h default def at top
            h "그러니··· 일단 아무 생각 하지 맙시다."

            hide char
            "헤안는 내가 이전에 해줬던 위로를 내게 다시 되돌려 주었다."

            "그러고는 그가 내 얼굴을 끌어당겼다."

            "나는 별다른 저항을 하지 않았다."

            "헤안과 입을 맞춤으로써 내 외로움이 지워졌으면 했다."

        "저, 이제 혼자예요.":
            $ persistant.Likeability['hean'] += 10
            s "저, 아무래도 이제 혼자가 된 것 같아요."
            s "외로움이라는 감정을 모르는 줄 알았어요, 제가···."

            s "근데 지금은 그냥 외로워요."

            "나는 그에게 호소하듯 한마디 한마디를 뱉어냈다."

            s "분명 사랑받은 기억 따윈 없는데, 황제는 저를 방치하기만 했는데도···."

            s "그 사람의 죽음이 믿기지 않아요."

            "입술이 메말라갔다. 떨어지지 않는 입을 떼려고 노력했지만, 역부족이었다."

            "눈가에 눈물이 고였다. 하지만, 울지 않으려 애썼다."

            "그 순간, 헤안이 내 손을 맞잡았다."

            "이 행동이 나에게 어떤 용기를 주었다."

            s "사실 저도 사랑받고 싶었습니다. 황제는 제 친아버지였으니까요."

            s "가만히 숨만 쉬어도 사랑받는 황태자가 부러웠습니다."

            s "힘든 일이 있거나, 모든 걸 포기하고 싶었을 때 누군가에게 기대고 싶었습니다."

            s "하지만, 제 곁에는 아무도 없었죠."

            s "아버지는 제 존재 자체를 부정하셨습니다. 사랑받고 싶은 이 갈망이 저를 오랫동안 괴롭혔던 것 같습니다."

            s "저는 그 사람을 가족이라 여겼나 봅니다."

            "나는 그에게 솔직한 내 감정과 생각을 전달했다."

            s "제 생각을 누군가에게 말하기는 처음입니다. 부끄럽네요···."

            s "그래도 제 목표에는 흔들림이 없습니다, 걱정하지 마세요."

            "외롭다고 호소하는 사람치고는 끝이 덤덤했을지도 모른다."

            "그저, 나 자신이 무기력해 보일까 봐 덧붙인 사족에 가까웠다."

            "헤안의 앞에서는 최소한의 체면을 차리고 싶었다. 같은 목표를 지니고 있었으니까."

            "그러나, 오히려 헤안은 마지막 한 마디에 울컥하는 표정을 지었다."

            scene black
            play sound "sfx/skin.mp3"
            "그는 손을 내려놓고, 나를 끌어안았다."

            "빈틈없이 껴안아서인지, 앞이 보이지 않았다."

            show char h default def at top
            h "···이래도 당신의 외로움이 채워지지 않을까요?"

            s "······."

            show char h default def at top
            h "세레나님이 그를 가족으로 생각했다면, 그런 것이겠죠."

            show char h default def at top
            h "다만, 세레나님이 외롭다고 느끼는 건 세레나님 탓이 아닙니다."

            show char h default def at top
            h "당신이 잘못한 건 하나도 없습니다. 그러니 죄책감 가질 필요 없습니다. "

            show char h default def at top
            h "이제는 당신의 악몽을 놔줍시다···."

            hide char
            "그의 얼굴을 볼 수 없었다."

            "점점 나를 세게 껴안는 감각만이 느껴졌다."

            "나는 고개를 들어 조심스럽게 입을 열었다."

            s "어떻게 하면 좋을까요···."

            "헤안은 울먹거리는 내 목소리를 듣자, 제 품 안에 가둬뒀던 나를 풀어주었다."

            "그와 눈이 마주쳤다."

            show char h default def at top
            h "지금은 우리 둘만 생각하는 겁니다."

            scene hean_illust1
            $ persistent.UnlockImage['hean'][0] = True
            hide char
            "헤안이 조심스럽게 내 턱을 들어 입을 맞췄다."

            "고요한 방에는 우리 둘의 다급한 숨소리만 들렸다."

            "감정은 점점 격해졌고, 그는 내 입술을 놓치지 않은 채 침대를 향했다."

            s "헤안, 잠시만···!"

            "푹신한 이불 위에서도 우리는 멈출 생각을 하지 않았다."

            "오히려 더욱더 서로를 보채듯 달라붙었고, 서로의 허물을 벗겨냈다."

            #show char h default defr at top
            h "이상하게도 당신 곁에만 있으면 통제가 되질 않습니다.
"

            #show char h default defr at top
            h "모든 게 다요.
"

            #show char h default defr at top
            h "그러니, 이해해 주세요.
"

            hide char
            "그가 버거웠다."

            "하지만, 내 머릿속에는 점점 그로 가득 차올랐다."

            "외로움 따위는 잊힌 지 오래였다."

            "나는 헤안의 뜨거운 숨결을 가까이 느끼며 모든 것을 그에게 맡겼다."

            scene black

    play sound "sfx/bird.mp3"
    play music "bgm/comfort4.mp3"
    "서늘한 바람이 나를 반겼다."
    scene black
    "공작가의 두 번째 아침을 맞이했다."

    "나는 서둘러 기사단으로 복귀할 채비를 마쳤다."

    $ persistent.ClaerChapter = max(12,persistent.ClaerChapter)
    return
