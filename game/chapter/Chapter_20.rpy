﻿label chapter_20:
    scene black
    "제목 : 마지막 비호"

    scene bg kingdom way
    play music "bgm/dis.mp3"
    "황후가 세레나에 의해 감금되었다는 소식이 황궁에 울려 퍼졌다."

    "당연한 치사였는지도 모른다. "

    "프라타히라 왕국이 세레나의 편이 되어, 황궁을 함께 휩쓸었으니."

    show char knight default at top
    Character('황실 기사단') "세레나 황녀는 황제가 애지중지했던 딸 아니었어?"

    show char knight default at top
    Character('황실 기사단') "프라타히라 왕국이 황녀를 돕다니, 무슨 일이야?"

    show char knight default at top
    Character('황실 기사단') "지금 뭐가 어떻게 돌아가고 있는 거냐고!"

    hide char
    "순식간에 여론이 흔들렸다."

    "하지만, 에런 만큼은 그러지 못했다. 아니, 그럴 수 없었다."

    show char e default des at top
    e "나마저도 진압되는 건 순식간이겠지만,"

    show char e default des at top
    e "황후의 세력은 아직도 많이 남아있어. 곧 황궁으로 몰려들 거고."

    show char e default des at top
    e "여전히 세레나에게 승산은 없어···."

    scene black
    hide char
    "에런은 남은 황실 기사단을 이끌고 황후가 감금되어 있는 곳으로 향했다."

    "황궁의 지리와, 비밀 통로를 꿰고 있는 에런에게는 쉬운 일이었다."

    "황후를 구출해 낸다는 것은 말이다."

    show char e default des at top
    e "이건 다 세레나를 위해서야."

    
    scene bg prison
    show char q default bsmi at top
    Character('황후 카일리') "하하, 네가 오기를 기다리고 있었단다."

    show char q default bsmi at top
    Character('황후 카일리') "너라면 알고 있었겠지. 여기서 끝이 아니라는 걸."

    show char q default bsmi at top
    Character('황후 카일리') "그 아이, 생각보다 많은 걸 준비해 뒀더구나."

    show char q default bsmi at top
    Character('황후 카일리') "이건 나도 놀랐어."

    show char e default des at top
    e "······."

    show char e default def at top
    e "무의미한 싸움을 빨리 끝내고 싶습니다."

    show char q default def at top
    Character('황후 카일리') "그래, 그건 나도 마찬가지란다."

    show char q default def at top
    Character('황후 카일리') "황궁 외곽 쪽으로 병사들과 정예 기사단을 준비해 놓았어."

    show char q default def at top
    Character('황후 카일리') "어서 움직이자꾸나."

    show char e default def at top
    e "···기사들과 먼저 가고 계십시오."

    show char q default bad at top
    Character('황후 카일리') "허튼짓은 하지 않는 게 좋아, 에런."

    show char e default def at top
    e "네, 잘 알고 있습니다."

    scene black

    scene bg kingdom way
    play music "bgm/tension5.mp3"

    s "이제는 스승님··· 아니, 에런을 찾아야 해."

    hide char
    "황후는 붙잡아뒀으니, 다른 불씨를 꺼트려야만 했다."

    show char h default bad at top
    h "세레나님!"

    show char h default bad at top
    h "황후가 탈출했다고 합니다."

    show char h default bad at top
    h "행방을 알 수 없었던 에런 경이 도운 것 같습니다."

    hide char
    "간과했다. 이곳은 그들의 소굴이라는 것을."

    s "그래, 이렇게 쉽게 끝날 리가 없지."

    scene bg forest night
    "나는 아드리안, 헤안과 함께 예상되는 도망 경로로 향했다."

    "녹스에게는 황후가 황궁 밖으로 나가지 않게 감시해달라는 부탁을 남겼다. "

    "도망 경로에 도착했을 때, "
    #show char e default def
    "황후는 이미 사라진지 오래였고, 혼자 남아 서 있는 스승님이 보였다."

    s "아드리안, 헤안."

    s "둘은 기사단과 함께 황후를 계속 쫓는 게 좋겠어."

    show char a default emb at top
    a "뭐?"

    show char h default emb at top
    h "···하지만."

    s "괜찮으니까, 빨리."

    hide char
    "나는 둘을 황후가 있는 쪽으로 보냈다."

    "스승님의 행동들이 다 이해가 되지 않아서,"

    "그래서 마지막으로 대화를 나누고 싶었다."

    menu .m0:
        "혹시라도 내가 모르는 진실이 있을 까봐."
        "왜 이런 짓을 벌인 거죠?":
            s "왜 이런 짓을 벌인 거죠?"
            s "정말 부패한 황실을 엎고 싶었던 겁니까?"

            s "제가 봤을 때는 아닌 것 같은데."

        "저한테 할 말 있으실 것 같은데··· 아닌가요?":
            $ persistant.Likeability['eren'] += 5
            s "저한테 할 말 있으실 것 같은데···."
            s "아닌가요?"

            show char e default des at top
            e "······."

            show char e default des at top
            e "나는 너를 처음 봤을 때부터 지금까지,"

            show char e default des at top
            e "지켜야겠다는 마음뿐이었어."

            show char e default des at top
    e "···이번 한 번만 물러나 주면 안 되는 거야?"
    s "지금 황후가 제국을 망치는 걸 가만히 보고만 있으라는 거예요?"

    hide char
    "황후가 어떤 사람인지 알고 있다면, 절대 할 수 없는 말이었다."

    show char e default des at top
    e "네가 살려면 이 방법밖에는 없어."

    s "당신이 황제가 되는 게, 나를 살리는 거라고요?"

    s "그건 오히려 나를 죽이는 겁니다."

    s "스승님의 말, 행동 그 모든 게 모순적이에요."

    show char e default emb at top
    e "세레나, 제발···!"

    hide char
    "스승님은 내 손을 잡고, 간절하게 외쳤다."

    show char e default des at top
    e "황후에게는 아직도 세력이 많이 남아있어."

    show char e default des at top
    e "왕국을 끌어들여도 안 된다고."

    show char e default des at top
    e "여론도 황후와 내 쪽이 더 우위야."

    show char e default des at top
    e "아직도 현실을 모르겠어?"

    hide char
    "더 이상 스승님의 말을 들을 가치가 없었다."

    "나는 분노에 휩싸였다."

    play sound "sfx/slap.mp3"
    with shake
    "손을 쳐내, 스승님의 뺨을 내리쳤다. "
    

    s "현실을 모르는 건 스승님이겠죠!"

    s "스승님은 그저 꼭두각시일 뿐이에요."

    s "스승님이 황제가 된다 해도, 이 제국은 변하지 않을 겁니다."

    "그때, 갑자기 근처에서 큰 소리가 나기 시작했다."

    "칼이 맞부딪히고, 사람들이 괴성을 지르는 소리가."

    "그리고 그 소리는 아드리안과 헤안을 보냈던 방향에서 나고 있었다."

    s "또 무슨 짓을 벌인 거예요?"

    show char e default des at top
    e "말했잖아···. 황후에게는 네가 모르는, 숨겨져 있는 세력이 아직도 많이 남아있다고."

    hide char
    "나는 그의 말을 듣자마자, 아드리안과 헤안이 있는 방향으로 급하게 뛰어갔다."

    "스승님 또한 나를 뒤따랐다."
    
    scene bg forest fire
    play music "bgm/ptsd7.mp3"
    "그러나 이미 내가 도착했을 때는, 늦은 후였다."

    "헤안과 아드리안, 그리고 기사단원들은 상처투성이인 채로 널브러져 있었고, "

    "황후의 전력이 내 앞을 가로막았다."

    "황후는 그 틈에서 안전한 보호 아래에, 서 있었다."

    show char e default des at top
    e "······."

    hide char
    "나는 원망스러운 눈빛으로 뒤따라온 스승님을 쳐다봤다."

    s "이게 스승님이 원하시던 겁니까?"

    "스승님의 눈은 세차게 흔들리고 있었다."

    show char e default des at top
    e "···세레나는 물론 세레나의 측근도 건드리지 마십시오."

    show char q default def at top
    Character('황후 카일리') "이거 하지 말라, 저거 하지 말라."

    show char q default def at top
    Character('황후 카일리') "그럼, 대체 나는 뭘 하라는 거니."

    hide char
    "황후가 앞으로 나섰다."

    show char q default def at top
    Character('황후 카일리') "에런, 이래서 황제의 역할은 제대로 할 수나 있겠니?"

    show char q default def at top
    Character('황후 카일리') "그 자리에 올라가기 위해서, 손에 피 묻히는 건 어쩔 수 없는 일이야."

    show char e default des at top
    e "······."

    show char q default def at top
    Character('황후 카일리') "넌 너무 나약하구나···."

    show char q default def at top
    Character('황후 카일리') "너를 강하게 키우지 못한 이 어미 잘못일지도 모르겠어."

    show char e default emb at top
    e "···그게 대체 무슨 소리십니까?"

    show char q default def at top
    Character('황후 카일리') "이제는 말도 제대로 못 알아 듣는 거니."

    show char q default smi at top
    Character('황후 카일리') "내가 네 친모라고, 에런."

    hide char
    "둘의 대화를 따라갈 수가 없었다."

    "이 상황이 그저 충격적이었다."

    "놀랍게도 에런 또한 이 사실을 모르고 있는 것 같았다."

    "일단, 나는 둘의 언쟁을 뒤로 하고 집중하기로 했다."

    "힘을 사용하기 위한 집중을."

    "여태 알 수 없는 이유로 사용되지 않았지만, 지금이라면 될 것만 같았다."

    "힘을 사용할 수만 있다면, 나는 물론 아드리안과 헤안까지 치유가 될 테니까···."

    "지금의 나는 간절했다. 그 누구보다도."

    show char e default bad at top
    e "말도 안 됩니다. 헛소리하지 마세요."

    hide char
    "에런 스승님은 황후의 말을 부정하듯 쳐냈다."

    show char q default def at top
    Character('황후 카일리') "네가 아무리 부정해도 달라지는 건 아무것도 없어."

    show char q default def at top
    Character('황후 카일리') "너를 낳은 것도, 황궁으로 불러들인 것도, 황제를 죽인 것도 모두 나고. "

    show char q default def at top
    Character('황후 카일리') "황태자를 죽인 것도, 전쟁에 나가 분란을 일으켰던 것도 여태 다 모두 네가 한 일이니까."

    show char q default def at top
    Character('황후 카일리') "그 모든 잘못을 내게 돌릴 생각은 마."

    show char q default def at top
    Character('황후 카일리') "내 말을 듣기로 결정한 건 바로 너의 선택이었으니까."

    show char e default bad at top
    e "저도 잘 알고 있습니다. 어쨌든 제가 저지른 일들이라는 거."

    show char e default des at top
    e "하지만··· 이건 뭔가 잘못됐습니다."

    show char e default des at top
    e "제가 당신의 아들이라는 미친 소리도, 마음을 다잡지 못해 휘둘리는 저도"

    show char e default des at top
    e "죄다 역겹습니다."

    show char e default des at top
    e "대체 내가 무슨 짓을 저질렀던 건지···."

    hide char
    "스승님은 머리를 짚었다. "

    "단언컨대, 그는 무너져 내려가고 있었다."

    "손을 무척이나 떨고 있었으니까."

    "후회라도 하고 있는 걸까."

    show char q default bad at top
    Character('황후 카일리') "나는 황제의 피를 가지고 있는 놈들을 모조리 없앨 거란다."

    show char q default bad at top
    Character('황후 카일리') "역겨운 황제의 피가 더 이상 이 제국에 흘러선 안 돼."

    show char q default bad at top
    Character('황후 카일리') "그리고, 오로지 나만을 위한 새로운 제국이 만들 것이란다."

    show char e default ang at top
    e "말이 다르지 않습니까!"

    show char e default ang at top
    e "전에 저와 약속했을 땐, 지금의 황가를 무너뜨리는 것뿐이었잖아요."

    show char q default def at top
    Character('황후 카일리') "그래, 황가를 무너뜨리기 위해서는 황실의 피부터 메마르게 해야 하지 않겠니."

    show char q default def at top
    Character('황후 카일리') "저 아이도 마지막엔 그에 포함되겠고."

    show char q default def at top
    Character('황후 카일리') "넌 머리도 좋은 애가, 저 아이와 관련되면 멍청해지더구나."

    show char q default def at top
    Character('황후 카일리') "지금이라도 현실을 직시해 보렴."

    show char q default def at top
    Character('황후 카일리') "네가 무슨 상황인지, 그리고 저 아이가 너 때문에 무슨 일을 겪고 있는지."

    show char e default bad at top
    e "이런 식으로 뒤통수를 치실 생각이었습니까?"

    hide char
    "스승님은 고개를 숙인 뒤, 그 후로 말을 잇지 못했다."

    "더 이상 그의 눈에 의지라는 게 보이지 않았다."

    "이 혼란스러운 상황을 해결할 수 있는 유일한 사람은 나밖에 남아있지 않았다."

    "지금부터는,"

    "제국의 미래가 달린 결정을 내려야 할 때였다."

    play music "bgm/브금 중지.mp3"
    "그 순간이었다."

    play sound "sfx/heart.mp3"
    "내 심장이 세차게 뛰기 시작했다."

    "제국과 나를 응원해주는 사람들을 생각해서였을까?"

    play music "bgm/tension7.mp3"
    "심장 부근의 힘이 자유롭게 흘러 다니는 게 느껴졌다."

    "온몸에 전율이 흘렀다. 처음 느껴보는 감각이었다."

    play sound "sfx/magic.mp3"
    "나는 그 힘을 아드리안과 헤안, 그리고 기사단에게 흘려보냈다."
    show white at fadeInOut
    s "···됐다."

    "나는 작게 혼잣말을 속삭였다."

    "동시에, 널브러졌던 이들이 일어나기 시작했다."

    show char knight default at top
    Character('황실 기사단') "무, 뭐야?!"

    show char knight default at top
    Character('황실 기사단') "쓰러졌던 기사들이 다시 일어나고 있습니다!"

    show char q default emb at top
    Character('황후 카일리') "뭐?"

    hide char
    "황후와 그의 기사단이 당황해하며 물러섰다."

    show char q default bad at top
    Character('황후 카일리') "계획이 너무 틀어졌어···."

    hide char
    "황후가 중얼거렸다."

    show char q default ang at top
    Character('황후 카일리') "사생아에게 저런 힘이 있다는 걸 나한테 말 안 하고 있었어? 에런 스노우!"

    hide char
    "스승님은 여태 모든 사건 사고를 황후에게 전달하지 않은 모양이었다."

    "나름의 보험이었던 걸까."

    play sound "sfx/war_shout, sword_hit2.mp3"
    "또다시 두 기사단이 맞부딪히기 시작했다."

    "이번에는 나도 합세했다."

    "넘치는 힘이 나를 둘러싸고 있어서인지 몸 자체가 가벼웠다."

    show char h default emb at top
    h "세레나님, 괜찮으십니까? 또 그 힘을 사용하신 겁니까?"

    show char a default emb at top
    a "야, 너 뭐야? 괜찮아?"

    hide char
    "둘은 동시에 내 상태를 물어왔다."

    "상태가 심각했던 건 정작 그 둘이었는데도."

    s "물론, 괜찮지."

    "힘을 계속 사용해서인지 어지러워지기는 했지만, 이 정도는 괜찮았다."

    "전투가 지속되자, 점점 우리 기사단이 우위에 서기 시작했다."

    "내 힘 덕분에 기사단의 체력이 소모되지 않고 있었기 때문이었다."

    "이대로만 간다면, 황후를 제압하고 제국 개혁이라는 목표가 머지 않은 시점이었다."

    play sound "sfx/sword_out.mp3"
    "그때 황후가 혼란을 틈타, 기사의 칼을 빼 들어 달려들었다."

    show char q default ang at top
    with shake  
    Character('황후 카일리') "너만 없었어도!"
    

    s "···!"

    hide char
    "하지만 황후의 칼은 막혔다."

    call screen endingSelect
    $ persistent.IsAllClear = True
    $ persistent.ClaerChapter = max(21,persistent.ClaerChapter)
    #menu .m1:
    #    "...에 의해."
    #        "녹스"
    #        with choise3
#
    #        "아드리안 하몬"
    #        with choise4
#
    #        "세레나 에프탈"
    #        with choise5
#
    #
    return
