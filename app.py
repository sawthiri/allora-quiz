import streamlit as st

#page setup
st.set_page_config(page_title = "quiz", page_icon= "🐡")
st.title("Lets see whether you're with me only for my biceps💔")
st.write("You have to answer all the questions. it might help if you actually know our playlists by heart🙄")

questions = [
   {"question" :"OKayy Allora, let's start with easy \n What is the date of our first date(☞ﾟヮﾟ)☞",
   "options" :["March 5", "March 6", "March 7"],
   "answer" : "March 5"},
   {"question" : "Hmm.. what underwear color am i wearing now(´･ω･`)?",
   "options" : ["lacey thong", "nothing at all", "boring one"],
   "answer" :"boring one"},
   {"question" : "What's the very first song that i send you?(#`O′)",
   "options" : ["You're In Love","Love Song","Dreams"],
   "answer" : "Love Song"},
   {"question" : "ANd the very first meal we cooked together?:O)",
   "options" : ["Carbonara","Kbbq Pork","those seafood rice and eggs"],
   "answer" : "Kbbq Pork"},
   {"question" : "How does how our first arguement went?ಥ_ಥ",
   "options" : ["Don't Remember","When was it even?","very very healthy"],
   "answer" : "very very healthy"},
   {"question" : "You know that I love you🍑",
   "options" : ["Do I?","Into a world that i can't even see with one eye","But this ain't a love song"],
   "answer" : "But this ain't a love song"},
   {"question" : "Your eyes are like heaven🧿",
   "options" : ["You're In Love","Mine(Taylor's version","This song"],
   "answer" : "This song"},
   {"question" : "ayyy the song of the very first edit i hard launch you?🎶",
   "options" : ["Dreams","Everywhere","Love it if we made it"],
   "answer" : "Everywhere"},
   {"question" : "Who kisssed who first?(○｀ 3′○)",
   "options" : ["Me","You","idkk mwuh mwuh"],
   "answer" : "You"},
   {"question" : "Who's the love of your life?(。・ω・。)",
   "options" : ["hehe my wife","my toe","my thumb"],
   "answer" : "hehe my wife"},]

user_answers = []

for i, q in enumerate(questions):
   st.subheader(q["question"])

   choice = st.radio("Pick one", q["options"], key=f"q_{i}", index= None)
   user_answers.append(choice)
   st.write("------")

if st.button("Submit answers🎰"):
   
   score = 0
   for i,q in enumerate (questions):
      if user_answers[i]== q["answer"]:
         score +=1
   
   total = len(questions)
   st.header(f"You sccore {score} out of {total}")

   if score==total:
      st.balloons()
      st.success("Someone's obviously obessed. You gonna get reward for that full mark👅")
   elif score >= total//2:
      st.info ("Awwn babyboo what did you get wrong but you will need to be punisnhed😤")
   else:
      st.warning("bro i knew it you gor distracted with  your sidedishes.⚰️")
