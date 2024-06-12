#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 라이브러리
import pandas as pd
import plotly.express as px
import streamlit as st


# In[4]:


# 꽉 찬 화면 
st.set_page_config(layout="wide")


# In[5]:


# 논어 전문 불러오기
with open ('lunyu.txt', 'r', encoding = 'utf-8') as file: 
    lunyu_txt = file.read()


# In[6]:


# 이미지 파일
kongzi = 'https://jmagazine.joins.com/_data/photo/2017/01/2949993309_Hu1tv2Y3_01.jpg'
lunyu = 'https://lh5.googleusercontent.com/proxy/fWx6IWh2tjdNWCAOyDrG-hvrBVM11O7KTbS9NkM7CZEB64p7L7YeCiRQBm0Ham8be9B_kcEBVNj_tiZvfbAmnC_yWqbv4l1XCZH2s88giGYYlplkdvS-cLS2o8HHuQ'


# In[9]:


# 사이드바에 탭 생성
sidebar = st.sidebar.radio("LIST", ['main', '공자', '행복관', '樂', '說', '논어전문'])

# 탭에 따라 다른 내용 표시
if sidebar == 'main':
    st.title('『논어』로 보는 공자의 행복관')
    
    st.subheader('데이터 기획 배경')
    st.markdown('''
    다양한 문화권에서 좋은 삶은 보통 행복과 연관되고는 한다. <br>
    도덕적으로 완성된 군자를 교육한다는 측면에서, 좋은 삶을 제시하고자 했던 공자도 마찬가지로 행복과 관련한 언급을 했다. <br>
    이 언급을 정리함으로써 공자의 행복관을 알아보고 이를 오늘날에도 활용할 방법을 모색하고자 데이터를 기획했다.
    ''', unsafe_allow_html=True)
    
    st.subheader('데이터 수집 대상')
    st.markdown('''
    <p>공자의 행복관은 『논어』에서 어떻게 드러날까? </p>
    <p>‘행복이란 무엇인가?’라는 질문은 사람이 살아감에 있어서 한번 쯤 생각하기 마련인 보편적인 질문이다. <br>
    그러나 이 질문에 대한 답을 명확히 단정 짓기는 힘들다. <br>
    우리는 행복을 너무 경험적인 것으로 해석하는 경향이 있다. <br>
    즉, 행복을 주관적이고 개별화된 것으로 여기며, 경험적 쾌락으로 제한한다. <br>
    쾌락은 행복과 엄연히 다른 것이다. 쾌락 이외의 다른 가치로도 행복을 논할 수 있으며 순간의 쾌락을 넘어서, 인생의 의미에서 행복을 찾을 수 있다. <br>
    행복의 의미가 확장된다면, 그것은 더 이상 단순한 행복이 아니라, 삶의 의미를 추구하는 목적이 될 수 있다. </p>
    
    <p>幸이란 요행(徼幸)으로 뜻하지 않은 좋은 운(運)이며, 福이라는 개념 역시 하늘에서 내려진 축복이라고 할수 있다. <br>
    행복이란 나의 의지보다는 외부에서 주어진 행운과 축복이라는 것이 일차적인 정의이다.<br>
    행복이란 행운을 뜻하는 행과 축복을 뜻하는 복의 합성어이다. <br>
    『논어』에는 福이라는 말이 한 번도 등장하지 않고 있다. <br>
    이에 간접적인 방식으로 행복을 유추해야 한다. <br>
    즐거움과 같은 것이 그 답이 될 수 있다. <br>
    행복은 즐거움, 좋은 감정 내지 상태와 연관되기 때문이다. <br>
    이와 관련한 한자어를 추적하여 정리하면 행복과 관련된 개념을 구체화할 수 있을 것이다. <br>
    따라서 기쁨, 즐거움을 가진 한자어를 데이터 수집 대상으로 정의한다. <br>
    각 한자어에 따른 문장을 수집한 후, 맥락을 고려해 한 글자씩 뜯어보며, 공자는 어떤 가치에 대해서 즐거움을 부여했는 지 알아본다. </p>
    ''', unsafe_allow_html=True)
    
    st.subheader('데이터 수집 방법')
    st.markdown('''
    인터넷 검색을 통해 『논어』 전문에 대한 텍스트 파일을 다운받고, 원하는 양식에 맞게 수정한다. <br>
    원하는 한자를 입력하면, 해당 글자가 등장하는 문장을 추출하는 코드를 작성한다. <br>
    즐거움과 관련된 한자 樂(즐거울 락), 說(기쁠 열)이 등장하는 문장을 추출한다. 
    ''', unsafe_allow_html=True)
    
    st.subheader('데이터 편찬 방법')
    st.markdown('''
    즐거움과 관련된 한자 樂(즐거울 락), 說(기쁠 열)이 등장하는 문장을 추출한다. <br>
    해당 단어들이 지목하는 대상을 찾아 긍정과 부정을 표기한다. <br>
    예를 들어 '밥을 먹어서 기쁘다'라는 문장에 대해, 즐겁다의 대상이 밥이기 때문에, 밥은 긍정적인 가치를 지닌다고 해석한다. <br>
    그렇게 모아진 해석 데이터를 통해 공자가 생각하는 긍정/부정의 대상을 리스트화 한다. 
    ''', unsafe_allow_html=True)

elif sidebar == "공자":
    st.title('『논어』와 공자')
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.header('공자(孔子)')
        st.image(kongzi)
        st.markdown('''
        <p>공자가 살던 노나라는 주 천자의 통치를 받는 제후국이었다. <br>
        * 주나라 무왕이 동생 주공단에게 봉해준 봉국 <br>
        주나라는 봉건제였으며, 봉건제란 천자가 제후를 임명하고 토지를 하사하는 제도이다. </p>

        <p>하지만 혈연으로 유지되던 봉건제가 시간이 흐를수록 유대감이 희석되었다. <br>
        각 제후국들은 성장해 독립적인 힘을 지니게 되었고, 주나라의 제도와 문화의 붕괴로 인해 <span style="color:red">새 시대에 맞는 제도와 규범, 기준의 필요성이 대두되었다<span style="color:red">. </p>

        <p> 공자가 인의예지신이라는 가치를 가르친 이유: <br>
        혼란스러운 전국시대에서 주 왕실의 규범과 가치, 윤리와 제도로 돌아가 혼란스러운 현실을 구제하자!</p>
        ''', unsafe_allow_html=True)

    with col2:
        st.header('『논어』')
        st.image(lunyu)
        st.markdown('''
        <p>논어는 공자와 그 제자들의 언행을 기록한 유교경전이다. </p>
       
        <p>내용 구성:<br>
        각 편의 머리 두 글자를 따서 편명으로 삼고 있다. <br>
        공자 사후 스승과 제자 사이에 오갔던 문답을 중심으로 20편으로 구성되어 있다. </p>
       
        <p>논어의 종류: <br>
        『제논어』 : 제(齊)나라 사람들이 전해온 논어<br>
        『노논어』 : 노(魯)나라에서 전해 온 논어
        『고문논어』 : 공자의 옛집 벽 속에서 나온 논어<br>
        -> 현재 전해지는 것은 전한 말 장우(張禹)가 편집한 것 = 노논어 중심</p>
        
        ''', unsafe_allow_html=True)
        

elif sidebar == "행복관":
    st.title("행복과 즐거움에 관하여")
    st.markdown('''
    幸이란 요행(徼幸)으로 뜻하지 않은 좋은 운(運)이며, 福이라는 개념 역시 하늘에서 내려진 축복이라고 할수 있다. <br>
    행복이란 나의 의지보다는 외부에서 주어진 행운과 축복이라는 것이 일차적인 정의이다.<br>
    행복이라는 행운을 뜻하는 행과 축복을 뜻하는 복의 합성어이다. <br>
    <span style="color:red">『논어』에는 福이라는 말이 한 번도 등장하지 않고 있다.</span>
    ''', unsafe_allow_html=True)
    st.divider()
    st.subheader("'幸'이 등장하는 문장")
    st.markdown('''
    <雍也第六>02 <br>
    哀公問, “弟子孰爲好學?” 孔子對曰, “有顔回者好學, 不遷怒, 不貳過. <span style="color:red">不幸短命死矣</span>, 今也則亡, 未聞好學者也.” <br>
    애공이 물었다. “제자 중에 누가 배우기를 좋아합니까?” 공자께서 대답하셨다. “안회라는 사람이 배우기를 좋아해서, 노여움을 남에게 옮기지 않고, 같은 잘못을 두 번 저지르지 않았는데, 불행히도 단명하여 죽었습니다. 이제는 그런 사람이 엇으니, 그 후로는 아직 배우기를 좋아한다는 사람을 들어 보지 못했습니다.”
    ''', unsafe_allow_html=True)
    st.text('''
    단명해서 죽은 것에 대해서 안타까워하는 함
    단명 = 장수하지 못함 = 불행 = 부정적
    수명의 길고 짧음에 대해서 하늘의 명(어찌할 수 없는 것)이라고 여김
    ''')
    st.divider()
    st.markdown('''
    <雍也第六>17 <br>
    子曰, “人之生也直, 罔之生也<span style="color:red">幸</span>而免.” <br>
    공자께서 말씀하셨다. “사람의 삶은 정직해야 한다. 정직하지 않은 삶은 <span style="color:red">요행히 화나 면하는 것</span>이다.”
    ''', unsafe_allow_html=True)
    st.text('''
    정직하지 않은 삶 = 부정적
    정직하지 않은 삶을 산다면 언젠가는 화를 당할 것. 
    여태까지 화를 당하지 않은 것은 그저 '요행'일 뿐.
    ''')
    st.divider()
    st.markdown('''
    <述而第七>30 <br>
    陳司敗問昭公知禮乎, 孔子曰, “知禮.” 孔子退, 揖巫馬期而進之, 曰, “吾聞君子不黨, 君子亦黨乎? 君取於吳爲同姓, 謂之吳孟子. 君而知禮, 孰不知禮?” 巫馬期以告. 子曰, “丘也<span style="color:blue">幸</span>, 苟有過, 人必知之.” <br>
    진(陳)나라의 사패가 “소공은 예(禮)를 아는 사람입니까?”라고 여쭙자, 공자께서는 “예를 아는 사람입니다”라고 말씀하셨다. 공자께서 물러가시자, 인사하며 무마기를 맞아들이면서 말하였다. “나는 군자는 편당을 짓지 않는다고 들었는데, 군자도 편당을 짓습니까? 임금(소공)은 오나라에서 부인을 취하였는데, 성이 같기 때문에 부인을 오맹자라고 불렀습니다. 이런 임금이 예를 안다면 누가 예를 알지 못하겠습니까?” 무마기가 이를 알려 드리자, 공자께서 말씀하셨다. “나는 행복하구나! 진실로 허물이 있으면 사람들이 반드시 알려준다.”
    ''', unsafe_allow_html=True)
    st.text('''
    행복하다 = 기쁘다, 즐겁다
    ''')
    st.divider()
    st.markdown('''
    <先進第十一>06 <br>
    季康子問, “弟子孰爲好學?” 孔子對曰, “有顔回者好學, <span style="color:red">不幸短命死矣</span>, 今也則亡.” <br>
    계강자가 물었다.“제자 중에 누가 학문을 좋아합니까?” 공자께서 대답하셨다. “안회라는 사람이 학문을 좋아하였는데 불행히도 젋은 나이에 죽었습니다. 이제는 그런 사람이 없습니다.”
    ''', unsafe_allow_html=True)
    st.text('''
    ''')
    st.divider()

    st.subheader('동양의 행복관 - 오복(五福)')
    st.markdown('''
    <p>1. 수(壽) : 오래 사는것. 이것은 세계 모든 사람의 공통된 염원이다. <br>
    장수(長壽)에 대한 공자의 입장은 어진 사람은 장수한다고 말한 것으로 보아 긍정적이다. <br>
    물론 삶의 양보다는 질을 중시했다고 할 수 있지만, 短命을 불행하게 생각했다. <br>
    애제자 안연의 죽음에 통곡을 하였던 공자의 입장이야말로 짧은 생애로 마감한 제자의 불행을 잘 나타내고 있다. <br>
    이것은 공자도 역시 장수를 복이 있는 삶이라고 생각한다는 것임을 알 수 있다. <br>
    그의 제자 염유가 병에 걸려 신음할 때 매우 깊은 한탄을 한다는 점에서도 건강이 복임을 말한다.</p>

    <p>2. 부(富) : 富者(부자)가 되는것. 살아가는데 불편하지 않을 만큼의 재산은 꼭 필요하다.<br>
    ​부귀라는 것은 누구나 바라는 바이지만 정도(正道)로써 얻은 것이 아니면 누리지 말아야하고,
    빈천은 누구나 싫어하는 바이지만 도로써 얻은 것이 아니라도 빈천을 벗어나려 하지 말라. <br>
    공자는 장수와 건강 그리고 부귀는 누구나 다 원하는 것이라고 보고 있다. <br>
    빈천은 또한 누구나 싫어하는 것이라고 규정한다. <br>
    이것이 인간의 바람이자 인간이 누릴 수 있는 오복 가운데 하나라는 것을 인정하고 있다. <br>
    다만 논어에서 등장하는 부의 개념은 비교적 부정적인 것으로 여겨지고 있다. </p>

    <p>3. 강녕(康寧) : 健康(건강)한것. 건강하게 사는 것도 중요하다. <br>
    그러나 논어에서 직접적으로 건강과 관련한 언급은 등장하지 않는다. 
    '健', '康', '寧'에 대한 텍스트 검색 결과, 유의미한 결과 없음.
    '康'의 검색 결과는 '계강자'라는 공자의 제자 이름만 등장한다. 
    '寧'은 '차라리'라는 뜻으로 사용됨. <p>
    
    4. 유호덕(攸好德) : 남에게 선행을 베풀어 덕을 쌓는것.
    5. 고종명(考終命) : 天壽(천수)를 다하는것. 죽음복을 잘 타고 나야 합니다. 질병없이 살다가 고통없이 편안하게 일생을 마치는 것도 큰 복입니다.

    ''', unsafe_allow_html=True)
    st.text('''
   
    ''')
    st.divider()

elif sidebar == "樂":
    st.title("樂이 등장하는 문장")
    st.markdown('''
    <學而第一>01 <br>
    子曰, “學而時習之, 不亦說乎? 有<span style="color:blue">朋自遠方來</span>, 不亦<span style="color:blue">樂</span>乎? 人不知而不慍, 不亦君子乎?” <br>
    공자께서 말씀하셨다. “배우고 때때로 그것을 익히면 또한 기쁘지 않은가? 벗이 먼 곳에서 찾아오면 또한 즐겁지 않은가? 남이 알아주지 않아도 성내지 않는다면 또한 군자답지 않은가?”
    ''', unsafe_allow_html=True)
    st.text('''
    說 = 기쁘다
    樂 = 즐겁다
    學, 習, 朋自遠方來, 君子 = 긍정적
    慍 = 성내다, 부정적
    ''')
    st.divider()
    st.markdown('''
    <學而第一>15 <br>
    子貢曰, “貧而無諂, 富而無驕, 何如?” 子曰, “可也, 未若<span style="color:green">貧</span>而<span style="color:blue">樂</span>, <span style="color:blue">富</span>而<span style="color:blue">好禮</span>者也.” 子貢曰, “詩云, ‘如切如磋, 如琢如磨’, 其斯之謂與?” 子曰, “賜也, 始可與言詩已矣, 告諸往而知來者.” <br>
    자공이 말하였다. “가난하면서도 남에게 아첨하지 않고 부유하면서도 다른 사람에게 교만하지 않는다면 어떻습니까?” 공자께서 말씀하셨다. “<span style="color:blue">그 정도면 괜찮은 사람이지</span>. 그러나 가난하면서도 즐겁게 살고 부유하면서도 예의를 좋아하는 것만은 못하다.” 자공이 말하였다. “『시경』에서 말하기를 ‘칼로 자르는 듯, 줄로 가는 듯, 정으로 쪼는 듯, 숫돌로 광을 내는 듯 하도다’라고 하였는데 이를 말씀하시는 것입니까?” 공자께서 말씀하셨다. “ “賜(사, 자공의 이름)야, 이제 함께 시를 논할 수 있겠구나. 지나간 이야기를 일러주니 다가올 이야기까지 아는구나.”
    ''', unsafe_allow_html=True)
    st.text('''
    빈부에 대해서는 긍부정을 나타내지 않음
    가난하면서도 즐거운 것 = 긍정
    부유하면서도 예를 좋아함 = 긍정
    아첨, 교만 = 부정
    부유하다고 해서 무조건 긍정 X
    가난하다고 해서 무조건 부정 X
    가난하지만 그것에서 벗어나려 애쓰지 않고(아첨하지 않고) 그 상황을 즐기는 것에 대해 긍정적으로 바라봄
    ''')
    st.divider()
    st.markdown('''
    <八佾第三>03 <br>
    子曰, “人而不仁, 如禮何? 人而不仁, 如<span style="color:green">樂</span>何?” <br>
    공자께서 말씀하셨다. “사람이 되어서 인하지 못하다면 예의를 지킨들 무엇하겟는가? 사람이 되어서 인하지 못하다면 음악을 한들 무엇하겠는가?”
    ''', unsafe_allow_html=True)
    st.text('''
    인하지 않으면, 예가 쓸모없다. 
    인하지 않으면, 음악이 쓸모없다. 
    인 = 모든 것의 기반
    인 >>> 예, 음악
    음악은 인이 실천된 후에야 쓸모 있는 것
    ''')
    st.divider()
    st.markdown('''
    <八佾第三>20 <br>
    子曰, “關雎, <span style="color:blue">樂</span>而<span style="color:red">不淫</span>, 哀而不傷.” <br>
    공자께서 말씀하셨다. “『시경』의 「관저」는 즐거우면서도 지나치지 않고 슬프면서도 마음을 상하게 하지는 않는다.”
    ''', unsafe_allow_html=True)
    st.text('''
    淫(음란하다) = 어떤 흐름을 좇아 묻히거나 흘러가며 이어지는 상태나 행위, 제 마음을 주체하지 못해 마구잡이로 벌이는 행동인 방종(放縱), 탐욕과 탐심, 다시 그런 욕망에 빠져 헤어나오지 못하는 미혹(迷惑)의 새김
    즐거우면서도 지나치지 않다 = 즐거움을 추구하되, 쾌락에 매몰되지 않다.
    육체적 쾌락 뿐만 아니라 지나치게 쾌락만을 추구하는 행위에 대해서 부정적으로 인식
    ''')
    st.divider()
    st.markdown('''
    <八佾第三>23 <br>
    子語魯大師<span style="color:green">樂</span>, 曰, “<span style="color:green">樂</span>其可知也, 始作, 翕如也, 從之, 純如也, 皦如也, 繹如也, 以成.” <br>
    공자께서 노(魯)나라 태사(大師)에게 음악에 대하여 말씀하셨다. “음악은 알 수 있으니, 처음 시작할 때에는 오음(五音)을 합하며 풀어놓을 때에는 조화를 이루고 분명하며, 연속되어서 한 악장을 끝마쳐야 한다.”
    ''', unsafe_allow_html=True)
    st.text('''
    음악의 조화를 중요하게 여김
    ''')
    st.divider()
    st.markdown('''
    <里仁第四>02 <br>
    子曰, “不仁者不可以久處<span style="color:blue">約</span>, 不可以長處<span style="color:blue">樂</span>. 仁者安仁, 知者利仁.” <br>
    공자께서 말씀하셨다. “인하지 못한 사람은 오랜 동안 곤궁하게 지내지도 못하고, 오래도록 안락하게 지내지도 못한다. 인한 사람은 인을 편하게 여기고, 지혜로운 사람은 인을 이롭게 여긴다.”
    ''', unsafe_allow_html=True)
    st.text('''
    樂 = 안락하다, 긍정적
    인하지 않으면 안락할 수 없음 
    -> 이 역시 인이 먼저 선행되어야 함을 의미, 즉 즐거움(안람함)을 얻기 위해서는 인이라는 덕목을 쌓아야 함.
    ** 인하지 못한 사람은 곤궁하게 지내지 못함(?) 
    곤궁約 = 절약하다, 긍정적
    ''')
    st.divider()
    st.markdown('''
    <雍也第六>09 <br>
    子曰, “<span style="color:blue">賢</span>哉, 回也! 一簞食, 一瓢飮, 在陋巷, 人不堪其憂, 回也不改其<span style="color:blue">樂</span>. 賢哉, 回也!” <br>
    공자께서 말씀하셨다. “어질도다, 회여! <span style="color:red">한 그릇의 밥과 한 표주박의 물</span>을 가지고 <span style="color:red">누추한 거리</span>에 살고 있으니, <span style="color:red">보통 사람</span>이라면 그런 근심을 견뎌내지 못하겠지만, 회는 그 즐거움이 변치 않는구나. 어질도다, 회여!”
    ''', unsafe_allow_html=True)
    st.text('''
    곤궁하고 누추함 = 부정적 (보통 사람들이 견디기 힘든 것이라는 것을 인정)
    그 속에서도 樂즐거워 함 = 어질다, 현명하다
    자신이 처한 상황을 즐기는 자를 진정 어질다고 봄
    ''')
    st.divider()
    st.markdown('''
    <雍也第六>18 <br>
    子曰, “<span style="color:blue">知</span>之者不如好之者, <span style="color:blue">好</span>之者不如<span style="color:blue">樂</span>之者.” <br>
    공자께서 말씀하셨다. “무언가를 안다는 것은 그것을 좋아하는 것만 못하고, 좋아하는 것은 즐기는 것만 못하다.”
    ''', unsafe_allow_html=True)
    st.text('''
    무언가를 알다 <<< 좋아하다 <<< 즐기다
    ''')
    st.divider()
    st.markdown('''
    <雍也第六>21 <br>
    子曰, “知者<span style="color:green">樂</span>水, 仁者<span style="color:green">樂</span>山. 知者動, 仁者靜. 知者<span style="color:blue">樂</span>, 仁者壽.” <br>
    공자께서 말씀하셨다. “지혜로운 사람은 물을 좋아하고 인(仁)한 사람은 산을 좋아하며, 지혜로운 사람은 동적이고 인한 사람은 정적이며, 지혜로운 사람은 즐겁게 살고 인한 사람은 장수한다.”
    ''', unsafe_allow_html=True)
    st.text('''
    좋아하다는 단지 동사로 사용
    지혜로운 사람은 즐길 줄 안다 
    즉, 지혜로워야만 제대로 즐길 수 있다. 
    정신적 즐거움에 대해 언급
    ''')
    st.divider()
    st.markdown('''
    <述而第七>13 <br>
    子在齊聞韶, 三月不知<span style="color:blue">肉</span>味, 曰, “不圖爲<span style="color:green">樂</span>之至於斯也.” <br>
    공자께서 제나라에서 순임금의 음악인 소를 들으신 후, 석달 동안 고기 맛을 잊으시고는 다음과 같이 말씀하셨다. “음악을 하는 것이 <span style="color:blue">이런 경지에 이를 줄</span>은 생각하지 못했다.”
    ''', unsafe_allow_html=True)
    st.text('''
    고기 = 긍정적
    음악을 듣고 고기 맛을 석달 동안 잊다? 
    그런 경지에 이르다는 것은 음악을 들은 것이 석달동안 고기를 먹는 행위와 동일하다는 것. 
    순임금은 태평성대를 이끈 인물, 공자의 우상
    ''')
    st.divider()
    st.markdown('''
    <述而第七>15 <br>
    子曰, “飯疏食飮水, 曲肱而枕之, <span style="color:blue">樂</span>亦在其中矣. <span style="color:red">不義</span>而<span style="color:green">富且貴</span>, 於我如浮雲.” <br>
    공자께서 말씀하셨다. “거친 밥을 먹고 물을 마시며 팔을 굽혀 베개 삼고 누워도 즐거움은 또한 그 가운데 있다. 외롭지 않으면서 부귀를 누리는 것은 나에게는 뜬구름과 같은 것이다.”
    ''', unsafe_allow_html=True)
    st.text('''
    검소한 생활 = 긍정적
    왜냐하면 즐거움이 있기 때문
    부귀한 것 = 중립적
    다만 부귀하면서 의롭지 않은 것 = 부정적
    ** 공자는 부귀에 대해서 긍정적, 빈곤에 대해서도 긍정적으로 바라봄
    ''')
    st.divider()
    st.markdown('''
    <述而第七>18 <br>
    葉公問孔子於子路, 子路不對. 子曰, “女奚不曰, 其爲人也, 發憤忘食, <span style="color:blue">樂</span>以忘<span style="color:red">憂</span>, 不知老之將至云爾.” <br>
    섭공이 자로에게 공자에 대하여 물었는데 자로는 대답하지 않았다. (이 말을 듣고) 공자께서 말씀하셨다. “너는 어째서 ‘그의 사람됨은 무언가에 의욕이 생기면 먹는 것도 잊고, 도를 즐기느라 근심을 잊어, 늙음이 곧 다가오는 것도 알지 못한다’고 말하지 않았느냐?”
    ''', unsafe_allow_html=True)
    st.text('''
    樂 = (도를) 즐기다 
    도라는 덕목을 터득하고 나서야 즐길 수 있음
    도 < 락
    ''')
    st.divider()
    st.markdown('''
    <泰伯第八>08 <br>
    子曰, “興於詩, 立於禮, 成於<span style="color:green">樂</span>.” <br>
    공자께서 말씀하셨다. “시를 통해 순수한 감성을 불러일으키고, 예의를 통해 도리에 맞게 살아갈 수 있게 되며, <span style="color:blue">음악을 통해 인격을 완성한다</span>.”
    ''', unsafe_allow_html=True)
    st.text('''
    음악 = 인격 수양의 도구
    ''')
    st.divider()
    st.markdown('''
    <子罕第九>14 <br>
    子曰, “吾自<span style="color:red">衛</span>反<span style="color:blue">魯</span>, 然後<span style="color:green">樂</span>正, <span style="color:green">雅頌</span>各得其所.” <br>
    공자께서 말씀하셨다. “내가 위나라에서 노나라로 돌아온 뒤에야 음악이 바르게 되어 아와 송이 각각 제자리를 찾았다.”
    ''', unsafe_allow_html=True)
    st.text('''
    위나라 = 부정적
    노나라 = 긍정적
    아와 송 = 중립적
    어느 나라에 속한 음악이냐에 따라서 그 가치가 긍정/부정으로 변화함
    ''')
    st.divider()
    st.markdown('''
    <先進第十一>01 <br>
    子曰, “<span style="color:blue">先進</span>於<span style="color:green">禮樂</span>, <span style="color:blue">野人</span>也, <span style="color:red">後進</span>於禮樂, <span style="color:red">君子</span>也. 如用之, 則吾從先進.” <br>
    공자께서 말씀하셨다. “옛 사람들은 예(禮)와 음악에 있어서 <span style="color:blue">야인처럼 질박</span>했으나, 후대의 사람들은 예와 음악에 있어서 군자처럼 형식미를 갖추고 있다. 만일 내가 마음대로 택하여 쓸 수 있다면 나는 옛 사람들을 따르겠다.”
    ''', unsafe_allow_html=True)
    st.text('''
    야인처럼 질박함 = 긍정적
    ** 군자와 같은 형식미 = 부정적
    -> 음악에 있어서는 다른 기준을 가지고 있음
    ''')
    st.divider()
    st.markdown('''
    <先進第十一>12 <br>
    閔子侍側, 誾誾如也, 子路, 行行如也, 冉有子貢, 侃侃如也. 子<span style="color:blue">樂</span>. “若由也, 不得其死然.” <br>
    민자건은 공자를 곁에서 모실 때 더불어 즐거워하면서도 주장이 분명하였고, 자로는 강하고 용감하였으며, 염유․자공은 강직하였다. 공자께서는 이런 제자들과 지내며 즐거워하셨다. 그러나 “유(자로)와 같은 사람은 제 명대로 살지 못할 것이다.”라고 하셨다.
    ''', unsafe_allow_html=True)
    st.text('''
    즐겁다는 동사로 사용됨
    ''')
    st.divider()
    st.markdown('''
    <先進第十一>25<br>
    子路曾晳冉有公西華侍坐. 子曰, “以吾一日長乎爾, 毋吾以也. 居則曰, ‘不吾知也!’ 如或知爾, 則何以哉?” 子路率爾而對曰, “千乘之國, 攝乎大國之間, 加之以師旅, 因之以饑饉, 由也爲之, 比及三年, 可使有勇, 且知方也.” 夫子哂之. “求! 爾何如?” 對曰, “方六七十, 如五六十, 求也爲之, 比及三年, 可使足民. 如其<span style="color:green">禮樂</span>, 以俟君子.” “赤! 爾何如?” 對曰, “非曰能之, 願學焉. 宗廟之事, 如會同, 端章甫, 願爲小相焉.” “點! 爾何如?” 鼓瑟希, 鏗爾, 舍瑟而作, 對曰, “異乎三子者之撰.” 子曰, “何傷乎? 亦各言其志也.” 曰, “莫春者, 春服旣成, 冠者五六人, 童子六七人, 浴乎沂, 風乎舞雩, 詠而歸.” 夫子喟然歎曰, “吾與點也!” 三子者出, 曾晳後. 曾晳曰, “夫三子者之言何如?” 子曰, “亦各言其志也已矣.” 曰, “夫子何哂由也?” 曰, “爲國以禮, 其言不讓, 是故哂之.” “唯求則非邦也與?” “安見方六七十如五六十而非邦也者?” “唯赤則非邦也與?” “宗廟會同, 非諸侯而何? 赤也爲之小, 孰能爲之大?” <br>
    자로․증석․염유․공서화가 공자를 모시고 앉아 있을 때, 공자께서 말씀하셨다. “내가 너희들보다 나이가 조금 많기는 하지만, 그런 것을 의식하지 말고 얘기해 보아라. 평소에 말하기를 ‘나를 알아주지 않는다’라고 하는데, 만일 너희를 알아주는 사람이 있다면 어떻게 하겠는가?” 자로가 불쑥 나서면서 대답하였다. “제후의 나라가 큰 나라들 사이에 끼어 있어서 군대의 침략을 당하고 거기에 기근까지 이어진다 하더라도, 제가 그 나라를 다스린다면 대략 3년 만에 백성들을 용감하게 하고 또한 살아갈 방향을 알도록 하겠습니다.” 공자께서 미소지으셨다. “구(염유)야, 너는 어찌하겠느냐?” 염유가 대답하였다. “사방 60～70리 혹은 50～60리의 땅을 제가 다스린다면, 대략 3년 만에 백성들을 풍족하게 할 수 있습니다. <span style="color:red">하지만 그 곳의 예법이나 음악과 같은 것에 관해서는 군자를 기다리겠습니다</span>.” “적(공서화)아, 너는 어찌하겠느냐?” 공서화가 대답하였다. “저는 ‘할 수 있다’고 말하기보다는, 배우고자 합니다. 종묘에서 제사 지내는 일이나 혹은 제후들이 천자를 알현할 때, 검은 예복과 예관을 갖추고 조금이나마 도움이 되기를 바랍니다.” “점(증석)아 너는 어찌하겠느냐?” 거문고를 타는 소리가 점차 잦아들더니, 뎅그렁 하며 거문고를 밀어 놓고 일어서서 대답하였다. “세 사람이 이야기 한 것과는 다릅니다.” 공자께서 말씀하셨다. “무슨 상관이 있겠느냐? 또한 각기 자기의 뜻을 말한 것이다.” 증석이 말하였다. “늦은 봄에 봄옷을 지어 입은 뒤, 어른 5～6명, 어린 아이 6～7명과 함께 기수에서 목욕을 하고 무우에서 바람을 쐬고는 노래를 읊조리며 돌아오겠습니다.” 공자께서 감탄하시며 말씀하셨다. “나는 점과 함께 하련다.” 세 사람이 나가고 증석이 뒤에 남았다. 증석이 여쭈었다. “저 세 사람의 말이 어떻습니까?” 공자께서 말씀하셨다. “또한 각각 자기의 뜻을 이야기했을 뿐이다.” “<span style="color:green">선생님께서는 무엇 때문에 유의 말이 미소를 지으셨습니까?</span>” “<span style="color:red">나라를 다스리는 것은 예(禮)로써 해야 하는데 그의 말이 겸손하지 않았기 때문에 미소지은 것이다</span>.” “<span style="color:green">구(염유)의 경우는 나라를 다스리는 것이 아니지 않습니까?</span>” “<span style="color:green">어찌 사방 60～70리 또는 50～60리인데 나라가 아니라고 생각하는 것이냐?</span>” “적(공서화)의 경우는 나라를 다스리는 것이 아니지 않습니까?” “종묘의 일과 천자 알현하는 일이 제후의 일이 아니고 무엇이겠느냐? 적의 일을 작은 일이라고 한다면 누구의 일을 큰일이라고 할 수 있겠느냐?”
    ''', unsafe_allow_html=True)
    st.text('''
    예법과 음악을 동일하게 생각
    ''')
    st.divider()
    st.markdown('''
    <子路第十三>03 <br>
    子路曰, “衛君待子而爲政, 子將奚先?” 子曰, “必也正名乎!” 子路曰, “有是哉, 子之迂也! 奚其正?” 子曰, “野哉, 由也! 君子於其所不知, 蓋闕如也. 名不正, 則言不順, 言不順, 則事不成, 事不成, 則<span style="color:green">禮樂</span>不興, <span style="color:green">禮樂</span>不興, 則刑罰不中, 刑罰不中, 則民無所錯手足. 故君子名之必可言也, 言之必可行也. 君子於其言, 無所苟而已矣.” <br>
    자로가 여쭈었다. “위나라 임금이 선생님을 모시고 정치를 한다면, 선생님께서는 장차 무엇을 먼저 하시겠습니까?” 공자께서 말씀하셨다. “반드시 명분을 바로잡겠다. 자로가 말하였다. “그런 것도 있습니까? 세상물정 모르시는 선생님이시여! 어째서 그것을 바로잡겠다고 하십니까?” 공자께서 말씀하셨다. “어리숙하구나, 유(자로)야! 군자는 자기가 알지 못하는 것에 대해서는 대체로 가만히 내버려두는 것이다. <span style="color:red">명분이 바르지 못하면 말이 사리에 맞지 않고, 말이 사리에 맞지 않으면 일이 이루어지지 않고, 일이 이루어지지 않으면 예와 음악이 흥성하지 못하고, 예와 음악이 흥성성하지 모사면 형벌이 적절하지 않고, 형벌이 적절하지 않으면 백성들은 살아갈 방도가 없다.</span> 그러므로 군자는 명분을 세우면 반드시 그에 대해 말을 할 수 있고, 말을 하면 반드시 실천을 할 수 있다. 군자는 그 말에 대해서 구차히 하는 일이 없어야 하는 것이다.”
    ''', unsafe_allow_html=True)
    st.text('''
    명분 < 말 < 일이 이루어짐 < 예악 흥성 < 형벌 적절하지 않음 < 백성이 못 삼
    예악은 덕치를 위한 중요한 요소!
    ''')
    st.divider()
    st.markdown('''
    <子路第十三>15 <br>
    定公問, “一言而可以興邦, 有諸?” 孔子對曰, “言不可以若是其幾也. 人之言曰, ‘爲君難, 爲臣不易.’ 如知爲君之難也, 不幾乎一言而興邦乎?” 曰, “一言而喪邦, 有諸?” 孔子對曰, “言不可以若是其幾也. 人之言曰, ‘予<span style="color:red">無樂</span>乎爲君, 唯其言而莫予違也.’ 如其善而莫之違也, 不亦善乎? 如不善而莫之違也, 不幾乎一言而喪邦乎?” <br>
    정공이 여쭈었다. “한마디로 나라를 흥하게 할 수 있는 그런 말이 있습니까?” 공자께서 말씀하셨다. “말이란 그와 같이 결과를 기약할 수는 없는 것입니다. 그러나 사람들의 말에 ‘임금노릇 하기도 어렵고 신하노릇 하기도 쉽지 않다’고 합니다. 만일 임금노릇 하기가 어렵다는 것을 안다면, 한 마디 말로 나라를 흥하게 하기를 기약할 수 있지 않겠습니가?” “한마디로 나라를 잃을 수 있는 그런 말이 있습니까?” 공자께서 말씀하셨다. “말이란 그와 같이 결과를 기약할 수는 없는 것입니다. 그러나 사람들의 말에 ‘나는 임금노릇하는 데 즐거움이 없고, 다만 내가 말을 하면 내 뜻을 어기지는 않는다’고 합니다. 만일 그 말이 선하여 그것을 어기지 않는다면 또한 선하게 되지 않습니까? 만일 그 말이 선하지 않은데 그것을 어기지 않는다면, 한마디 말로 나라를 잃게 되기를 기약할 수 있지 않겠습니까?”
    ''', unsafe_allow_html=True)
    st.markdown('[본 문장 해석본 첨부](https://leeza.tistory.com/1065)')
    st.divider()
    st.markdown('''
    <憲問第十四>13 <br>
    子路問成人. 子曰, “若臧武仲之知, 公綽之不欲, 卞莊子之勇, 冉求之藝, 文之以<span style="color:green">禮樂</span>, 亦可以爲成人矣.” 曰, “今之成人者何必然? 見利思義, 見危授命, 久要不忘平生之言, 亦可以爲成人矣.” <br>
    자로가 완성된 인간에 대해서 여쭙자, 공자께서 말씀하셨다. “장무중의 지혜와 맹공작의 욕심 없음과 변장자의 용기와 염구의 재주를 가지고, 예절과 음악을 보태어 다듬는다면 완성된 인간이 될 수 있다.” 그리고는 다시 말씀하셨다.“오늘날의 완성된 인간이야 어찌 반드시 그러하겠느냐? 이익될 일을 보면 의로운가를 생각하고, 나라가 위태로운 것을 보면 목숨을 바치며, 오래된 약속일지라도 평소에 한 그 말들을 잊지 않는다면, 또한 완성된 인간이 될 수 있다.”
    ''', unsafe_allow_html=True)
    st.text('''
    완성된 인간이 되기 위한 조건 중 하나  = 예악
    ''')
    st.divider()
    st.markdown('''
    <憲問第十四>14 <br>
    子問公叔文子於公明賈曰, “信乎, 夫子不言, 不笑, 不取乎?” 公明賈對曰, “以告者過也. 夫子時然後言, 人不厭其言, <span style="color:blue">樂</span>然後<span style="color:blue">笑</span>, 人不厭其笑, 義然後取, 人不厭其取.” 子曰, “其然? 豈其然乎?” <br>
    공자께서 공명가에게 공숙문자에 대해서 물으셨다. “정말입니까? 그 분은 말하지도 않고 웃지도 않으며 재물을 취하지도 않습니까?” 공명가가 대답하였다. “선생님께 말씀드린 사람이 지나쳤습니다. 그 분은 말할 때가 된 후에 말하기 때문에 남들이 그의 말을 싫어하지 않고, 즐거운 연후에 웃기 때문에 남들이 그의 웃음을 싫어하지 않으며, 의로운 것임을 안 후에 취하므로 남들이 그의 취함을 싫어하지 않는 것입니다.” 공자께서 말씀하셨다. “그렇습니까? 어찌 그럴 수 있습니까?”
    ''', unsafe_allow_html=True)
    st.text('''
    즐거움을 느낀 뒤에야 웃는 것이 타당하다.
    ''')
    st.divider()
    st.markdown('''
    <衛靈公第十五>10 <br>
    顔淵問爲邦. 子曰, “行夏之時, 乘殷之輅, 服周之冕, <span style="color:blue">樂則韶舞</span>. <span style="color:red">放鄭聲</span>, 遠佞人. <span style="color:red">鄭聲淫</span>, 佞人殆.” <br>
    안연이 나라를 다스리는 데 대하여 여쭙자, 공자께서 말씀하셨다. “하나라의 역법을 쓰고, 은나라의 수레를 타며, 주나라의 예관을 쓰고, 음악은 순임금의 것을 따르며, 정나라의 음악을 몰아내고, 교묘하게 말 잘하는 사람을 멀리 해야 한다. 정나라의 음악은 음란하고, 교묘하게 말 잘하는 사람은 위태롭기 때문이다.”
    ''', unsafe_allow_html=True)
    st.text('''
    순임금의 음악을 칭송
    정나라의 음악은 음란하기 때문에 몰아내야 함
    ''')
    st.divider()
    st.markdown('''
    <季氏第十六>02 v
    孔子曰, “天下<span style="color:blue">有道</span>, 則<span style="color:green">禮樂</span>征伐自<span style="color:blue">天子出</span>, 天下<span style="color:red">無道</span>, 則<span style="color:green">禮樂</span>征伐自<span style="color:red">諸侯出</span>. 自諸侯出, 蓋十世希不失矣, 自大夫出, 五世希不失矣, 陪臣執國命, 三世希不失矣. 天下有道, 則政不在大夫. 天下有道, 則庶人不議.” <br>
    공자께서 말씀하셨다. “천하도 도(道)가 행해지면 예악과 정벌이 천자로부터 나오고, 천하에 도가 행해지지 않으면 예악과 정벌이 제후로부터 나온다. 그것이 제후로부터 나오면 대체로 십대 안에 정권을 잃지 않는 일이 드물고, 그것이 대부로부터 나오면 오대 안에 정권을 잃지 않는 일이 드물며, 그것이 가신(家臣)으로부터 나오면 삼대 안에 정권을 잃지 않는 일이 드물다. 천하에 도가 행해지면 정권이 대부에게 있지 않으며, 천하에 도가 행해지면 일반 백성들이 정치를 논하지 않는다.”
    ''', unsafe_allow_html=True)
    st.text('''
    천자 > 제후 > 대부 > 가신 
    도가 이뤄지는 것 = 군군신신부부자자
    위계질서, 신분제를 중시함
    ''')
    st.divider()
    st.markdown('''
    <季氏第十六>05 <br>
    孔子曰, “<span style="color:blue">益者三樂</span>, <span style="color:red">損者三樂</span>. <span style="color:blue">樂節禮樂, 樂道人之善, 樂多賢友, 益矣.</span> <span style="color:red">樂驕樂, 樂佚遊, 樂晏樂, 損矣.</span>” <br>
    공자께서 말씀하셨다. “좋아하면 유익한 것이 세 가지가 있고 좋아하면 해로운 것이 세 가지가 있다. 예악(禮樂)의 절도를 따르기를 좋아하고, 남의 좋은 점을 말하기를 좋아하고, 현명한 벗을 많이 사귀기를 좋아하면 유익하다. 교만하게 즐기기를 좋아하고, 방탕하게 노는 데 빠지기를 좋아하고, 주색에 싸여 음란하게 놀기를 좋아하면 해롭다.”
    ''', unsafe_allow_html=True)
    st.text('''
    예악의 절도, 남의 좋은 점 말하기, 현명한 벗 사귀기 = 긍정적
    교만하게 즐기기, 방탕하게 놀기, 음란하게 놀기 = 부정적
    ''')
    st.divider()
    st.markdown('''
    <陽貨第十七>11 <br>
    子曰, “禮云禮云, 玉帛云乎哉? <span style="color:green">樂云樂云</span>, 鐘鼓云乎哉?” <br>
    공자께서 말씀하셨다. “예(禮)가 어떻다, 예가 어떻다 말들 하지만, 그것이 옥이나 비단을 말하는 것이겠는가? 음악이 어떻다, 음악이 어떻다 말들 하지만, 그것이 종이나 북을 말하는 것이겠는가?”
    ''', unsafe_allow_html=True)
    st.text('''
    종이나 북같은 타악기는 음악으로 치지 않는다
    ''')
    st.divider()
    st.markdown('''
    <陽貨第十七>18 <br>
    子曰, “惡紫之奪朱也, 惡<span style="color:red">鄭聲</span>之亂<span style="color:green">雅樂</span>也, 惡利口之覆邦家者.” <br>
    공자께서 말씀하셨다. “자주색이 붉은색을 침해하는 것을 미워하고, 정나라 음악이 아악을 어지럽히는 것을 미워하며, 기민한 말재주가 나라를 뒤엎는 것을 미워한다.”
    ''', unsafe_allow_html=True)
    st.text('''
    정나라 음악 = 부정적
    鄭聲 소리 성자를 사용
    아악 = 긍정적 
    雅樂 우아할 아, 음악 악자를 사용
    ''')
    st.divider()
    st.markdown('''
    <陽貨第十七>21 <br>
    宰我問, “三年之喪, 期已久矣. 君子三年不爲禮, 禮必壞, <span style="color:red">三年不爲樂, 樂必崩.</span> 舊穀旣沒, 新穀旣升, 鑽燧改火, 期可已矣.” 子曰, “食夫稻, 衣夫錦, 於女安乎?” 曰, “安.” “女安則爲之! 夫君子之居喪, 食旨不甘, <span style="color:red">聞樂不樂</span>, 居處不安, 故不爲也. 今女安則爲之!” 宰我出. 子曰, “予之不仁也! 子生三年, 然後免於父母之懷. 夫三年之喪, 天下之通喪也, 予也有三年之愛於其父母乎!” <br>
    재아가 여쭈었다. “삼년상은 기간이 너무 깁니다. 군자가 삼 년 동안 예(禮)를 행하지 않으면 예가 반드시 무너지고, 삼 년 동안 음악을 하지 않으면 음악이 반드시 무너질 것입니다. 묵은 곡식은 다 없어지고 새 곡식이 등장하며, 불씨를 얻는 나무도 다시 처음의 나무로 돌아오니, 일 년이면 될 것입니다.” 공자께서 말씀하셨다. “쌀밥을 먹고 비단옷을 입는 것이 너에게는 편안하냐?” “편안합니다.” “네가 편안하다면 그렇게 하여라. 대체로 군자가 상을 치를 때는, 맛있는 것을 먹어도 맛이 없고, 음악을 들어도 즐겁지 않으며, 집에 있어도 편하지 않기 때문에 그렇게 하지 않는 것이다. 지금 네가 편안하다면 그렇게 하여라.” 재아가 밖으로 나가자 공자께서 말씀하셨다. “여(재아)는 인(仁)하지 못하구나! 자식은 태어나서 삼 년이 지나 연후에야 부모의 품에서 벗어난다. 대체로 삼년상은 천하에 공통된 상례(喪禮)이다. 여도 그 부모에게서 삼 년간의 사랑을 받았겠지?”
    ''', unsafe_allow_html=True)
    st.text('''
    예와 악을 구분지어 언급
    ''')
    st.divider()
    st.markdown('''
    <微子第十八>04 <br>
    齊人歸<span style="color:red">女樂</span>, 季桓子受之, 三日不朝, 孔子行. <br>
    제나라 사람이 여자 가무단을 보내 오자, 계환자가 이를 받았다. 이들과 즐기느라 사흘이나 조회를 열지 않자, 공자께서는 노나라를 떠나셨다.
    ''', unsafe_allow_html=True)
    st.text('''
    락 = 여색, 부정적
    ''')
    st.divider()
    
elif sidebar == "說":
    st.title("說이 등장하는 문장")
    st.markdown('''
    <學而第一>01 <br>
    子曰, “<span style="color:blue">學</span>而時<span style="color:blue">習</span>之, 不亦<span style="color:blue">說</span>乎? 有朋自遠方來, 不亦樂乎? 人不知而不慍, 不亦君子乎?” <br>
    공자께서 말씀하셨다. “배우고 때때로 그것을 익히면 또한 기쁘지 않은가? 벗이 먼 곳에서 찾아오면 또한 즐겁지 않은가? 남이 알아주지 않아도 성내지 않는다면 또한 군자답지 않은가?”
    ''', unsafe_allow_html=True)
    st.text('''
    說 = 기쁘다
    樂 = 즐겁다
    學, 習, 朋自遠方來, 君子 = 긍정적
    慍 = 성내다, 부정적
    ''')
    st.divider()
    st.markdown('''
    <公冶長第五>05 <br>
    子使漆彫開仕. 對曰, “吾斯之未能信.” 子<span style="color:blue">說</span>. <br>
    공자께서 칠조개에게 벼슬살이를 시키려 하시자, 그가 말하였다. “<span style="color:blue">저는 아직 그 일에 자신이 없습니다</span>.” 이에 공자께서 기뻐하셨다.
    ''', unsafe_allow_html=True)
    st.text('''
    자신이 없다 = 겸손하다
    說 = 기쁘다, 긍정적
    ''')
    st.divider()
    st.markdown('''
    <雍也第六>10 <br>
    冉求曰, “非<span style="color:red">不說</span>子之道, 力不足也.” 子曰, “力不足者, 中道而廢. 今女畵.” <br>
    염구가 말하였다. “선생님의 도(道)를 좋아하지 않는 것은 아니지만, 제 능력이 부족합니다.” 공자께서 말씀하셨다. “능력이 부족한 자는 도중에 가서 그만두게 되는 것인데, 지금 너는 미리 선을 긋고 물러나 있구나.”
    ''', unsafe_allow_html=True)
    st.text('''
    說 = 좋아하다
    ''')
    st.divider()
    st.markdown('''
    <雍也第六>26 <br>
    子見南子, 子路<span style="color:red">不說</span>. 夫子矢之曰, “予所否者, 天厭之! 天厭之!” <br>
    공자께서 남자를 만나시자, 자로가 좋아하지 않았다. 이에 선생님께서 맹세하셨다. “내게 잘못된 것이 있다면 하늘이 나를 버리실 것이로다! 하늘이 나를 버리실 것이로다!”
    ''', unsafe_allow_html=True)
    st.text('''
    說 = 좋아하다
    ''')
    st.divider()
    st.markdown('''
    <子罕第九>23 <br>
    子曰, “法語之言, 能無從乎? 改之爲貴. 巽與之言, 能無<span style="color:blue">說</span>乎? 繹之爲貴. <span style="color:red">說</span>而不繹, 從而不改, 吾末如之何也已矣.” <br>
    공자께서 말씀하셨다. “올바른 말로 일러주는 것을 따르지 않을 수 있겠는가? 그러나 중요한 것은 실제로 잘못을 고치는 것이다. <span style="color:blue">은근하게 타이르는 말</span>에 기뻐하지 않을 수 있겠는가? 그러나 <span style="color:blue">중요한 것은 그 참뜻을 찾아 실천하는 것</span>이다. <span style="color:red">기뻐하기만 하고 참뜻을 궁구하지 않거나, 따르기만 하고 실제로 잘못을 고치지 않는다면</span>, 나도 그런 사람은 끝내 어찌 할 수가 없구나.”
    ''', unsafe_allow_html=True)
    st.text('''
    은근하게 타이르는 말 = 긍정적
    참 뜻을 찾아 실천 = 긍정적
    기뻐하다 <<< 참뜻 궁구 
    따르다 <<< 잘못 교정
    ''')
    st.divider()
    st.markdown('''
    <先進第十一>03 <br>
    子曰, “回也非助我者也, 於吾言無所<span style="color:red">不說</span>.” <br>
    공자께서 말씀하셨다. “안회는 나를 도와주는 사람이 아니다. 그는 내가 하는 말에 대해 기뻐하지 않는 것이 없구나.”
    ''', unsafe_allow_html=True)
    st.text('''
    안회는 공자의 말을 기뻐하지 않음
    부정적으로 바라봄
    ''')
    st.divider()
    st.markdown('''
    <子路第十三>16 <br>
    葉公問政. 子曰, “近者<span style="color:blue">說</span>, 遠者來.” <br>
    섭공이 정치에 대해서 여줍자, 공자께서 말씀하셨다. “가까이 있는 사람들은 기뻐하고, 먼 데 있는 사람들은 찾아오도록 하는 것입니다.”
    ''', unsafe_allow_html=True)
    st.text('''
    지배를 받는 사람, 즉 민중을 기쁘게 하는 것이 가치있다.
    ''')
    st.divider()
    st.markdown('''
    <子路第十三>25 <br>
    子曰, “君子易事而難<span style="color:blue">說</span>也. <span style="color:green">說</span>之不以道, <span style="color:red">不說</span>也, 及其使人也, 器之. 小人難事而易說也. <span style="color:green">說</span>之雖不以道, 說也, 及其使人也, 求備焉.” <br>
    공자께서 말씀하셨다. “군자는 섬기기는 쉬어도 기쁘게 하기는 어렵다. 그를 기쁘게 하려 할 때 올바른 도리로써 하지 않으면 기뻐하지 않는다. 그러나 군자가 사람을 부릴 때는 그 사람의 역량에 따라 일을 맡긴다. 소인은 섬기기는 어려워도 기쁘게 하기는 쉽다. 그를 기쁘게 하려 할 때는 올바른 도리로써 하지 않더라도 기뻐한다. 그러나 소인이 사람을 부릴 경우에는 능력을 다 갖추고 있기를 요구한다.”
    ''', unsafe_allow_html=True)
    st.text('''
    올바른 도리로 기쁘게 해야 한다. 
    리더의 자질
    ''')
    st.divider()
    st.markdown('''
    <陽貨第十七>05 
    公山弗擾以費畔, 召, 子欲往. 子路<span style="color:red">不說</span>, 曰, “末之也已, 何必公山氏之之也?” 子曰, “夫召我者, 而豈徒哉? 如有用我者, 吾其爲東周乎?” 
    공산불요가 비 땅을 근거지로 하여 반란을 일으키고 공자를 부르자, 공자께서 가려 하셨다. 자로가 기분 나빠하며 말하였다. “가실 데가 없으시면 그만이지, 하필이면 공산씨에게로 가리셔 하십니까?” 공자께서 말씀하셨다. “나를 부르는 사람이 어찌 공연히 부르겠느냐? 나를 써 주는 사람이 있다면, 나는 그곳의 동쪽의 주나라로 만들 것이다.”
    ''', unsafe_allow_html=True)
    st.text('''
    비록 자신을 불러주는 사람이 반란자라고 하더라도, 마다하지 않는 모습. 
    자신을 필요로 하는 사람을 피하지 않고, 교화할 수 있다고 믿음 = 주나라, 긍정적
    ''')
    st.divider()
    st.markdown('''
    <堯曰第二十>01 <br>
    堯曰, “咨! 爾舜! 天之厤數在爾躬, 允執其中. 四海困窮, 天祿永終.” 舜亦以命禹. 曰, “予小子履敢用玄牡, 敢昭告于皇皇后帝, 有罪不敢赦. 帝臣不蔽, 簡在帝心. 朕躬有罪, 無以萬方, 萬方有罪, 罪在朕躬.” 周有大賚, 善人是富. “雖有周親, 不如仁人. 百姓有過, 在予一人.” 謹權量, 審法度, 脩廢官, 四方之政行焉. 興滅國, 繼絶世, 擧逸民, 天下之民歸心焉. 所重, 民食喪祭. 寬則得重, 信則民任焉, 敏則有功, 公則說. <br>
    요임금께서 말씀하셨다. “아아, 그대 순이여! 하늘의 정해진 뜻이 바로 그대에게 와 있으니, 진실로 중용의 도를 지키도록 하라. 천하가 곤궁해지면 하늘이 내려 주신 천자의 자리도 영원히 끊어질 것이다.” 순임금도 또한 이 말씀으로 우임금에게 명하셨다. 탕임금이 말씀하셨다. “소자 리는 감히 검은 황소를 바치며, 감히 위대하신 거룩하신 하느님께 밝게 아룁니다. 죄 있는 사람은 감히 용서하지 않겠으며, 하느님의 신하는 그 능력을 숨기지 않겠으며, 모든 일은 하느님의 뜻에 따라 행하겠습니다. 제 몸에 죄가 있다면 그것은 세상 백성들 때문이 아니지만, 세상 백성들에게 죄가 있다면 그 죄는 저 자신에게 있는 것입니다.” (은나라를 정벌한 후) 주나라에서 크게 은혜가 베풀어져, 착한 사람들이 부유해졌다. (무왕은 말하기를) “(주에게) 비록 지극히 가까운 친척은 있었을지라도, 어진 사람이 있는 것만은 못한 것이다”라고 하였다. 또한 “백성들에게 허물이 있다면 그 책임은 나 한 사람에게 있는 것이다”라고 하였다. 도량형을 신중히 바로잡고, 법도를 점검하고, 폐지했던 관직들을 정비하여, 사방의 정치가 행해지게 되었다. 멸망했던 성현들의 나라를 다시 일으키고, 끊어졌던 성현들의 집안에 대를 이어주고, 은거하며 살던 인물들을 등용하니, 천하의 백성들이 진심으로 따르게 되었다. 소중히 여기는 것은 바로 백성들의 양식과 상사(喪事)와 제사였다. 관대하게 대하면 많은 사람들을 얻게 되고, 신의가 있으면 백성들이 믿고 따르게 된다. 민첩하게 하면 공을 이루게 되고, 공정하게 하면 사람들이 기뻐하게 된다.
    ''', unsafe_allow_html=True)
    st.text('''
    순, 요, 우, 탕 -> 태평성대를 이끈 임금
    ''')
    st.divider()
    
elif sidebar == "논어전문":
    st.title('논어 전문 필터링')
    search_term = st.text_input("검색어를 입력하세요.")

    if search_term:
        filtered_text = [line for line in lunyu.split("\n") if search_term in line]
        if filtered_text:
            st.text("\n".join(filtered_text))
        else:
            st.text("검색어에 해당하는 내용이 없습니다.")
    else:
        # 검색어가 입력되지 않으면 전체 텍스트 표시
        st.text("검색어를 입력하세요.")

    
    st.markdown(lunyu_txt)
    st.markdown('''
    
    ''')
    st.divider()


# In[ ]:




