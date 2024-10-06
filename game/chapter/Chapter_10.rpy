label chapter_10:
    "제목 : 예상치 못한 사건"

    scene black
    play music "bgm/comfort7.mp3"
    "우리 기사단과 제국의 병사들은 일단 약속대로, 프라타히라와의 왕국 전쟁을 준비하는 나날을 보냈다."

    "제국 측의 사람도 합류를 한 이상, 눈속임을 부릴 수는 없었다."

    "그들의 움직임이 점점 커지고 있기도 했고."

    scene bg camp in
    s "헤안, 4부대에 장비지원이 더 필요하다고 합니다."

    "물품 관련 직책을 맡고 있는 스승님 대신, 헤안에게 장비 지원 요청을 맡겼다."

    "여전히 스승님과 단둘이 있기에는 껄끄러워서였다."

    show char h default des at top
    h "아···. 예. 금방 처리해 드리겠습니다."

    hide char
    "그의 표정이 좋지 않았다."

    s "무슨 일 있습니까?"

    show char h default des at top
    h "아닙니다."

    hide char
    "영 괜찮은 표정과 분위기가 아니었다."

    "분위기를 풀어보려, 화제를 전환시켰다."

    s "그나저나, 아까 헤안님 앞으로 급한 전보가 왔다던데."

    s "혹시 또 황실입니까?"

    "화제 전환은 실패였다."

    "오히려 내가 불이라도 지핀 것 처럼, 그의 표정이 더 어두워졌다."

    show char h default des at top
    h "황실에서 온 것은 맞습니다만···. 공작가 관련 일입니다."

    show char h default des at top
    h "그래서, 제가 잠시 자리를 비워야 할 것 같습니다. 공작가로 가서 직접 일을 해결해야 할 것 같아서요."

    show char h default des at top
    h "죄송합니다."

    s "황실 측에서 협박이라도 온 겁니까?"

    hide char
    "그는 곤란한 표정을 지었다."

    "하지만, 황실과 관련된 것이라면 그냥 지나칠 수는 없었다."

    menu .m0:
        "나는 집요하게 그를 붙잡았다."
        "황실을 들먹이며, 내용을 요구한다.":
            s "황실에서 보낸 거라면, 저도 알아야 할 것 같습니다. "
            "저희, 같은 목표를 하고 있지 않습니까."

        "솔직하게 말해달라고 요구한다.":
            $ persistant.Likeability['hean'] += 5
            s "솔직하게 말해주세요."
            "곤란한 일이라면, 도와드리겠습니다."

    "그는 한숨을 깊게 쉬고, 입을 열었다."
    show char h default des at top
    play music "bgm/ptsd3.mp3"
    h "공작가가 반역을 일으켰다는 전보였습니다."

    s "공작가라면··· 헤안님의 레이워스 가문이 맞습니까?"

    show char h default des at top
    h "네. 저희 레이워스가가 전쟁 자금을 빼돌리고, 무기를 왕국에게 유통했다고 합니다."

    show char h default des at top
    h "황실 측은 이를 반역이라 본 것 같고요."

    s "반역이라고요?"

    hide char
    "헤안의 말에 놀란 나는 그의 말을 되물었다."

    show char h default des at top
    h "네. 하지만, 말이 안 됩니다. 레이워스가가 전쟁의 중심이라니요."

    show char h default des at top
    h "뭔가, 뭔가 오해가 있는 게 분명합니다."

    hide char
    "무척이나 불안해 보였다. 평소의 헤안답지 못했다."

    "나 또한 믿을 수 없었다. 레이워스가는 중립을 잘 지켰으며, 청렴을 내세우는 가문이었기 때문이었다. "

    "게다가 가문의 일원인 헤안은 가족이 살기 좋은 국가를 만들기 위해, 그 누구보다 열심히 살아가는 사람이었다."

    "머리를 굴려봤다. 해답은 하나였다."

    s "황실의 조작."

    "생각만 한다던 게, 입 밖으로 튀어나왔다."

    show char h default emb at top
    h "네?"

    s "황실이 중립을 지키는 헤이워스가를 방해물로 여겼을 확률이 큽니다."

    s "이번 기회에, 제국에서 헤이워스가를 지울 생각일지도 모른다는 뜻입니다."

    s "왜 지금인지는 잘 모르겠지만요."

    show char h default emb at top
    h "그렇다면, 황실에 무슨 일이 일어난 걸지도 모릅니다. "

    show char h default emb at top
    h "최근 급하게 움직인다는 느낌을 받았거든요."

    show char h default emb at top
    h "이번 압박건도 그렇고요."

    hide char
    "그의 말은 설득력 있었다."

    "황실에게 의문이 생겼고, 나는 이를 해결해야 할 것만 같았다."

    s "그럼, 저도 함께 공작가로 가겠습니다."

    show char h default emb at top
    h "그게 무슨 소리십니까."

    s "황실이 보낸 훌륭한 지휘관과 기사들도 있고, 에런님도 있으시니 괜찮을 겁니다."

    s "당분간은 정비 기간이기도 하고."

    hide char
    "전투가 일어나지 않을 것을 확신했기에 가능했다."

    "이번 전투로 인해, 프라타히라 왕국은 전력을 복구하는 데에 시간이 걸릴 것이었다."

    s "이번 일, 황실과 전쟁이 엮여 있는 것을 보아하니 저도 직접 알아봐야 할 것 같습니다."

    s "전쟁을 멈출 수 있는 실마리를 잡을 수 있을지도 모릅니다."

    show char h default des at top
    h "후··· 알겠습니다. 대신, 3일. "

    show char h default def at top
    h "세레나님은 3일 이내에 기사단으로 복귀하시는 걸로 하십시오."

    show char h default def at top
    h "그 이상은 세레나님조차 황실의 반역자로 묶일 수 있습니다."

    s "알겠습니다."

    hide char
    "나와 헤안은 기사단과 에런에게 황실의 명령 수행을 위해 잠시 자리를 비운다는 말을 남겼다."

    "헤안이 황실의 전보를 받은 것을 알고 있었기에, 별 의심을 받지 않았다."

    "또한, 황실의 명령이라는 핑계로 어렵게 소수 전용 텔레포트 마도구를 빌릴 수 있었다."

    "빠르게 갔다 오기 위함이었다."

    scene bg forest day
    play music "bgm/comfort4.mp3"
    s "준비되셨습니까?"

    show char h default des at top
    h "네···."

    hide char
    "그의 표정은 여전히 좋지 않았다."

    menu .m1:
        "심지어는 손을 떨고 있었다. 그를 자세히 보지 않았다면, 모르고 넘어갈 뻔했다."
        "헤안을 응원한다.":
            "나는 떨리는 그의 손을 잡았다."
            "그는 흠칫했다."

            s "괜찮을 겁니다."

            s "여태 잘 해오셨잖아요. 이번에도 잘될 겁니다."

            s "일단 지금은 아무것도 생각하지 맙시다."

            show char h default des at top
            h "네. 감사합니다···."

            hide char
            "여전히 힘이 나보이는 것 같진 않았다."

            "그는 입을 꾹 다물고 있었다."

        "헤안을 위로한다.":
            $ persistant.Likeability['hean'] += 5
            play sound "sfx/cloth.mp3"
            "나는 그에게 다가가, 포옹을 건넸다."
            "그는 흠칫했다."

            "그렇게, 서로 아무런 말을 하지 않았다. 차츰 그의 떨림이 멈추기 시작했다."

            "그리고 그가 먼저 입을 열었다."

            show char h default des at top
            h "사실 잘 모르겠습니다···."

            show char h default des at top
            h "정말 레이워스가가 그랬다면 어떻게 해야 막막하기도 하고,"

            show char h default des at top
            h "형님의 상태 또한 걱정됩니다. "

            s "일단 지금은 아무것도 생각하지 맙시다."

            s "다가올 것이 두려워서 지금 아무것도 못 하면 안 되잖아요."

            s "가서 생각합시다. 다 괜찮을 거예요."

            s "저도 함께하잖아요."

            show char h default smi at top
            h "···감사합니다."

            hide char
            "그는 아이 같은 맑은 웃음을 보였다."

            "한결 마음이 편해진 듯 보였다."

    scene black
    play music "bgm/dis.mp3"
    "우리는 텔레포트를 타고, 레이워스 공작가에 들어갔다."
    "제대로 된 사용인 하나 보이지 않았다."

    "말 그대로 난장판이었다."

    "이미 황실 측이 한 번 들쑤시고 간 모양이었다."

    "헤안은 사색이 되어, 공작의 집무실을 향해 뛰어갔다."

    "나 또한 그를 뒤따라갔다."

    show char h default emb at top
    scene bg noble work
    h "아버지··· 이게 대체 무슨 일입니까!"

    hide char
    "레이워스가의 공작이자, 헤안의 아버지가 텅 빈 집무실에 앉아 서류를 정리하고 있었다."

    "공작은 침착해 보였지만, 그 누구보다 참담해 보였다."

    show char hf default at top
    Character('레이워스 공작') "오랜만에 보는데, 꼴이 이래서 미안하구나···."

    show char hf default at top
    Character('레이워스 공작') "너를 볼 낯이 없다."

    show char h default bad at top
    h "괜찮으니까 진실을 말해주세요, 아버지."

    show char hf default at top
    Character('레이워스 공작') "후···."

    hide char
    "공작이 한숨을 크게 내쉬고, 한참을 뜸 들이다 입을 열었다."

    show char hf default at top
    Character('레이워스 공작') "너는 자세히 몰랐겠지만, 네 형의 상태가 점점 악화되고 있었다. 언제 세상을 떠나도 이상하지 않았지."

    hide char
    "하지만 황제가 이걸 어떻게 알았는지, 네 형의 목숨을 담보로 나에게 거래를 걸었어."

    "급박했다. 네 형의 목숨이 오가는 상황에서 어쩔 수가 없었어."

    show char h default bad at top
    h "설마···. 사실입니까?"

    show char h default bad at top
    h "무기 보급을 도운 게? 전쟁 자금을 빼돌린 것도요?"

    show char hf default at top
    Character('레이워스 공작') "처음에는 그저 자국을 위한 무기 생산과 유통이었다. 여기까지는 문제가 되지 않았지."

    show char hf default at top
    Character('레이워스 공작') "아무리 황제가 미쳐있어도, 만든 무기를 적국에 팔아넘길 줄은··· 몰랐지만 말이다."

    show char h default des at top
    h "미리 막을 순 없었나요?"

    show char hf default at top
    Character('레이워스 공작') "안타깝게도 그걸 알아챈 순간은 이미 너무 늦은 후였다."

    show char hf default at top
    Character('레이워스 공작') "우리 가문이 그에 관여한 것은 확실했고, 서류로도 증거가 남겨져 있었다."

    show char hf default at top
    Character('레이워스 공작') "게다가 네 형의 목숨까지 들먹이며, 협박을 해왔지."

    show char hf default at top
    Character('레이워스 공작') "확실히, 거래 이후에 황실의 치료를 받고 나서부터는 상태가 꽤 괜찮아졌었거든."

    show char hf default at top
    Character('레이워스 공작') "황제가 이토록 비겁할 줄은 몰랐다. 이 정도는 아니었는데."

    show char h default bad at top
    h "아버지 어떻게 이럴 수가 있습니까···."

    hide char
    "헤안의 목소리는 떨리고 있었다. 울음을 애써 참고 있는 사람처럼."

    "헤안의 고개가 일어날 생각을 하지 않았다."

    show char hf default at top
    Character('레이워스 공작') "미안하다···. 변명의 여지가 없구나."

    show char hf default at top
    Character('레이워스 공작') "너를 전쟁으로 내민 것도 모자라, 가문까지 멸문으로 내밀었구나."

    show char h default def at top
    h "전쟁은 제 선택이었습니다. 그리고 아직 멸문은 아닙니다."

    show char h default def at top
    h "아버지께서는 한 가문의 대표로서, 이 가문을 살릴 생각이나 하고 계십시오."

    show char h default def at top
    h "저도 돕겠습니다."

    hide char
    "그는 무언가를 결심한 듯했다. 그러고는 고개를 번뜩 들었다."

    show char h default def at top
    h "형님은 어디 계십니까?"

    show char hf default at top
    Character('레이워스 공작') "네 형의 목숨만은 어떻게 붙여놨다."

    show char hf default at top
    Character('레이워스 공작') "하지만, 황실의 발길이 끊긴 이후로는 눈 뜰 생각을 안 해."

    hide char
    "헤안은 두 눈을 질끈 감았다."

    "말하지 않아도, 두 부자의 감정이 느껴졌다."

    s "그건 제가 어떻게든 해보겠습니다."

    "나도 모르게 나온 말이었다."

    "헤안을 돕고 싶었다. 그리고, 할 수 있을 것 같았다."

    "그 힘을 써본다면···."

    "헤안의 형을 살리는 것 정도는 가능할 것 같았다."

    show char hf default at top
    Character('레이워스 공작') "당신은 누구신지···."

    hide char
    "경황이 없어, 공작이 여태 날 보지 못한 모양이었다."

    show char h default def at top
    h "아, 이분은 황실기사단장 세레나님이십니다."

    hide char
    "헤안이 뒤늦게 나를 소개시켰다."

    show char hf default at top
    Character('레이워스 공작') "황실기사단장이라면··· 황녀 아니던가?"

    hide char
    "공작이 얼굴을 찌푸리며, 엄중한 목소리를 냈다."

    "내가 직접 나서야 할 것 같았다."

    s "걱정하지 십시오. 사생아라서, 저 또한 황실에 좋은 감정 없습니다."

    s "제가 이곳에 온 이유는, 황실이 왜 지금 공작가를 공격해야만 했는지를 알고 싶기 때문이었습니다."

    s "저는 전쟁을 멈추고, 이 제국을 갈아엎을 생각입니다."

    show char hf default at top
    Character('레이워스 공작') "황녀께서는 반역을 일으키겠다는 겁니까?"

    s "반역이 아닙니다."

    s "혁명이자, 계승이 되겠죠."

    show char hf default at top
    Character('레이워스 공작') "하···!"

    show char hf default at top
    Character('레이워스 공작') "(기가 차다는 듯한 소리를 냈다. 하지만 썩 나쁜 표정은 아니었다."

    show char hf default at top
    Character('레이워스 공작') "그게 성공한다면 좋겠군요."

    s "예. 그러니, 제게 협조해 주십시오."

    s "황제가 어째서 지금 이 때에 공작가를 공격한 것이죠?"

    show char hf default at top
    Character('레이워스 공작') "일단 중립 가문이었던 레이워스가가 거슬렸을 겁니다."

    hide char
    "여기까지는 예상했던 대로다."

    show char hf default at top
    Character('레이워스 공작') "그리고, 최근 황실에 대한 여론이 계속해서 안 좋아지고 있습니다."

    show char hf default at top
    Character('레이워스 공작') "당신을 전쟁에 내보냈는데도."

    show char hf default at top
    Character('레이워스 공작') "그래서 이 비난의 화살을 돌릴 곳이 필요했을 겁니다. 마침 레이워스가가 타깃이 된 거고요."

    show char hf default at top
    Character('레이워스 공작') "아무리 황제라도 제국민 전체의 반란은 무서웠을 테니."

    show char hf default at top
    Character('레이워스 공작') "하지만, 이상한 점이 있습니다."

    s "···!"

    show char hf default at top
    Character('레이워스 공작') "해명과 재판을 위해 황궁으로 찾아갔으나, 황제가 모습을 드러내지 않더군요."

    show char hf default at top
    Character('레이워스 공작') "과시와 권력을 그리 좋아하는 양반이 말입니다."

    show char hf default at top
    Character('레이워스 공작') "대신 황후가 저를 맞이했습니다. "

    show char hf default at top
    Character('레이워스 공작') "아마, 황제에게 무슨 일이 생긴 것 같았습니다. "

    show char hf default at top
    Character('레이워스 공작') "그 때문에 공작가를 몰아내는 것에 서두른 것이겠죠. 프라타히라 왕국 정복이 앞당겨진 것도 그렇고 말입니다."

    hide char
    "역시 황실에 파란이 일어난 게 분명했다."

    s "알겠습니다. 감사합니다, 공작."

    s "하지만 명심하십시오. 제가 혁명에 성공한다 하더라도, 어찌 되었든 전쟁에 가담한 죄는 물을 것입니다."

    "레이워스 공작가에게 실망을 하지 않은 것 아니었다."

    "다만, 지금은 순서가 있다고 생각되었다."

    show char hf default at top
    Character('레이워스 공작') "예. 명심하죠."

    scene bg noble way
    play music "bgm/hean1.mp3"
    hide char
    "공작의 말을 끝으로, 헤안과 나는 집무실을 벗어났다."

    "헤안은 또다시 고개를 떨구었다."

    show char h default def at top
    h "세레나님은 이만 복귀하셔도 될 것 같습니다."

    show char h default def at top
    h "저는 상황 정리와 죄의 감형을 입증할 만한 것을 찾아본 후 복귀하겠습니다."

    s "아니요. 아직 할 게 남았습니다. 아까 말했잖아요."

    s "헤안님의 형님분을 치료해 보겠다고요."

    show char h default bad at top
    h "네? 그게 쉬운 일이신 줄 아십니까?"

    show char h default bad at top
    h "게다가 그 마법사가 힘을 쓰지 말라고 했다고 하지 않았습니까?"

    hide char
    "그는 내게 화를 냈다."

    s "괜찮습니다. 가능합니다."

    s "그때 보셨잖습니까. 없던 신체도 되돌리는 힘을요."

    show char h default bad at top
    h "대체 무엇을 믿고, 그리 나섭니까!"
    with shake

    hide char
    "결국, 그가 큰 소리를 내었다."

    s "제 자신을 믿습니다."

    s "저는 여태, 저에게 확신 하나 없던 사람입니다."

    s "사생아로 태어나, 정체성 확립도 못 한 채로 살아왔으니까요."

    s "전쟁에도 떠밀려 나오고."

    s "근데, 최근 들어 이런 생각이 들었습니다."

    s "내가 나를 믿지 않으면, 내가 직접 행동하지 않으면, 아무것도 해결되는 게 없다는 걸요."

    s "제가 형님분을 살릴 수 있다는 건, 제 자신감이자 확신입니다."

    s "가능합니다. 그래야만 하니까요."

    "전쟁에 떠밀려 나와서 겪은 일들, 타나의 죽음, 새로운 힘의 발견. "

    "무력감을 느꼈던 일들뿐이었지만, 결국 모든 것은 나로 인해 벌어진 일들이었다."

    "내가 해야만 한다. 그래야 바꿀 수 있다."

    "그랬기에, 제국을 엎겠다는 목표도 세운 것 아니었던가."

    "여기서 사람 하나 살리지 못한다면, 내게는 그럴 자격 따위는 없다."

    "헤안은 나를 한참 쳐다봤다."

    show char h default des at top
    h "형님의 방으로 안내해 드리겠습니다."

    hide char
    "조용히 그를 따라갔다."

    show char h default def at top
    scene bg noble bed blue day
    play music "bgm/sad4.mp3"
    h "여기입니다."

    hide char
    "모든 게 엉망이던 공작가에서 유일하게 깔끔한 방이었다."

    "헤안과 닮은 남자가 창백한 얼굴로 누워있었다."

    "나는 곧바로 그를 치료하기 위해, 심장에 집중했다."

    "빛 무리가 또다시 내 주변을 떠다니기 시작했다."
    show white at fadeInOut
    "이번에는 터트리듯이 아닌, 실을 뽑아내듯이 미세하게 힘을 어루만졌다."

    play sound "sfx/heart.mp3"
    "불안정했다. 심장이 또다시 아파왔다."
    show red at fadeInOut
    s "윽···."

    "그러나 누군가 속삭이는듯한 소리도 들리는 것 같았다."

    "그럼에도 꾹 참고, 그 힘을 헤안의 형 쪽으로 옮긴다고 생각했다."

    play sound "sfx/magic.mp3"
    "파앗―"
    show white at fadeInOut
    show char h default emb at top
    h "···!"

    s "허억···."

    hide char
    "성공인가···?"

    "창백했던 얼굴에 핏기가 돌아오기 시작했다."

    "그리고, 그가 눈을 살며시 떴다."

    show char h default emb at top
    h "형님···!"

    hide char
    "헤안이 아이처럼 그에게 달려들었다."

    scene bg noble way
    play music "bgm/peace.mp3"
    "나는 형제의 시간을 방해하지 않도록, 조용히 방을 나왔다."

    "다행히, 힘을 사용할 수 있었다. 아직 많이 불안정해서, 다음에도 쓸 수 있을지는 모르겠지만 말이다."

    "그래도 나만의 무기가 생겼다는 건 좋은 일이었다."

    "그렇게 오랜 시간 동안 공작가를 돌아다녔다."

    show char h default smi at top
    h "세레나님···!"

    hide char
    "헤안이 재회를 마친 듯, 내게 달려왔다."

    show char h default smi at top
    h "아까는 죄송했습니다. 감사하다는 인사도 제대로 못 드리고."

    s "괜찮습니다. 보기 좋았는데요, 뭐."

    hide char
    "그의 귀가 빨개졌다."

    show char h default smir at top
    h "시간이 늦었으니, 오늘 복귀는 힘드실 것 같습니다."

    show char h default smir at top
    h "묵으실 방을 안내해 드리겠습니다."

    s "되게 집사 같네요."

    hide char
    "나는 분위기를 풀기 위해 시덥잖은 이야기들을 꺼냈다."

    "그렇게 방에 도착했을 때,"

    show char h default desr at top
    h "저···세레나님."

    show char h default desr at top
    h "오늘은 정말 감사했습니다. 그리고 죄송합니다."

    show char h default desr at top
    h "복잡한 일에 휘말리게 한 것 같고, 세레나님을 믿지 못한 것 같아서요."

    show char h default desr at top
    h "소리를 크게 지른 것도요."

    show char h default desr at top
    h "앞으로는 이런 일 없도록 하겠습니다."

    show char h default desr at top
    h "그러니, 제가 세레나님의 목표까지 함께 할 수 있도록 허락해 주십시오."

    hide char
    "그는 고개를 숙였다."

    "오늘따라 그의 고개는 영 힘을 못 추리는 것 같았다."

    s "고개 숙이는 건 오늘 그만합시다."

    "그가 곧바로 고개를 들었다. "

    "조금 웃겼다. 말을 곧이 곧대로 다 듣는게 꼭 개같아서."

    s "우리 사이에 허락이고 할 게 뭐 있어요. 다 괜찮습니다."

    s "전 헤안님이랑 함께 하고 싶었습니다."

    s "우리는 앞으로 황실의 낯을 모두에게 밝히고 전쟁을 멈추는 것에 집중합시다."

    s "아, 헤안님은 일단 공작가부터 어떻게 해보시고."

    "그의 어깨가 너무 무거워 보여서, 일부러 가벼운 말투를 내뱉었다."

    "이렇게라도 해야, 그가 짐을 덜 수 있을 것 같았다."

    "그리고, 왠지 모르겠지만 그가 편해졌다."

    "그가 한참이나 말을 잇지 않았다."

    "내가 너무 무례하게 굴었나 싶어, 그의 얼굴을 쳐다봤다."

    s "응?"

    "그는 알 수 없는 표정을 하고서는, 조용히 눈물을 흘리고 있었다."

    "사람이 소리 없이도 우는구나 싶기도 하면서, 놀랐다."

    "처음에 봤을 때는 그만큼 딱딱한 사람이 없었는데, 지금은 이렇게나 물렁해졌다니."

    menu .m2:
        "그가 애처로워 보였다."
        "울지 말라며, 그를 달랜다.":
            $ persistant.Likeability['hean'] += 2
            play music "bgm/hean2.mp3"
            "힘들었어요?"
            "나는 나긋이 그에게 물었다."

            "그가 천천히 눈을 감고, 고개를 끄덕였다. 그의 눈물은 멈추지 않았다."

            s "괜찮아요. 다 괜찮아질 거예요."

            s "내가 그렇게 만들어볼게. 됐죠?"

            s "이제 울지 맙시다. 뚝!"

            s "명색의 공작가 자제가 이래서 되나."

            "나는 그의 울음을 멈추기 위해서 열심히 달랬다."

            "마치 애를 다루듯 말이다."

            show char h default smir at top
            h "푸핫···!"

            hide char
            "다행히, 성공했는지 그는 웃음을 보였다."

            "여전히 물기 있는 얼굴에, 눈가가 붉었지만, 기운을 조금 차린 것 같았다."

            show char h default smir at top
            h "이제 저를 완전히 애로 보시는 군요."

            s "애처럼 우시던데요. 뭘."

            hide char
            "그의 얼굴 전체가 붉어졌다."

            show char h default smir at top
            h "세레나님을 볼 낯이 없네요."

            s "괜찮아요. 못 볼 꼴 다 본 사이만큼 좋은 거 없을 겁니다."

            show char h default smir at top
            h "그런가요."

            s "ㄴ···."

            hide char
            "네라고 대답하려던 찰나,"

            "그가 볼에 입맞춤을 했다."

            s "···!"

            show char h default smir at top
            h "이것도 못 볼 꼴에 해당될까요?"

            s "···아닐걸요?"

            hide char
            "그답지 않은 행동에 어안이 벙벙했다."

            show char h default smir at top
            h "아쉽네요."

            hide char
            "덤덤해 보이는 말과는 다르게, 그의 얼굴은 금방이라도 터질 것 같았다."

            show char h default smir at top
            h "그럼, 내일 뵙겠습니다. 안녕히 주무십시오."

            s "ㄴ,네."

            scene black
            hide char
            "그는 재빠르게 자리를 떠났다. 마치 저번에도 이런 비슷한 일이 있었던 것 같았다."

            "나는 거의 뜬눈으로 밤을 지새웠다."

            "황실에 대한 걱정 때문인지, 아니면 다른 무엇 때문인지는 알 수 없었다."

        "조용히, 그의 눈물을 닦아준다.":
            $ persistant.Likeability['hean'] += 5
            scene bg noble work
            play music "bgm/hean2.mp3"
            "나는 그에게 손을 뻗어, 눈물을 닦아주었다."
            "그는 눈물을 닦아주던 내 손에 제 얼굴에 기댔다."

            s "참지말고 울어도 됩니다."

            s "그만큼 힘드셨잖아요."

            "내 말을 들은 그는, 내게 천천히 다가왔다."

            "그러고는 내 품에 안겨, 숨죽여 울기 시작했다."

            "나는 그를 다독였다."

            s "괜찮아요. 다 잘 될거니까요."

            s "저 믿죠?"

            "내 어깨에 고개를 묻었던 그가, 작게 끄덕였다."

            "오늘따라 그가 굉장히 작아보였다."

            "나는 내게서 헤안을 일으켜 세웠다."

            "그는 순순히 밀려났다."

            "붉은 눈가, 물기 있는 얼굴. 그 누구보다 순해 보였다."

            show char h default embr at top
            h "···!"

            hide char
            "그의 동공이 확장되었다."

            "내가 했지만, 나도 알 수 없는 행동이었다."

            "그에게 입맞춤을 한 건 말이다."

            show char h default embr at top
            h "저를 좋아하십니까?"

            s "아, 아니 그건 모르겠는데···."

            s "그냥 나도 모르···"

            hide char
            "내 말은 끝내 다 이어지지 못했다."

            "그가 곧바로 내게 다시 입을 맞춰왔기 때문이었다."

            "순하다고 했던 건 취소다."

            scene black
            "그렇게 우리는 한참을 문 앞에서 입을 맞췄다."

            "조용하고 서늘한 복도에는"

            "오로지 둘 뿐이었다."

            scene bg noble way
            s "그··· 그만···."

            show char h default desr at top
            h "아···."

            show char h default desr at top
            h "죄송합니다."

            hide char
            "그는 아쉽다는 듯 내게서 떨어졌다."

            s "죄송할 필요는 없고···."

            "침묵이 계속되어, 내가 먼저 운을 띄웠다."

            s "이만 그···자러 갈까요? 시간도 늦었고···."

            show char h default embr at top
            h "네?"

            hide char
            "그는 갑자기 당황한 눈치였다. 얼굴까지 붉히면서."

            "그가 정신이 없어, 무언가 오해한 것 같다고 생각했다."

            s "그니까, 각자!"

            show char h default embr at top
            h "아, 아!"

            show char h default embr at top
            h "네. 그래야죠···."

            hide char
            "그의 얼굴이 금방이라도 터질 것 같았다."

            "그는 헛기침을 몇 번 하고서는, 저녁 인사를 건넸다."

            show char h default defr at top
            h "안녕히 주무십시오."

            s "헤안님도요."

            hide char
            "그는 내 말을 들을 새도 없이, 자리를 떠났다."

            "그렇게 빠른 걸음은 세상에서 처음 봤다."

            scene bg noble bed yellow night
            "나 또한 방에 재빠르게 들어가, 잠을 청했지만 한참을 뒤척였다."

            s "미쳤나봐···."

            scene black
            "마음이 뒤숭숭했다."

    play music "bgm/ptsd2.mp3"
    "그렇게, 공작가에 아침이 찾아왔다."
    scene bg noble way
    "준비를 빠르게 마치고, 방을 나섰다."

    "헤안이 급하게 내 쪽으로 달려오고 있었다."

    "레이워스 공작가 앞으로 급한 전보가 날라왔다고 한다."

    scene black
    "황제가 서거하였다는."

    "이거였다. 황실이 최근 급하게 군 이유가."

    "나는 황제의 죽음 뒤에 많은 일이 오가고 있다는 것을 직감적으로 느낄 수 있었다."

    $ persistent.ClaerChapter = max(11,persistent.ClaerChapter)
    return
