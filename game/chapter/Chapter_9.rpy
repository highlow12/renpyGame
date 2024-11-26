label chapter_9:
    "제목 : 도움을 받는다는 것은"

    scene black
    play sound "sfx/clothes.mp3"
    play music "bgm/sad.mp3"
    "나는 외부에서 들리는 소리에 어렴풋이 정신을 차렸다."

    "내가 어디에 있는지조차 알 수 없었다."

    "쓰러진 후로는 그 어떤 기억도 떠오르지 않았다. "

    "그저 타오르는 듯한 열감을 느꼈었다."

    "지금도 별반 다를 건 없는 것 같았지만, 쓰러지기 전보다는 확실히 괜찮았다."

    "문제는, 누군가가 내 몸을 돌보고 있다는 것이었다."

    "몸을 일으키고 싶었지만, 내 몸과 생각은 이미 따로 놀고 있었다."

    "그냥, 움직일 수가 없었다. 상처 때문인지, 피로도의 축적 때문인지."

    "눈조차 떠지지 않을 정도로."

    show char a default def at top
    a "정신을 차린 건가?"

    hide char
    "희미하게 들리는 익숙한 목소리였다."

    "목소리를 통해 누구인지 금방 추측이 가능했다."

    "나에게 여러모로 도움을 주었던 사람이자, 프라타히라의 왕자의 측근."

    "그는 적국의 황녀인 나를 왜 도망치게 두었는지, 지금은 또 왜 나를 쫓아와서 돌보고 있는지 알 수 없었다. "

    "그를 어떻게 생각해야 할지 모르겠을 뿐이다."

    "하지만, 지금은 그의 도움 따위 받고 싶지 않았다."

    "타나를 생각해서라도."

    show char a default def at top
    a "움직이지 마."

    show char a default def at top
    a "단도에는 맹독이 있었어. 너는 그걸 정통으로 맞았고."

    show char a default def at top
    a "상처 자체는 깊지 않지만, 독에 중독되면 저세상 가는 건 금방일걸?"

    s "뭐?"

    show char a default def at top
    a "나한테 해독제가 있어."

    show char a default des at top
    a "그러니까, 제발 가만히 있어. 치료해 줄 테니까."

    hide char
    "무어라 말이라도 하고 싶었다. 하지만 목소리 또한 잃어버린 지 오래였다."

    show char a default des at top
    a "아마 너도 나 불편할 거고, 나도 너 불편해."

    show char a default des at top
    a "지금 무슨 일이 벌어졌는지, 나도 감당이 안 되고 있으니까."

    show char a default des at top
    a "그리고, 널 지금 이렇게 만든 녀석한테 복수해야 하는 거 아니야?"

    show char a default def at top
    a "나였다면, 이대로는 억울해서 못 죽을 것 같은데."

    hide char
    "그의 말이 맞았다. 여기서 허무하게 죽을 수는 없었다."

    "누구 좋으라고."

    "하지만, 그의 행동이 여전히 이해가 가지 않았다."

    show char a default def at top
    a "물론 나도 여기서 널 살리는 것보다, 죽이는 게 좋아."

    show char a default des at top
    a "하지만 잘 모르겠다. 그렇게 해서 뭐가 좋은지···."

    hide char
    "그 또한 답을 모르는 모양이었다."

    show char a default des at top
    a "그냥, 내 눈앞에서 사람 죽게 못 내버려두는 내 이기심이라고 생각해."

    show char a default des at top
    a "그리고 다 잊어. 동굴 일도, 지금 일어나고 있는 일도. 모두."

    hide char
    "그 말을 끝으로, 그가 무언가를 들이키고 있는 소리가 들렸다."

    "그러고는 내 몸을 살짝 일으켜, 턱을 잡아 눌렀다."

    "자연스럽게 내 입이 벌어질 수밖에 없었다."

    menu .m0:
        "더 이상 내 몸을 통제할 수 없었다."
        "저항해 본다.":
            "아무리 생각해 봐도, 그에게 몸의 통제권을 빼앗긴 것을 용서할 수 없었다."
            "말은 저렇게 해도, 그가 나에게 무슨 짓을 할지 알 수 없는 노릇이었다."
            show red at fadeInOut
            "최대한 몸을 움직여보려 발버둥 쳤다."

            "하지만 그 때문인지, 상처들이 짓눌려 고통이 더해졌다."

            s "읏···."

            "동시에, 그가 들이킨 것을 삼키는 소리가 들렸다."

            "그리고, 그의 호통이 나를 덮쳐왔다."

            show char a default ang at top
            with shake
            a "야!"
            

            show char a default ang at top
            a "상처도 있는 게 왜 자꾸 이래?"

            show char a default ang at top
            a "고집 좀 부리지 마."

            hide char
            "자기도 저번에 고집부렸으면서. 누구더러 고집부리지 말라는지."

            show char a default ang at top
            a "그냥 해독제 좀 먹이려 한 거야."

            show char a default ang at top
            a "너 손 까딱도 못 하잖아. 내가 먹여줘야 할 거 아니야."

            show char a default ang at top
            a "나도 뭐 하고 싶어서 하는 줄 알아?"

            hide char
            "그럼 하지를 말던가. 그의 말에는 어폐가 있었다."

            "그는 나를 꼭 살려야 하는 것처럼 굴었다."

            scene adrian_illust1
            $ persistent.UnlockImage['adrian'][0] = True
            "결국 한숨을 쉬더니, 병째로 내 입에 그가 해독제라고 주장하는 것을 천천히 넘겨주기 시작했다."

            "해독제는 입안을 가득 채운 걸로도 모자라, 볼을 타고 흘렀다."

            "제대로 삼키기도 힘들었기 때문이었다."

            #show char a default des at top
            a "이거 봐, 다 흘리잖아. "

            hide char
            "내 상처가 덧나지 않도록, 나를 조심히 안은 그의 손길이 느껴졌다."

            "무엇이 두려운지, 바들바들 떨고 있는 진동까지도."

        "가만히 있는다.":
            $ persistant.Likeability['adrian'] += 15
            play music "bgm/romantic5.mp3"
            "나는 가만히 있었다."
            "상처가 가득한 몸을 함부로 움직일 수도 없었기 때문이다."

            "그리고 그의 앞선 말들을 보아. 내게 해독제를 먹이려는 것 같았다."

            "살아야만 했으니, 지금은 그에게 몸을 맡겨야만 했다."

            "그렇게, 해독제가 들어올 것이라는 예상과는 달리 입술에는 새로운 감촉이 느껴졌다."

            scene adrian_illust1
            $ persistent.UnlockImage['adrian'][0] = True
            s "···!"

            "맞닿은 입술 사이로 뒤늦게 해독제가 입 안에 들이닥쳤다."

            "들이닥친 해독제처럼 내 모든 것이 요동치기 시작했다."

            "갑작스러운 고통에 나는 몸을 버둥거렸다."

            show char a default des at top
            a "야, 가만히 좀 있어봐···."

            hide char
            "분명 이전에는 성한 곳 없는 몸뚱아리 때문에, 신경이 분산 되어있었다."

            "하지만 지금은 모든 신경이 고통을 뚫고, 입술에 집중되었다."

            "세상에 둘 뿐인 것만 같았다. 민망한 소리가 오갔다."

            "그러고는, 그가 넘겨준 해독제를 남김없이 목구멍으로 넘겼다."

            "해독제를 먹었으니, 열은 내려야 하는 게 맞았지만 내 몸은 그렇지 못했다."

            "나는 이 열이 독에 의한 게 아니라는 것을 애써 무시했다."

            "그 또한 내 상처가 덧나지 않도록, 나를 조심스러운 손길로 다뤘다."

            "무엇이 두려운지, 바들바들 떨고 있는 진동까지도 느껴졌다."

            show char a default des at top
            a "아까 말했던 거 기억나지? 다 잊어버리라고."

            show char a default des at top
            a "그냥 어쩔 수 없었다고 생각해. "

            show char a default des at top
            a "나도 하고 싶어서 한 거 아니니까."

            hide char
            "괜히 민망함에 투정 부리는 것 같았다."

            "하고 싶지 않아 하는 사람치고는 나를 꼭 살려야만 하는 것 같은 몸짓이었으면서."

    scene black
    show char a default des at top
    a "일단 쉬어."
    hide char
    "그는 계속해서 나를 돌봤다."

    "열이 내리고 있는지, 피는 멈췄는지, 상처가 벌어지고 있지는 않은지."

    "보이지는 않았지만, 그가 열성을 다하고 있다는 사실만큼은 느껴졌다."

    "그렇게 아까와는 달리, 조용한 순간이 한참이나 유지됐다."

    "시간이 얼마나 흘렀는지 모르겠다."

    "왜인지 모르겠지만, 몸이 빠르게 회복되어 가는 게 느껴졌다."

    show char a default def at top
    a "손수건은 다시 돌려줄게."

    show char a default def at top
    a "네 피를 닦느라 조금은 더러워졌지만."

    show char a default def at top
    a "소중한 거라며."

    s "···!"

    show char a default des at top
    a "온전하게는 못 돌려줬네. 그래도, 너한테 쓴 거니까 봐줘."

    hide char
    "그가 몸을 일으키는 듯한 소리가 들렸다."

    show char a default def at top
    a "내 이름은 아드리안 하몬."

    show char a default def at top
    a "자기소개하기에는 너무 늦은 것 같지만 말이야."

    show char a default def at top
    a "다음에는 네 이름, 직접 들을게."

    show char a default def at top
    a "그때의 우리가 과연 자기소개하고 있을 만큼, 평화로울지는 모르겠지만."

    scene bg forest night
    hide char
    "아까까지만 해도 떠지지 않던, 눈이 조금씩 떠졌다."

    "눈을 떴음에도 앞이 잘 보이지는 않았다."

    "그래도 알 수 있는 건, 퉁명스러운 말투와는 달리 그의 표정이 썩 좋지는 않았다는 거다."

    show char a default def at top
    a "눈이라도 떠서 다행이네. 상태 보니까 금방 괜찮아질 것 같아."

    show char a default def at top
    a "난 이만 가볼게. 계속 자리를 비우고 있을 수는 없어서."

    show char a default def at top
    a "너희 막사에서 멀지 않은 곳이니까, 일어나면 금방 찾아갈 수 있을 거야."

    show char a default def at top
    a "안녕."

    hide char
    "그의 인사말에는 여러 의미가 담긴 것 같았다."

    play sound "sfx/footstep_grass.mp3"
    "시간이 어느 정도 흐른 뒤, 나는 몸을 움직일 수 있게 되었다."

    "곧바로 몸을 일으켰다."

    s "빨리 돌아가야 해. 시간을 너무 지체했어."
    
    show red at fadeInOut
    with shake
    s "윽···."
    
    "여전히 상처 자체에 대한 고통은 남아있었다."

    "하지만, 단장이라는 자가 전장을 비우다니. 있어서는 안 되는 일이었다."

    "나는 성치 않은 몸을 이끌며, 제국과 왕국의 습격을 동시에 받았던 기지로 돌아갔다."

    "그리고 내가 있었던 자리를 뒤돌아봤다."

    "그의 말대로 내가 있던 곳은 기지에서 멀지 않은 안전한 곳이었다."

    scene black

    scene bg camp out blood
    play sound "sfx/footstep_grass.mp3"
    play music "bgm/sad5.mp3"
    "돌아왔을 때는 이미 모든 상황이 끝나 있었다."

    "헤안과 스승님이 멍하니 서 있는 나를 발견하고 달려왔다."

    show char h default emb at top
    h "세레나!"

    show char e default emb at top
    e "세레나!"

    show char h default emb at top
    h "여태 어디에 계셨던 겁니까? 정말··· 어떻게 된 줄 알고 걱정을 얼마나 했는지 아십니까?"

    show char e default emb at top
    menu .m1:
        e "괜찮아? 설마 많이 다친 거야?"
        "······.":
            s "······."
            hide char
            "나는 굳이 대답하지 않았다."

            "괜찮다는 말 한마디 꺼내기조차 힘들었기 때문이었다."

            "게다가 몰골만 봐도 괜찮지 않다는 것쯤은 알 수 있을 것이라 생각했다."

            s "지금 상황이 어떻게 된 겁니까?"

        "전 괜찮습니다.":
            $ persistant.Likeability["eren"] += 5 
            $ persistant.Likeability["hean"] += 5
            s "전 괜찮습니다. 그나저나 지금 어떻게 된 겁니까?"
            "진심이 담기지 않은 대답을 한 후에, 곧바로 본론을 꺼냈다."

            "중요한 건 현재 상황이었다."

    "헤안과 스승님은 내 대답에 불만스러운 표정을 지었다."
    "하지만 내 단호함에 어쩔 수 없다는 듯, 헤안이 입을 열었다."

    show char h default des at top
    h "제국과 협상을 했습니다."

    show char h default des at top
    h "침입한 왕국을 함께 진압해 주겠다는 것을 대가로, 프라타히라 왕국 정복을 앞당기라는 것을요."

    s "결국···. 애초에 같은 제국인데도 왜···!"

    show char h default des at top
    h "네. 하지만 어쩔 수 없었습니다. 상황 자체가 급박했으니까요."

    show char e default des at top
    e "우리 기사단의 상태도 모두 좋지 않았으니까요."

    show char h default des at top
    h "저희는 당한 겁니다. 제국과 왕국 둘 모두에게요."

    hide char
    "주먹을 세게 쥐었다. 황제에게 완전히 놀아났다."

    "아마 왕국에 우리 막사의 위치를 알려준 것도, 제국 측이었을 것이다."

    "손해를 감수해서라도, 압박을 주고 싶었던 거다."

    "이 정도 손해는 그들에게 기별도 가지 않으니까."

    "그때 머리가 암전되며, 발밑이 쑥 꺼지는 느낌이 들었다."

    "복부에는 아직 회복되지 못한 피가 흘러나오고 있었다."

    "헤안과 스승님에게는 보이지 않도록 옷으로 상처를 감췄다."

    "회복도 제대로 안 됐는데, 너무 무리를 한 듯했다."

    "그렇게 휘청이는 순간,"

    show char n default emb at top
    n "뭐야, 얘 상태가 왜 이래?"

    hide char
    "녹스가 공중에서 나타나, 나를 붙잡았다."

    "헤안은 놀라서 미처 반응조차 하지 못하고 있었다."

    "스승님은 예민하게 반응했다."

    show char e default bad at top
    e "당신, 뭡니까?"

    show char n default def at top
    n "요즘 따라 뭐냐는 말 참 많이 듣는 것 같네."

    show char n default smi at top
    n "얘 연구자 겸, 마탑에서 파견된 완전 센 마법사?"

    hide char
    "진짜 너는 미친놈이다."

    s "마탑에서 파견된 마법사고, 저를 감시하고 있는 사람입니다."

    s "지금은 사정이 있어서, 저랑 협력 중이고요."

    s "위험한 사람은 아닙니다. 아마···."

    "나는 녹스에 대해 간단한 설명을 덧붙였다."

    "헤안과 스승님은 탐탁지 않아 하는 것 같았다."

    show char n default emb at top
    n "그나저나 너 피가···."

    hide char
    "나는 녹스의 입을 막았다."

    "상황도 좋지 않은데, 내가 다친 걸로 괜히 일을 키우고 싶지 않았다."

    "녹스는 상황을 눈치챘는지, 입꼬리를 올리고 있었다."

    "그러고는 몸을 숙여, 내게 속삭였다."

    show char n default bad at top
    n "그래도 빨리 치료하는 게 좋을걸? 너는 치료 마법도 안 먹혀."

    s "됐어. 괜찮으니까."

    show char n default def at top
    n "흠···."

    hide char
    "나는 그를 뒤로하고, 헤안에게 현재 상황 보고와 기사단이 있는 곳으로의 안내를 부탁했다."

    "에런은 다시 부상자를 확인하러 자리를 떠났고, 녹스는 나를 따라왔다."

    scene bg camp out blood
    play music "bgm/ptsd6.mp3"
    "처참했다."

    "부상자가 많았다. 중상부터, 심하게는 신체 부위 하나를 잃은 것까지."

    "게다가 피가 고인 웅덩이가 가득한 바닥, 왕국과 제국 나눌 것 없이 미처 수습하지 못한 시신들이 넘쳐났다."

    "그중에는 상단으로 인해 잠시 머물던 민간인들도 있었다."

    "이전에 있었던 아디크 왕국의 정복과는 차원이 달랐다."

    "아직 시작조차 안 했는데도."

    s "죄송합니다···. 제가 자리를 비우지 않았더라면."

    show char h default des at top
    h "당신 탓이 아닌 걸 알고 계시잖습니까."

    hide char
    "이를 악물었다. 사실 내가 자리를 비우지 않았어도 결과는 똑같았을 거다."

    "그게 가장 분했다. 나는 황실에 휘둘리기만 하고 있고, 그 때문에 사람들이 무차별적으로 죽어 나가고 있다."

    "의미 없는 전쟁임에도 말이다."

    "황제의 욕심 하나만으로 이렇게 수많은 사람이 앞으로도 더 죽어 나가야 한다."

    "무력한 내 자신에게 죄책감이 덧씌워졌다."

    "지금껏 내가 감정적으로 행동했다는 사실도 깨달았다."

    "'타나를 위해서라도'라는 건 그저 핑계였을지도 모른다."

    show char n default def at top
    n "많이도 죽었네."

    show char n default def at top
    n "같은 제국군 아니던가? 제국인들도 참 별나."

    show char n default def at top
    n "안 그래?"

    show char h default bad at top
    h "말씀이 지나치시군요."

    hide char
    "헤안이 얼굴을 찌푸리며, 그의 무례를 지적했다."

    "그는 이 상황 자체를 심각하게 받아들이고 있지 않았다."

    "'전쟁 중재'가 임무인 자 아니었던가?"

    "나는 욱한 감정이 그대로 튀어나왔다."

    s "어, 그러게."

    s "근데, 너만큼 별난 게 있을까."

    show char n default def at top
    n "뭐?"

    hide char
    "그는 의미를 모르겠다는 듯, 고개를 삐딱하게 세웠다."

    s "네가 하는 일이 전쟁 중재라며."

    s "전쟁에 대해 알기나 해?"

    s "중재를 할 생각이 있기는 하고?"

    "한 번 트인 분노는 멈추지 않았다."

    s "사람을 연구 대상으로 보는 너한테는 무리겠지."

    s "고지식하신 마탑 분들은 인간 따위는 하등 생물로 보나?"

    s "그래서, 그딴 말을 쉽게 지껄일 수 있냐고."

    "왠지 심장 부근이 뜨거워지는 것 같았다."

    show char n default def at top
    n "우리는 오히려 인간을 높게 판단하는데 말이야."

    show char n default def at top
    n "그리고, 내가 말하지 않았던가? 우리는 인간들에게 직접 관여하지 않기로 했다고."

    show char n default def at top
    n "우리 같은 압도적인 강함이 개입되면, 인간의 본질을 흐릴 것이라는 판단 때문이야."

    show char n default def at top
    n "대신, 인간이 서로 충돌해서 멸망을 초래하지 않도록 '중재'라는 이름을 붙인 거지."

    hide char
    "그는 이전과는 달리 꽤 진중한 태도를 보였다."

    s "그렇다고, 네가 방금 저지른 무례가 없던 일이 되는 건 아니지."

    "그를 계속해서 쏘아붙였다."

    "내가 지금 괜한 화풀이를 하는 건 아닌지 생각해 봤다."

    "감정이 주체가 되지 않았다."

    show char n default def at top
    n "사과를 원해? 그럼 하고."

    hide char
    "그는 여전히 내 분노의 갈피를 잡지 못하고 있는 것 같았다."

    "마탑의 존재들은 인간의 규격에서 벗어난 존재들이라고 하던데···."

    "그는 아예 인간이 아닌 것만 같았다. 그의 언행들은 인간을 이해하지 못하는 것에 가까웠다."

    show char n default des at top
    n "내가 별난 건 맞아. 마탑 내에서도 특히 별난 편이거든. "

    show char n default des at top
    n "근데 그건···."

    hide char
    "그가 말하다 말았다."

    show char n default emb at top
    n "야, 야!"

    show char h default emb at top
    h "세레나님···?"

    play music "bgm/holy2.mp3"
    hide char
    "이상하게 내 주변에 빛무리들이 떠다니기 시작했다."
    show white at fadeInOut
    "이유는 알 수 없었다."

    play sound "sfx/heart.mp3"
    "다만, 심장이··· 금방이라도 터질 것 같았다."
    show red at fadeInOut
    "처음 느껴보는 고통에 어찌해야 할지를 몰랐다."

    "그때 녹스가 다시 입을 열었다."

    show char n default bad at top
    n "여기서 최대한 멀리 떨어지는 게 좋을걸? "

    show char n default bad at top
    n "저 마력에 휩싸이면 나 빼고 여기 있는 모두 다 개죽음을 당할 테니까."

    show char h default bad at top
    h "마력이요···? 세레나님은 괜찮은 거 맞습니까?"

    show char n default def at top
    n "어. 내가 지금부터 괜찮게 만들 거니까."

    hide char
    "녹스의 말에 헤안은 주변 부상자들을 챙겨, 함께 물러났다."

    "그리고 녹스가 내게 가까이 다가왔다."

    show char n default def at top
    n "야, 정신 차려. 그래야 내 사과를 받든 말든 하지."

    show char n default def at top
    n "그때 말했던 마력이 네 심장에서 날뛰기 시작했어."

    show char n default def at top
    n "아마 네 감정변동과 몸 상태 때문에 그런 것 같고."

    show char n default def at top
    n "네가 직접 그 힘을 바로 잡아보던가, "

    show char n default def at top
    n "아니면 전과는 반대로, 내가 네 마력을 흡수해서 진정시키던가."

    s "허억···."
    show red at fadeInOut
    hide char
    "나는 숨을 제대로 쉬기도 벅찼다."

    menu .m2:
        "그의 말도 제대로 들리지 않았다."
        "녹스를 밀쳐낸다.":
            "나는 그를 밀쳐냈다."
            "그저 모든 게 소음처럼 들렸고, 아무도 나를 도와줄 수 없을 거로 생각했기 때문이었다."

            s "저리가···."

            show char n default bad at top
            n "상태 보니까 전자는 안 되겠네."

            show char n default bad at top
            n "마력 좀 가져간다?"

            hide char
            "그는 내 목에 손을 대고, 마력을 흡수하기 시작했다."

            "고통이 줄어드는 듯했다."

            "하지만 그도 잠시, 끝없는 심장의 고통이 다시 찾아왔다."

            s "흣···."
            show red at fadeInOut
            "주변의 빛무리가 더욱더 커졌다."
            show white at fadeInOut
            show char n default bad at top
            n "이거 큰일이네···."

        "녹스를 끌어당긴다.":
            hide char
            "나는 그의 멱살을 잡고 끌어당겼다."
            "그저 이 힘을 식혀줄 사람이 필요하다고 본능적으로 느꼈기 때문이었다."
            with shake
            s "뭐가 됐든, 당장 가져가···!"
            

            show char n default def at top
            n "네가 허락한 거다?"

            scene nox_illust1
            $ persistent.UnlockImage['nox'][0] = True
            hide char
            "그는 내 볼을 짓누르고, 입을 맞췄다."

            "내가 거부했던 점막 접촉이었다."

            "집요하게 느껴졌다."

            "머리도, 심장도, 원래 있던 상처도 모두 말끔하게 잊히는 기분이었다."

            "하지만 그도 잠시뿐이었다."

            s "흣···."

            "또다시 끝없는 고통이 찾아왔다."

            "나는 무의식적으로 그의 혀를 깨물고 말았다."

            "그의 혀 끝에서 피비린내 맛이 났다."
            show char n default def at top
            n "나를 물라고 한 적은 없는데. 짐승이 따로 없네."

            "계속되는 고통과 함께 주변의 빛무리가 더욱더 커졌다."
            show char n default def at top
            n "미치겠네···."
    scene bg camp out blood
    "그 또한 당황한 것 같았다."
    n "끝이 안 보여."

    "그가 작게 혼잣말했다. 그러고는 내게 정신을 차리라는 듯 볼을 툭툭 건드렸다."

    show char n default def at top
    
    n "야, 네 마력이 끝도 없어."

    show char n default def at top
    n "이 이상 내가 흡수해 봤자, 아픈 시간만 길어질 거야."

    show char n default def at top
    n "이제는 선택권이 없어. 네가 직접 이 힘을 다루는 수밖에."

    show char n default def at top
    n "내 말 잘 들어. 가장 쉬운 방법을 알려줄게."

    show char n default def at top
    n "재채기하듯이, 심장에 있는 힘을 방출시키는 거야. 알겠어?"

    hide char
    "참 어처구니없는 설명이었다."

    "하지만 살기 위해, 녹스의 말대로 심장에 집중했다."

    play sound "sfx/magic.mp3"
    with shake
    "파열음이 들렸다. 나한테만 들린 건지, 모두에게도 들린 건지는 모르겠다."
    

    play sound "sfx/high.mp3"
    s "이거, 생각보다 더 아픈데···."
    show red at fadeInOut
    
    show white
    play sound "sfx/magic.mp3"
    #play music "bgm/브금 없음.mp3"
    "그 순간 눈앞이 점멸했고, 거대한 빛이 숲 전체를 덮어버렸다."

    play music "bgm/peace.mp3"
    "고요해졌다."

    "내 심장의 고통도, 주변도 모두."

    scene bg camp out night
    "정신을 차려보니, 내 몸에 있던 모든 상처는 온데간데없이 사라진 상태였다."

    "심장의 고통 또한 말끔히 사라졌다."

    "녹스는 어안이 벙벙한 표정이었다. 그와는 어울리지 않는 표정이다."

    "그때, 이쪽으로 헤안과 스승님이 달려왔다."

    show char h default emb at top
    h "대체 무슨 짓을 하신 겁니까? 세레나님은 괜찮아지신 겁니까?"

    show char e default emb at top
    e "이게 무슨 일입니까?"

    s "어···. 뭐 보이는 대로."

    hide char
    "멀쩡해 보이는 내 모습을 보고, 오히려 헤안은 당황한 듯 보였다."

    show char h default emb at top
    h "그렇다면 다행입니다."

    show char h default emb at top
    h "거대한 빛과 함께 모든 부상자의 상처가 마치 없던 일처럼 사라져 버렸습니다."

    show char e default emb at top
    e "심지어는 신체가 돌아온 사람도 있습니다."

    show char h default def at top
    h "혹시, 마법사님께서 하신 겁니까?"

    show char n default def at top
    n "아니. 내 힘이 아니야."

    show char n default smi at top
    n "이쪽 힘이지."

    hide char
    "그는 나를 가리켰다."

    "어렴풋이 느낄 수 있었다. 지금 내 몸에 변화가 생겼다고."

    "이상하리만치 가벼운 느낌과 함께, 뭐든 할 수 있을 것만 같은 기분. "

    "그때 누군가 외쳤다."

    show char knight default at top
    q "신께서 강림하셨다! 이건 축복이자, 기적이다!"

    hide char
    "미처 대피하지 못한 사람들이었다."

    play sound "sfx/-.mp3"
    "부상자들도 뛰어나와 그를 보더니, 나에게 환호와 찬사를 날리기 시작했다."

    "한참이나 난리가 났다."

    "헤안과 나는 재빨리 이 난장판을 진정시키고, 정리시켰다."

    "그 후, 한숨을 돌리고 있었다."

    show char n default bad at top
    n "야!"

    hide char
    "하지만 곧바로 녹스가 내 앞에 나타났다."

    show char n default bad at top
    n "그 힘, 평범한 인간의 것이 아니야."

    show char n default bad at top
    n "아무튼, 당분간은 그 힘 사용할 생각하지 마."

    s "왜? 또 연구에 쓰려고?"

    hide char
    "나는 괜히 그를 비꼬았다."

    "나에게는 이전의 앙심이 아직 남아있었다."

    show char n default bad at top
    n "하···. 다음번에 또 이러지 않는다는 보장이 없다고."

    show char n default bad at top
    n "계속 그렇게 굴 거면, 그냥 사용해 버리고 죽던가."

    s "됐어. 어차피 사용할 줄도 몰라."

    show char n default def at top
    n "그럼, 심장에 신경 끄고 살면 돼. 그 외에는 나도 좀 더 조사를 해봐야겠으니까."

    show char n default def at top
    n "그리고 아까는 미안. 됐지?"

    hide char
    "진심으로 미안한 게 맞는 걸까 의심이 갔다."

    s "뭐가 미안한지는 알아?"

    s "네가 어떻게 살아왔는지, 어떤 식으로 인간을 바라보는지는 모르겠지만···."

    s "여기에는 모두 간절한 사람뿐이야."

    show char n default def at top
    n "전부 다?"

    s "그래. 각자 사정이 있어서 이 전쟁에 참여하게 되었고, 반절 이상은 이 전쟁을 원하지 않아."

    s "그럼에도, 다들 아득바득 이 전쟁에 임하는 건 명예도 부도 아니야."

    s "그냥 살고 싶어서야."

    s "나도 그래. "

    s "살고 싶어. 그리고 살리고 싶어."

    s "그래서 나는 전쟁에 참여할 수밖에 없게 만든 이를 끌어내고, 모두를 살려낼 거야."

    show char n default smi at top
    n "풋···."

    hide char
    "그는 처음으로 제법 제대로 된 웃음을 보여주었다."

    show char n default smi at top
    n "그래, 그럼 네가 하나부터 열까지 다 알려줘."

    s "뭐?"

    show char n default smi at top
    n "인간에 대해서. 그리고 내가 전쟁에 직접 관여할 수 있는 타당한 이유를 말이야. "

    show char n default smi at top
    n "지금은 전쟁에 대해 어느 정도 이해가 갔어."

    show char n default smi at top
    n "네가 알려주면, 나도 내가 왜 별났는지 알려줄게. 마탑에 대해서도."

    show char n default smi at top
    n "당분간은 네 앞에 나타나지 않을 거야."

    show char n default smi at top
    n "왕국 쪽의 상황도 봐야 하고, 네 힘의 근원도 찾아봐야 할 것 같아서 말이야."

    show char n default smi at top
    n "그러니까, 다음에 만날 때는 나를 아군으로 만들 각오 정도는 해놔."

    show char n default smi at top
    n "나 고급 인력이거든. 놓치면 안 된다?"

    s "야, 나 아직 말 안 끝났거든?!"

    hide char
    "또다시 그는 자기 말만을 늘어놓고는 떠나버렸다."

    "하지만 기분이 나쁘지는 않았다. 그에게 어떤 변화가 일어난 것으로 보였기 때문이었다."


    "그렇게, 나는 영웅 취급을 받으며 지냈다."

    "기분이 나쁘지는 않았지만, 좋지도 않았다."

    "전쟁은 이제부터 시작이었기 때문에."

    $ persistent.ClaerChapter = max(10,persistent.ClaerChapter)
    return
