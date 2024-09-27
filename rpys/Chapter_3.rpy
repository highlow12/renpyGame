﻿label chapter_0:
    "제목 : 정체불명의 마법사와 공자"

    scene bg kingdom way
    play Sound "sfx/sword_throw1.mp3"
    play music "bgm/nox2.mp3"
    "휘익 - "

    "나는 인기척이 느껴지는 곳으로 가지고 있던 단검을 날렸다."

    "단검은 공중에서 멈췄고, 알 수 없는 누군가의 인영이 점점 드러났다."

    show char n default bad at top
    q "너, 대체 정체가 뭐야?"

    hide char
    "짜증을 내는 듯한 말투였다."

    "동시에, 재미있는 것을 발견했다는 듯한 시선이 느껴졌다."

    "그의 신원을 파악해 보려 했지만, 로브를 단단히 고정한 모양인지 얼굴을 자세히 볼 수 없었다."

    menu .m0:
        "나는 굳이 황궁에 침입한 자에게 여유를 주고 싶지 않았다."
        "너야말로, 뭐 하는 녀석이야?":
            "너야말로, 뭐 하는 녀석이야?"
            show char n default smi at top
            q "궁금해?"

            s "아니, 네 녀석한테 쓸 시간 따위 없어."

        "공격한다.":
            "공격한다."
    play Sound "sfx/sword_hit1.mp3"
    hide char
    "챙 -"
    show char n default smi at top
    q "아까부터 다짜고짜 공격이라니, 너도 제정신은 아니구나?"

    hide char
    "분명 그의 가슴을 노린 공격이었다."

    "그러나 눈앞에는 커다란 불투명한 방어막이 내 칼을 가로막고 있었다."

    s "마법사?"

    "마법사라는 것 따위는 딱히 내 안중에는 중요하지 않았다. "

    "침입자를 처리하는 것. 그게 우선이었다."

    play Sound "sfx/sword_hit2.mp3"
    "나는 쉴 새 없이 그에게 공격을 이어갔다."

    "마법에 막히기는 했지만, 그가 점점 뒤로 밀려나는 게 보였다."

    show char n default bad at top
    q "그만 좀 해. 나도 상대해 주는 데에 한계가 있다?"

    s "그럼 힘 빼지 말고, 나한테 깔끔하게 잡혀주면 돼."

    show char n default bad at top
    q "말이 전혀 안 통하는 아가씨네."

    hide char
    "그는 순간이동 마법으로 도망치려는 것 같았다. 아직 여유가 넘치는 모양이었다."

    "나는 급한 마음에 칼은 내던지고 그의 로브를 향해 손을 뻗었다."

    play Sound "sfx/clothes.mp3"
    "휘익 - "
    with shake

    "어이없게도, 그는 뒤로 고꾸라지며 순순히 잡혀줬다."

    "당황스러웠다. 힘을 잔뜩 실었던 공격들은 다 막아냈으면서, 그냥 맨손으로 붙잡는 거에는 잡힌다고?"

    "마법사들은 원래 이렇게 약한가?"

    show char n default ang at top
    q "내 마법이 무효화 됐다고?"

    hide char
    "당황스러움을 느끼던 나와 비슷하게, 그 또한 어리둥절해 보였다."

    "맥 빠진 그의 표정이 어리둥절함을 증명했다."

    "나는 그 순간, 이 기회를 놓치지 않고 침입자 녀석의 목덜미를 세게 붙잡았다."

    s "잡았다, 이 침입자 자식아."

    show char n default ang at top
    q "야, 야! 잠깐만!"

    hide char
    "시끄러운 소리가 났다. "

    "그렇게 어쩌다 보니, 나와 침입자는 황궁 정원에서 잔뜩 얽혀 뒹굴고 말았다."

    "정확히는 내가 그의 멱살을 쥐고, 그의 몸 위에 올라타 있었다."

    "나는 그의 로브를 벗기기 위해 멱살을 위로 더 끌어올렸다. "

    "그는 내가 멱살을 끌어올리든 상관하지 않고, 무언가 골똘히 생각하는 것처럼 보였다."

    play Sound "sfx/cloth.mp3"
    "로브가 완전히 벗겨지자, 고혹적인 은빛의 머리카락이 흩날렸다."

    "동시에 예민한듯 나른해 보이는 눈이 나와 마주쳤다."

    "순간 무언가에 홀린 듯한 기분이었다."

    "내가 잠깐 그에게 홀린 사이, 그가 순식간에 자세를 역전시켰다. 방심했다."

    "칼을 내던진 지는 오래였다. 나는 완전한 무방비 상태였다."

    "그가 얼굴을 붙여왔다. 나는 눈을 질끈 감았다."

    show char n default def at top
    q "킁킁-"

    s "?"

    show char n default def at top
    q "아~ 뭐지? 무효화 마법을 달고 있는 것도 아닌데? 너 무슨 짓을 한 거야?"

    show char s default bad at top
    s "알려줄 의무가 있나?"

    show char n default def at top
    q "흠. 괜히, 황실 대표인 게 아닌가 보네. 아님 뭐 특별한 힘이라도 있는 건지···."

    hide char
    "이미 내 존재에 대해 알고 있는 모양이었다. 그리고 그가 궁금해하는 건 내가 아니라, 내 ‘정체’에 관한 것 같았다."

    show char n default def at top
    q "아니다. 어차피 감시해야 하는데, 실험체로 두고 보면 되겠네."

    hide char
    "그는 계속해서 알 수 없는 혼잣말을 늘어놓았다."

    "불만을 표출하려던 찰나, 그가 자신의 신원을 드러냈다."

    show char n default def at top
    q "녹스."

    show char n default def at top
    q "마탑에서 파견 나온 마법사야."

    hide char
    "그는 마탑을 증명하는 펜던트를 내게 내밀며, 어린아이와도 같은 천진난만한 웃음을 짓기 시작했다."

    s "마탑···?"

    "평범한 마법사도 아니고, 마탑에서 파견 나온 마법사라니···. 머리가 지끈거렸다."

    "마탑은 어디에도 속하지 않는 자유로운 마법사들이 대륙 곳곳에 세운 것이었다."

    "또한 그들은 에프탈 제국에 비하는, 독자적인 강력한 힘을 지녔다."

    "아니, 사실은 제국조차도 그들의 상대가 안될지 모른다."

    "본디 그 무엇에도 얽매이지 않고, 세상의 모든 것들을 탐구하는 자들."

    "그것이 마탑의 마법사다."

    "그러나 마탑의 마법사들은 평범한 인간들과 자신들의 힘의 격차를 인지하기 시작했고, 그들 스스로에게 책임의 의무를 부여했다."

    "제법 책임감이라는 것을 지닌 괴짜들이었다."

    "그들이 부여한 책임의 의무는 바로, ‘조율’이었다. 대륙 내의 혼란을 조율하며, 인간들의 발전을 도모하는 것. "

    "그렇기에, 최근 제국의 전쟁이라는 파격적인 행보는 마탑에게 당연히 거슬릴 수밖에 없었다."

    "마법사가 언젠가 나설 것이라고는 생각했지만, 벌써 이런 식으로 감시하고 있을 줄은 몰랐다."

    "결국 나는 그의 입에서 ‘마탑’이 나온 순간부터 어떠한 행동도 취할 수가 없었다."

    "마탑의 의무인 ‘조율’에는 어떠한 세력도 간섭할 수 없기 때문이다. 설령 그것이 현재 가장 강력하다는 제국의 황제라 해도."

    "나는 한숨을 크게 쉬었다."

    s "여태 제가 실례했군요. 죄송했습니다."

    s "그럼, 이만 비켜주세요."

    show char n default smi at top
    q "아, 아. 그래야지."

    play Sound "sfx/cloth.mp3"
    hide char
    "녹스와 엉겨 붙어 있던 몸이 떨어졌다."

    "그는 어딘가 묘하게 들뜬 표정이었다. "

    "사람 참 약 오르게 하는 마법사였다."

    s "근데, 음침하게 숨어서 돌아다니지는 마세요."

    s "또 나한테 들킬라."

    "비웃음을 흘려주며, 빠른 걸음으로 자리를 떴다."

    play Sound "sfx/heart.mp3"
    "나답지 않은 언행이었다. 괜히 심장이 쿵쿵거렸다. "

    scene black

    show char soldier default at top
    scene bg noble bed yellow day
    play music "bgm/ptsd3.mp3"
    Character('기사단원') "단장님, 출정을 준비하라는 전언입니다. "

    s "뭐?"

    show char soldier default at top
    Character('기사단원') "아디크 왕국를 향한 제국 영토 확장 출정이라고 합니다."

    hide char
    "반란군을 잠재운 지 얼마나 됐다고 또다시 등을 떠미는 지, 그들이 역겹게만 느껴졌다."

    "화가 났다. 하지만, 이 분노는 표출될 수 없다는 것을 잘 알고 있다."

    "황실의 대표가 되겠다고 한 순간부터 각오해야 할 일이었다. 내게 거절할 수 있는 선택지는 없다."

    "그들의 명령에만 충실히 따라야 할 뿐."

    "다만, 지금 상황에서 걱정이 되는 건 내 신뢰였다. "

    "저번 반란군 진압에서 보여줬던 한없이 가벼운 나의 나약함은, 황실 기사단장이라는 무거운 직책과는 거리가 멀었다."

    "모든 기사단원이 나를 신뢰하지 못하는 것은 당연한 수순이었다."

    "나 같아도 목숨을 내걸어야 하는 전장에서, 그런 기사단장은 사양이었다."

    "출정 전에, 바로 잡아야만 한다."

    "짧은 시간 내에 모두에게 신뢰를 주는 것은 불가능하다."

    "하지만 그렇다고 가만히 있는 것 또한 멍청한 짓이다."

    "내가 전할 수 있는 진심을 그들에게 직접 보여줘야만 한다."

    "적어도, 내가 이 전쟁을 가볍게 생각하고 있지 않다는 사실만 전해져도 충분했다."

    s "알겠다. 기사단 전원 연무장으로 집합하라 전해."

    scene bg camp out day
    "시간이 얼마 지나지 않아, 재빠르게 기사단 전원이 연무장으로 집합했다."

    "두려움을 가득 담은 눈을 하고 있는 사람, 굉장히 앳되어 보이는 사람, 알 수 없는 자신감에 가득 차 있는 사람, 삐딱한 자세로 불평을 늘어놓는 사람. 그리고 그 외의 다양한 사람들."

    "비록 지금 기사단이라는 공통으로 묶여있지만, 각자 저마다의 사정으로 모여 있는 사람들이었다."

    "나 또한 별반 다르지 않았다."

    "하지만, 이제부터는 이들 모두가 나 한 명에게 의지하여 목숨을 걸어야 한다."

    "나는 바보 같게도, 이제야 기사단장이라는 이름의 무게를 실감하기 시작했다."

    "억지로 끌려 나와 되고 싶지도 않은 황실 대표 기사단장이 됐지만, 적어도 이들 앞에서는 나약해져서는 안 된다. "

    "그게 내가 할 수 있는 최소한의 예의다."

    menu .m1:
        play music "bgm/ptsd2.mp3"
        "모두를 마주하고 난 후에야, 나는 간신히 몸을 움직였다."
        "칼집의 끝을 땅에 세게 내리친다":
            "큰 소리 때문에 모두가 얼떨떨하게 쳐다볼 뿐, 집중이 되지는 않았다."
            "하지만 나는 이 틈이라도 이용해서, 고개를 숙였다."

        "고개를 숙인다.":
            "고개를 숙인다."
    "연무장이 술렁였다. 황실 기사단장이라는 위치에 있는 자가 고개를 숙인 것에 대한 놀라움인 것 같았다. "
    s "제가 미덥지 않다는 거 잘 알고 있습니다. 실제로 그런 모습도 보였습니다. 변명하지 않겠습니다. 단장으로서 기사단원 전원에게 사과드립니다."

    "숨을 크게 들이쉬었다."

    s "앞으로는 이런 고개를 숙이는 일 따위는 하지 않겠습니다. 그만큼 각오하겠습니다. 저는 그저, 지금 바라보고 있는 이 기사단원 모두가···."

    s "다시 이 황궁의 연무장으로 무사히 돌아왔으면 합니다."

    s "앞으로는 도망치지 않겠습니다. 기사단장이란 직책의 무게를 감당하겠습니다. 부디 저를 믿어주시길 바랍니다."

    "분명, 흔들리는 목소리였을지도 모른다. "

    "그럼에도, 이 흔들리는 목소리에 흔들리는 마음이 있기를 바랐다."

    show char h default def at top
    play Sound "sfx/clap.mp3"
    hide char
    "짝짝짝 - "

    "연무장 뒤편의 큰 나무 뒤에서, 누군가가 손뼉을 치며 앞으로 걸어 나왔다."

    "그는 제국의 하나뿐인 공작가, 레이워스 가문의 둘째 공자 헤안 레이워스였다."

    "그 또한 이유는 모르지만, 귀족을 대표하여 전쟁에 함께 출정하게 되었다고 들었다. "

    "다만, 같은 기사단에 속한지는 몰랐던 일이었다."

    "그는 내게 점점 다가오더니, 나에게만 들리게 속삭였다. "

    show char h default def at top
    h "처음 뵙겠습니다. 헤안 레이워스입니다. 억지로 나온 사람치고는 꽤 본격적이시군요, 세레나 단장님."

    hide char
    "다음으로는, 연무장 모두에게 들리도록 언성을 높였다."

    show char h default smi at top
    h "저번 반란군의 일은 모르겠습니다만, 단장님께서 굳게 다짐하신 게 있으신 것 같으니 저는 믿고 따라보도록 하겠습니다."

    hide char
    "묘하게 나를 비꼬는 듯했지만, 결국엔 동조하는 분위기를 만들어냈다."

    "그래서였는지, 기사단원들은 전원 기사의 맹세를 외치기 시작했다."

    "완벽한 신뢰는 아니겠으나, 지금은 이것만으로도 충분하게 여겨졌다."

    "나는 어찌 됐든 헤안에게 도움을 받은 것 같아, 작게 감사의 의사를 표했다."

    show char s default smi at top
    s "감사합니다."

    hide char
    "헤안은 고개를 끄덕임과 동시에 내게 충고를 던졌다."

    show char h default def at top
    h "앞으로는 기사단원들에게 빈틈이라도 보여선 안 되실 겁니다. 명심하십시오. 그럼 잘 부탁드리겠습니다."

    hide char
    "헤안의 말에 다시 한번 정신을 차렸다. 나쁜 사람 같지는 않았다."

    scene bg forest winter day
    "며칠이 지나고, 우리 기사단은 아디크 왕국의 국경지대로 향하게 되었다."

    "그곳은 눈이 덮인 지형이었기에 많은 준비가 필요했다."

    play music "bgm/sad3.mp3"
    "그렇게, 우리는 사흘 정도를 내리 이동했다. "

    "목적지였던 아디크 왕국 국경에 다다르기 시작했다."

    play Sound "sfx/wind.mp3"
    "하지만, 점점 눈보라가 휘몰아쳐 우리의 길을 가로막았다."

    "나는 더 이상 움직이는 데에 한계가 있을 것이라고 판단했다. "

    show char s default bad at top
    s "기상악화로 더이상의 이동은 어려울 것 같습니다."

    show char h default bad at top
    h "예. 마침 기사단원들 대다수도 지친 모양입니다."

    show char e default def at top
    e "근처에 기후 영향을 덜 받는 지대가 있습니다. 그곳에 막사를 펼치고 쉬어가는 게 좋겠습니다."

    hide char
    "당연하게도 헤안과 에런은 기사단 내에서 높은 직급에 해당했고, 기사단과 관련된 사항들은 함께 논의해야 했다."

    "그들에게 자격이 없다거나, 일을 제대로 하지 않는다는 것과 같은 문제가 있는 것은 아니다. "

    "그저 내 자신이 에런에게 어쩔 수 없는 거리감을 느꼈다."

    "한마디로, 어색하고 불편했다. "

    "그를 더 이상 감정적으로 대하지 않기로 다짐했지만, 그것을 실천하기까지에는 오랜 시간이 걸릴 것만 같다."

    show char s default def at top
    s "알겠습니다."

    hide char
    "그와의 시선을 제대로 마주하지 않은 채, 대답했다."

    "감정을 최대한 드러내지 않기 위함이었으나, 이 자리에 있는 모두가 눈치를 챘을 것이 분명했다."

    menu .m2:
        "나는 애써 상황을 유연하게 만들기 위해···."
            show char s default def at top
        "헤안에게 말을 걸어, 시선을 분산시킨다.":
            s "헤안님, 기사단원들 상태가 어떻죠? 이동할 수 있는 정도인가요?"
            show char h default def at top
            h "다들 지친 정도입니다. 동상 증세가 보이는 단원이 둘 있고, 큰 부상자는 아직까지 없습니다. 이동할 수 있습니다."

            show char s default def at top
            s "그럼, 헤안님은 뒤에서 기사단원들을 살피며 이동 부탁드리겠습니다."

            show char h default def at top
            h "알겠습니다."

            hide char
            "그리고 에런에게는 대충 앞장서라는 눈짓만을 줬다."

            show char s default def at top
        "상황 지휘를 하며, 안전지대로 이동할 준비를 한다.":
            s "그럼, 헤안님은 기사단 전원에게 휴식을 위해 안전지대로 이동할 예정이라고 전해주세요."
            show char s default def at top
            s "그리고 뒤에서 기사단원들을 살피며 이동 부탁드리겠습니다."

            show char h default def at top
            h "알겠습니다."

            show char s default def at top
            s "에런님은 제게 자세한 이동 경로를 설명 부탁드립니다."

            show char e default def at top
            e "네. 이쪽으로 오시면, 설명해 드리겠습니다."

            hide char
            "나와 스승님의 사이를 더는 들키지 않기 위해, 둘 모두에게 지시를 내렸다. "

            "또한 에런과의 불편함을 감수하고, 그와의 동행을 선택했다."

    "그렇게, 기사단은 시간을 지체할 틈 없이 안전 지대로 서둘러 움직였다. "
    scene bg camp night
    play Sound "sfx/hammer.mp3"
    "안전지대에 도착한 후에는 막사를 설치하기 시작했다."

    "다들 분주했고, 여기저기서 곡소리가 들렸다."

    "아직 제대로 된 전투는 시작도 안 했는데, 기후 때문인지 기사단원들의 상태가 영 좋지 못했다."

    "앞으로를 위해서라도, 이번 휴식을 통해 원상태로 돌아오길 바랄 뿐이었다."

    "그리고, 국경 근처인 만큼 타국의 경계 보초를 위해 나는 헤안과 몇 기사단원을 이끌고 정찰을 나서기로 했다."

    "눈 덮인 숲만큼 위험한 곳은 없었다."

    "눈이 바닥을 빼곡히 채우고 있어, 발밑을 확신할 수 없었기 때문이다."

    "정찰대 일행은 그 점에 유의하며, 재빠르게 복귀할 예정이었다."

    "하지만 왠지 모를 불안감이 엄습 해오기 시작했다."

    show char t default emb at top
    play music "bgm/ptsd3.mp3"
    q "살려주세요!"
    with shake

    hide char
    "큰 비명과 함께 살려달라는 외침이 들렸다."

    "순식간에 벌어진 일이었다."

    "기사단원 타나가 절벽에서 미끄러져, 돌부리를 간신히 잡고 있었다. "

    "나는 망설임 없이 타나에게 달려들었다."

    "곁에 있던 헤안도 놀라 내게 빠르게 달려들었다."

    "헤안과 힘을 합쳐 있는 힘껏 함께 그녀를 끌어올렸다."

    "덕분에 그녀는 절벽에서 올라올 수 있었다."

    "하지만···."

    "내가 떨어지는 건 전혀 예상하지 못했던 일이었다."

    "그녀를 끌어올린 반동 때문이었다."

    "물론 헤안이 나를 간신히 잡았으나, 하필이면 눈바닥이 무너져 내리는 바람에 그는 나를 놓치고 말았다. "

    show char t default emb at top
    T "세레나님!!!!"

    show char h default emb at top
    h "세레나!!!!"

    hide char
    "다들 다급하게 내게 손을 뻗었다."

    "하지만 이미 늦은 후였다."

    "그래도 이런 순간에 나를 걱정해 주는 사람들이 있어 다행이라는 생각을 했다."

    "또한 절벽에 떨어지면서, 그동안의 멍청했던 나날들이 하나둘씩 떠올랐다."

    "이럴 줄 알았으면 조금 더 막 살아볼 걸···."

    "아니다, 이제 와서 이게 무슨 의미가 있을까."

    scene black
    "나는 눈을 감았다. "

    "부디 신이 있다면, 여기서 살아남을 수 있기를 기도했다."

    play Sound "sfx/fall.mp3"
    "쿵-"

    $ persistent.ClaerChapter(max(chapter_num,persistent.ClaerChapter))
    return
