label chapter_8:
    "제목 : 전쟁의 민낯"

    scene black
    play music "bgm/sad4.mp3"
    "사실 그 어느 하나 쉬운 것이 없었다."

    "전쟁을 나가는 것도, 사람을 죽이는 것도."

    "하물며 가장 혐오하는 인간의 명령을 수행하는 것마저"

    "하고 싶지 않은 일이었다. 도망칠 수만 있다면 벗어나고 싶었다."

    "그러나 내겐 거부할 수 있는 선택권이 없었다."

    "명령에 수행하는 것. 그것만이 내가 할 수 있는 유일한 일이었다."

    "시간이 흐르고, 마침내 아디크 왕국을 정복하는 데 성공했다."

    "적의 병사들과 기사들은 차례대로 무너져갔다."

    show char knight default at top
    Character('기사단') "단장님 만세!"

    show char knight default at top
    Character('기사단') "만세!"

    hide char
    "분노는 나를 강하게 만들었다."

    "하지만 그럴수록 내 마음은 심연으로 떨어져 갔다."

    "고통스러워하는 사람들의 표정과 전장의 피비린내가 지워지지 않았다."

    "동료들 또한 그에 포함되었다."

    "죽음은 편을 가르지 않았다."

    scene bg camp out
    s "타나···."

    "타나의 죽음은 내 인생에서 가장 큰 비극이었다."

    s "할 수만 있다면 그놈의 몸을 갈기갈기 찢어버릴 텐데."

    "하지만, 황실은 타나의 죽음을 애도할 시간조차 주지 않았다."

    show char knight default at top
    q "황제께서 보내셨습니다."

    hide char
    "검은색 로브를 쓴 남자. 황제의 측근이 분명했다."

    "기척도 없이 다가온 것을 보아, 상당한 실력자였다."

    "그런 그가, 고급스러운 종이 하나를 내밀었다."

    "황제에게서 온 전보라니. 불안감이 엄습했다."

    s "···이번에는 또 무슨 일이지?"

    show char emp at top
    play Sound "sfx/book.mp3"
    Character('황제 다리우스') "예상보다 일이 더디게 진행되는구나."

    show char emp at top
    Character('황제 다리우스') "아디크 왕국을 정복하는 데 성공했더구나."

    show char emp at top
    Character('황제 다리우스') "그 다음엔 프라타히라 왕국을 정복해라. 10일이라는 시간을 주겠다. 이 이상 늦어지지 않길 바란다."

    show char emp at top
    menu .m0:
        "불가능하다는 답변을 내놓을 거라면, 살아서 돌아올 생각은 하지 않는 게 좋을 거다."
        "반항한다.":
            $ persistant.Likeability = {key:value+3 for key,value in persistant.Likeability.items()}
            hide char
            "프라타히라 왕국 정복은 안 그래도 하려던 참이었다. 나의 복수를 위해서."
            "하지만, 10일이라는 제한된 시간은 말도 안 되는 이야기였다."

            s "10일이라고? "

            show char knight default at top
            Character('황제 측근') "지금 명령을 거절하겠다는 뜻입니까?"

            s "소국이었던 아디크 왕국을 정복하는 데도 일주일이 걸렸어."

            s "물자 보급을 받을 시간까지 포함하면 분명 더 걸릴 테지."

            s "현실적으로, 규모가 더 큰 프라타히라 왕국을 정복하는데 10일이란 시간은 터무니없이 부족해."

            show char knight default at top
            Character('황제 측근') "못하시겠다면, 황녀님의 의사를 전달해 드리도록 하겠습니다."

            show char knight default at top
            Character('황제 측근') "다만, 좋은 대답은 못 들으실 겁니다."

        "······.":
            

            s "황제께 알겠다고 전해."

            hide char
            "또 잊고 있었다. 내게는 처음부터 선택지 따위는 존재하지 않는다는 것을."

            "그래서인지, 지원 요청에 대해서는 말도 꺼내지 못했다."

            show char knight default at top
            Character('황제 측근') "알겠습니다. "

            hide char
            "황제의 측근은 마지막 말을 끝으로 재빠르게 사라졌다."

            s "정말 감촉같이도 사라지네."

            "황제가 말한 10일이라는 시간은 아무리 계산해도 말이 되지 않았다."

            "군인을 소집하고, 보급을 요청하는 시간만 해도 최소 사흘이었다."

            "여기서 이동하는 시간까지 하면···."

            "······."

            play music "bgm/sad3.mp3"
            "그때 불현듯 타나를 죽였던 왕자가 떠올랐다."

            s "타나···."

            "나를 위해서 대신 죽은 아이."

            "강하고 믿음직했던 제국의 기사이자, 내 친우."

            "그 아이가 아니라 내가 대신 죽었어야 했다."

            "왕자의 칼날이 향한 목적지는 사실 나였으니까."

            "타나의 마지막 얼굴이 아직도 생생하다."

            "타나를 찔렀던 왕자와 미동도 없던 그 애의 손까지."

            s "타나를 죽인 그놈은 지금쯤 몸 편히 누워있겠지."

            "그렇게 생각하니 가만히 있을 수 없었다."

            "어떻게 해서라도 타나의 원수를 갚아줘야만 했다."

            "그것이 타나를 자유롭게 할 수 있는 유일한 방법일 테니."

            s "그래, 황제가 아니라 타나를 위해서 이 전쟁을 준비하겠어."

            "10일라는 시간은 어쩌면 충분한 시간이 될지도 몰랐다."

            "내 복수와 분노를 빠르게 사그라뜨릴 수 있는."

            s "헤안을 찾아가자."

            "그라면, 답이 보이지 않는 이 상황에서 완벽한 해답을 내놓을 것이 분명했다. "

            "나는 걸음을 재촉했다."

            "한시라도 빨리 프라타히라 왕국을, 아니 그 개같은 놈을 죽이고 싶었다."

            s "타나, 조금만 기다려줘."

            "내 분노는 점점 더 타오르고 있었다."

            "프라타히라의 왕자를 내 손으로 직접 죽이지 않는 이상,"

            "이 분노는 절대 잠재워지지 않을 것이 분명했다."

        "······.":
            "······."
    play Sound "sfx/footstep_grass.mp3"
    "나는 검을 챙기고, 헤안의 막사로 향했다."
    "부디, 나의 복수가 타나에게 닿을 수 있길."

    "기사의 이름을 걸고 맹세했다."

    scene black

    show char h default bad at top
    scene bg camp in
    play music "bgm/dis.mp3"
    h "그건 곤란합니다."

    hide char
    "모든 상황을 설명했다. 황제의 명령이라는 것도 포함해서."

    "물론 복수를 하겠다는 사적인 감정이 담기지 않았다고 하면, 거짓말이었다."

    "하지만, 그가 이리 단호하게 거절하는 것은 예상 밖의 일이었다."

    s "왜 거절하시는 거죠?"

    show char h default bad at top
    h "세레나님께서도 이미 알고 계시잖습니까."

    show char h default bad at top
    h "이 상황에서 프라타히라 왕국에 가는 건 너무 무모합니다."

    show char h default bad at top
    h "시간도 충분치 않은 상황이고요."

    s "당연합니다. 하지만···!"

    hide char
    "헤안은 씁쓸한 미소를 지으며 말했다."

    show char h default def at top
    h "전쟁이 끝난 지 얼마 되지 않았습니다. "

    show char h default def at top
    h "기사들도 휴식이 필요하지 않겠습니까. 잠시라도 쉬어가야 합니다."

    s "황제의 보복이 두렵지도 않으신가 보군요."

    show char h default def at top
    h "···저희는 황실에 맞서 싸우기로 한 거 아니었습니까?"

    hide char
    "나는 허를 찌르는 헤안의 말에 할 말을 잃었다."

    "그동안 분노에 휩싸여 정말 중요한 내 목적을 잊고 말았다."

    "그렇지만···."

    s "당신은 모를 겁니다. 저라고 좋아서 황제의 명령을 따르는 건 아니라는 걸요."

    s "됐습니다. 오늘 대화는 여기까지로 하죠."

    show char h default bad at top
    h "잠시만요, 세레나님!"

    scene black
    play Sound "sfx/clothes.mp3"
    hide char
    "나는 헤안의 만류를 뒤로 한 채 자리를 떠났다."

    play Sound "sfx/footstep_grass.mp3"
    "그의 다급한 목소리에 발걸음을 더 재촉했다."

    s "그래, 이게 내가 할 수 있는 최선이야."

    "나는 홀로 이 전쟁에서 승리할 수 있는 방법을 계획하기 시작했다."

    "시간이 없었다. 서둘러야만 했다."

    "그렇게 밤을 지새웠다."

    play music "bgm/ptsd3.mp3"

    scene bg camp out
    s "다친 기사들은 이곳에 남고, 당장 출정 가능한 인원만 모이도록 한다!"

    show char knight default at top
    Character('기사단') "네, 단장님!"

    hide char
    "내가 밤새워 고민한 결과는 다음과 같았다."

    "현재, 최근 제국에서 지원 보낸 병사들의 수는 약 5천 명 남짓."

    "그 중, 부상으로 인해 전투 불가능 인원을 제외한다면 약 3천 명 정도다."

    "그들을 데리고 먼저 원정을 떠나 있는 동안, 제국 국경에 있는 황실 기사단에 지원을 요청하면 된다."

    "그러면, 프라타히라 왕국을 가는 동안 조금이라도 시간을 벌 수 있었다."

    s "촉박하지만 이렇게 하면 기사들을 더 모을 수 있어."

    "아무리 황제라도, 원정 중인 군사의 지원 요청을 거부할 수는 없을 테니까."

    "그러나 헤안에겐 아직 그 어떠한 말도 전하지 못했다."

    "헤안의 조언이 계속 떠올랐지만, 그렇다 한들 황제의 압박을 무시할 수 없었다."

    "연이은 전투에 지친 기사단을 데리고 전쟁을 또 나갈 수 있을까."

    "물론 장담할 수 없는 결과였고, 걱정이 앞서기도 했다."

    scene black
    "제발, 잘 돼야만 해···."

    scene bg camp out night
    play Sound "sfx/footstep_grass.mp3"
    "밤을 지새우며 주변을 걷던 중, 헤안이 내 앞을 가로막았다."

    show char h default des at top
    h "세레나님, 잠깐 얘기 좀 할 수 있을까요?"

    s "···물론이죠. 가능합니다."

    hide char
    "잔뜩 긴장된 목소리, 하지만 그 긴장감을 꾹꾹 눌러 담는 듯한 표정."

    "헤안을 마주하니 가슴이 울렁거렸다."

    "마치 내가 잘못된 선택을 내렸다고 말하는 것 같았다."

    show char h default des at top
    h "아무리 고민해 봐도 저는 당신의 계획을 존중할 수 없습니다."

    show char h default des at top
    h "차라리, 황제에게 시간을 조금만 더 늘려달라고 말해보는 건 어떠십니까?"

    hide char
    "며칠간 내 행동에 아무런 제약이 없던 것은, 헤안 스스로 고민하기 위함이었나."

    "헤안은 여전히 곧바로 출정하는 것에 부정적인 의견을 내놓았다."

    "그가 하는 말이 틀렸다고 생각하지 않는다. 어쩌면 옳은 말이었다."

    s "틀린 말은 아니군요."

    show char h default def at top
    h "그렇다면 계획을 철회하시는 겁니까?"

    s "헤안님은 황제라는 자를 잘 모르시는 것 같습니다."

    s "이 이상 지체했다간 제국을 개혁하기도 전에, 저희가 황실 기사단에 공격받고 말 거에요."

    s "황제는 같은 편이라도, 가차 없습니다."

    s "쓸모없는 말은 버리는 게 그의 철칙이니까요."

    s "우리 기사단만으로, 황실 기사단을 이길 수 있다고 확신할 수 있으십니까?"

    show char h default def at top
    h "······."

    hide char
    "헤안은 고개를 떨궜다."

    s "어쩔 수 없습니다. 제 계획에 동참해 주셔야만 합니다."

    show char h default des at top
    h "죄송합니다."

    play Sound "sfx/clothes.mp3"
    hide char
    "헤안은 갑작스레 나를 둘러업었다."
    with shake

    s "헤안? 이게 지금 무슨 행동이죠?"

    show char h default def at top
    h "잠시만 쉬고 계세요. 일이 정리되면 제가 다시 데리고 오겠습니다."

    hide char
    "강압적인 힘. 그는 진심으로 나를 둘러업고 있었다."

    "이런 식으로 나를 막으려 들 줄을 상상이나 했겠는가."

    "나는 온 힘을 다해 발버둥 쳤다."

    "그러나 아무리 도망치려고 애를 써봐도, 소용없는 짓이었다."

    s "제가 당신보다 상급자라는 사실을 잊은 겁니까?"

    show char h default def at top
    h "부디 저를 용서하지 마시길."

    s "···절대 용서하지 않을 겁니다."

    show char h default des at top
    h "······."

    play Sound "sfx/punch.mp3"
    hide char
    "헤안은 내 목덜미를 세게 내리쳤다."
    with shake
    show red at fadeInOut

    scene black
    "난 그로 인해 기절하고 말았다."

    "헤안의 표정이 좋지 않았다."

    show char h default des at top
    h "혹시라도 내 생각이 틀렸다면···."

    hide char
    "헤안은 즉시 고개를 저었다. 아무리 생각해도 현재 군인들 상태로 전쟁에 나가는 건 어림도 없었다."

    "헤안은 걸음을 옮겨 세레나의 막사로 향했다."

    "그녀를 안전한 곳에 옮겨둔 후에, 작전을 다시 세우기로 했기 때문이었다."

    show char h default des at top
    h "저를 용서하지 마세요, 세레나."

    play music "bgm/tension4.mp3"

    hide char
    "기분 나쁠 정도로 음침한 하늘이 드리워졌다. 텁텁한 공기는 사람들의 폐를 어지럽혔다."

    "마치, 어떤 일이라도 일어날 것처럼 하늘은 불길한 징조를 암시했다."

    "그러던 중, 제국이 세레나 기사단에 직접 황실 기사단을 보냈다는 소식이 들려왔다."

    "당연히, 유시크 기사단은 저들이 정복 전쟁을 돕기 위한 지원군이라고 생각했다."

    "하지만, 세레나의 말은 틀리지 않았다."

    "황제는 같은 편이라도 가차 없었다. 쓸모없는 말은 가치가 없으니."

    show char knight default at top
    play Sound "sfx/war_shout.mp3"
    Character('기사단원1') "제국의 황실 기사단이 우리를 공격하고 있다!"

    show char knight default at top
    Character('기사단원2') "뭐? 우리는 왕국 기사단이 아니잖아!"

    show char knight default at top
    Character('기사단원1') "다들 대비해! 무기를 챙겨!"

    hide char
    "경비를 담당하던 기사단원의 외침이 기지 전역에 울려 퍼졌다."

    scene bg camp in
    play Sound "sfx/sword_hit2.mp3"
    "나는 귀가 찢어질 듯한 소음에 눈을 떴다."

    "막사 안이었다. 밖은 이상할 정도로 소란스러웠다."

    s "설마···.!"

    "다급한 마음에 밖으로 뛰쳐나갔다."

    scene bg camp out blood
    "아비규환이었다. 황실 기사단들과 싸우고 있는 기사단이 보였다."

    show char h default bad at top
    h "세, 세레나님···!"

    s "헤안!"
    with shake

    hide char
    "한 황실 기사가 헤안의 뒤로 달려들었다."

    play Sound "sfx/sword_damage2.mp3"
    "나는 그 순간, 검을 집어 들고 헤안을 해치려던 이의 목을 내리쳤다."

    show char h default emb at top
    h "감사합니다···."

    s "도대체 어떻게 된 거죠?"

    show char h default bad at top
    h "황실 기사단이 쳐들어왔습니다! 제국의 기사단인 걸 밝혀도 저희를 공격하더군요."

    s "설마···."

    hide char
    "나는 황급히 무장을 갖추고 중앙으로 뛰어갔다."

    "황실 기사단의 깃발이 바람에 휘날리고 있었다."

    s "어째서··· 우리의 계획이 들키기라도 한 걸까."

    "헤안을 제외하면 그 누구에게도 나의 목적을 밝히지 않았다."

    "스승님에게 말하려 했으나, 망설이는 바람에 전하지 못했다."

    s "역시 시간을 너무 지체했나 봅니다."

    show char h default bad at top
    h "세레나님! 일단은 어서 도망가시는 게 좋을 것 같습니다. 이대로 가다간 전멸입니다."

    hide char
    "헤안의 다급한 목소리, 그것은 내 귀에 들리지 않았다."

    "그때, 불현듯 내 한 생각이 내 머릿속을 스쳐 지나갔다."

    s "어쩌면 황제는 내게 시간을 줄 마음 같은 건 없었던 걸지도 몰라."

    "황제가 나를 마음에 들어 하지 않는다는 것은 알고 있었다."

    "그럼에도 기사로 나를 불러 전쟁에 참전시키는 걸 보니, 아직까진 제 쓸모대로 사용할 줄 알았는데."

    "애초부터, 프라타히라 왕국을 정복하라는 것이 주목적이 아니었을지도 모른다."

    "황제는 우리를, 정확히는 이 전장에서 나를 죽이려고 하는 것이 틀림없었다."

    "정확한 이유는 알 수 없지만, 아마 그의 목적을 이루기 위해서···."

    s "모두 방어 태세를 준비해! 전열을 갖춰!"
    with shake

    "나는 큰 목소리로 외쳤다."

    "하지만 기사단의 대열은 이미 혼란에 빠져 있었다."

    play Sound "sfx/war_shout.mp3"
    "황실 기사단은 우리를 향해 무자비하게 공격해 왔다."

    "그들의 훈련된 움직임은 전장에 압도적인 존재감을 드러냈다."

    "우리 기사단은 이미 지쳐있는 상태였기에 제 실력이 발휘되기란 불가능에 가까웠다."

    play Sound "sfx/sword_hit2.mp3"
    "방패와 검이 부딪히는 소리가 사방에서 울려 퍼졌다. 전장은 순식간에 피로 물들었다."

    show char h default bad at top
    h "후퇴해야만 합니다!"

    hide char
    "헤안이 다급하게 다가와 내게 외쳤다."

    s "여기서 도망치면 정말 끝입니다. 기사단원들이 더 죽어 나갈 거라고요!"

    "나는 이를 악물고 답했다."

    "하지만 상황은 점점 안 좋아졌다. "

    play Sound "sfx/war_shout.mp3"
    "곳곳에서 동료들의 비명이 들려왔다. 나의 손은 이미 피로 물들고 있었다."

    "그 피가 내 검을 더 무겁게 만드는 것 같은 착각마저 들 정도였다."

    play Sound "sfx/war_horn.mp3"
    "그때, 땅이 흔들릴 정도로 거대한 소음이 울려 퍼졌다."

    show char knight default at top
    scene bg bf sunset
    play Sound "sfx/war_shout.mp3"
    q "지금이 기회다! 제국민들에게 복수를!"
    with shake

    show char knight default at top
    q "제국민들에게 복수를!"

    hide char
    "프라타히라 왕국의 기사들이었다."

    "푸른색의 문양,"

    "분명한 프라타히라 왕국의 색이었다."

    "숨어있던 프라타히라 왕국의 병력이 합세했다."

    "그들은 이미 제국의 내분을 눈치채 기회를 엿보고 있었던 것이다."

    s "하필 이런 때에···."

    "이제 우리의 적은 둘이나 되었다."

    scene black
    "모든 것이 엉망이었다."

    s "······."

    scene bg bf sunset
    play Sound "sfx/sword_hit2.mp3"
    play music "bgm/sad3.mp3"
    "나는 절망적인 마음으로 전장을 둘러보았다."

    "끝까지 최선을 다했지만, 결국 체력이 떨어지고 말았다."

    play Sound "sfx/sword_wind.mp3"
    "그때, 적국의 기사로부터 기습 공격이 들어왔다."

    "다행히 급소는 지나쳐갔다."

    "방금 건, 정말로 운이 좋았다고 봐야 했다."

    s "내가 조금만 더 정신을 차렸어도!"

    s "아니, 애초에 헤안이 날 방해하지만 않았어도···."

    "하지만 무슨 소용이 있겠는가. 이미 상황은 극악에 다다랐다."

    "헤안을 원망하려고 한들, 그의 말이 틀린 것은 없었다. "

    "오히려 잘못된 판단을 한 건 내 쪽이었을지도 모른다."

    "나는 나를 향해 검을 겨누는 기사를 마주 보며 몸을 지탱하기 위해 애썼다."

    "내가 할 수 있는 건 이제 아무것도 없었다."

    s "이대로 끝나는 걸까···."

    play Sound "sfx/footstep_grass.mp3"
    "그렇게 뒤늦은 후회를 하던 중, 낯선 남자가 내게 다가왔다."

    "내 자세는 완전히 무너져 내렸음에도, 곧바로 칼날을 세웠다."

    "로브를 깊게 눌러쓰고 있어, 얼굴이 보이지는 않았다."

    "적인지 아군인지도 구분이 되지 않았다."

    show char a default emb at top
    q "···너 여기서 뭘 하는 거야?"
    hide char
    menu .m1:
        
        "희미하지만 익숙한 음성이 들렸다."
        "너는···.":
            s "너는···."
            "나는 힘겹게 대답했다."

            show char a default des at top
            a "······."

            play Sound "sfx/clothes.mp3"
            hide char
            "그러나 그는 대답하지 않고 나를 부축하며, 걸음을 옮겼다."

            play Sound "sfx/footstep_grass.mp3"
            "하고 싶은 말이 많았지만, 입은 떨어지지 않았다."

            "그가 누군지 어렴풋이 알 것 같았다."

            "지금 왜 여기 있는지, 그의 정체가 무엇인지는 중요하지 않았다."

            "몸에 한계가 오기 시작한 듯했으니까."

        "그때 그 변태 자식···.":
            $ persistant.Likeability['adrian'] +=10
            s "그때 그 변태 자식···."
            "목소리로, 그를 단번에 알아봤다. 조난당했을 때 함께했던 그 남자였다."

            "나는 정신을 차리기 위해 애썼지만, 몸이 말을 듣지 않았다."

            show char a default bad at top
            a "야, 야!"

            play Sound "sfx/clothes.mp3"
            hide char
            "나는 그가 부축해 주기도 전에, 스스로 몸을 다시 세웠다."

            "악을 썼다고 보는 게 맞았다."

            "누구냐고, 묻고 싶었다."

            "정체가 뭐냐고, 왜 여기 있는 거냐고. 따지고 싶었다."

            "오랜만에 봐서 반가웠지만, 내 목소리는 그에게 닿지 못했다."

            "대신 거칠게 숨을 몰아쉬었다."

            play Sound "sfx/footstep_grass.mp3"
            "그는 한숨을 쉬고, 나를 부축하며 걸음을 옮겼다."

    "누가 적이고 아군인지 모를 상황 속에서, 그만큼은 그냥 믿어보기로 했다."
    "이전에도 우리는 서로를 도왔으니까."

    scene black
    s "···으."

    "고개를 떨구고 그에게 기대고 있으니, 주변의 소리가 죄다 묻혀서 들렸다."

    "하지만 다시 일어서야만 했다."

    "지금 이러고 있는 동안에도 내 기사단원들은 하나둘 죽어가고 있을 테니."

    scene bg bf sunset
    "호흡을 내쉬며, 집중했다. 다시 복귀해야겠다고 다짐했으니까."

    "그렇게 정신을 차리니, 나를 부축해 주던 이가 누군가와 언성을 높이며 대화를 나누고 있었다."

    q "···니다."

    show char a default bad at top
    a "내가 알아서 할게."

    play music "bgm/ptsd2.mp3"
    hide char
    "나는 고개를 들었다."

    play Sound "sfx/heart.mp3"
    "심장이 미칠 듯이 빨리 뛰기 시작했다."

    "낯설지만 분명한 얼굴."

    "타나를 죽였던 프라타히라 왕국의 왕자."

    "찬물을 끼얹은 듯이, 내 머릿속은 고요해졌다."

    "죽여야 해."
    show red at fadeInOut
    "그러고는 곧바로 실행에 옮겼다."

    play Sound "sfx/sword_wind.mp3"
    "칼을 바짝 쥐고, 그의 곁에 있는 새끼에게 달려들었다."

    play Sound "sfx/sword_hit.mp3"

    "하지만, 보기 좋게 공격이 막혔다."

    "힘이 모자란 탓이었다."

    show char a default emb at top
    a "이게 무슨 짓이야!"

    s "너도, 프라타히라 사람이었구나."

    s "심지어 왕자의 측근···."

    show char a default des at top
    a "······."

    hide char
    "그는 내 말에 별다른 부정을 하지 않았다."

    show char a default def at top
    a "너야말로 에프탈 제국의 황녀였던데."

    s "···하하."

    hide char
    "나도 모르게 웃음이 나왔다."

    "그를 믿었던 내가 바보같이 느껴졌기 때문일까."

    "모든 게 허무해졌다."

    play Sound "sfx/sword_damage.mp3"
    "그렇게 무방비함을 취하고 있을 때, 왕자가 내 옆구리에 단도를 박아 넣었다."
    with shake
    show red at fadeInOut
    "순식간이어서, 방어조차도 못 했다."

    show char a default emb at top
    a "···!"

    hide char
    "내 몸은 제대로 휘청했다."

    "살기 위해서는 도망가야만 했다. 하지만, 저 둘에게서 도망치기란 불가능이었다."

    s "흐윽···."
    show red at fadeInOut
    show char a default bad at top
    a "야, 일단 여기를 벗어나."

    show char a default bad at top
    a "쟤는 내가 막을 테니까."

    hide char
    "그는 왕자의 측근임에도, 내게 속삭였다."

    play Sound "sfx/clothes.mp3"
    "그러고는, 그가 왕자에게 무어라 말하며 왕자를 붙잡았다."

    play Sound "sfx/footstep_grass2.mp3"
    "나는 그 틈을 타, 숲을 향해 달렸다."

    scene black
    "죽을 듯이 달렸다. 앞이 점점 안 보이기 시작했다."

    play Sound "sfx/heart.mp3"
    "몸이 통제되지 않았다."

    "이대로 가다간 정말 죽을 수도 있겠다는 생각이 들었다."

    $ persistent.ClaerChapter = max(9,persistent.ClaerChapter)
    return
