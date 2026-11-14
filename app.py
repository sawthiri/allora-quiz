import streamlit as st

#page setup
st.set_page_config(page_title = "quiz", page_icon= "🐡")
st.title("Lets see whether you're with me only for my biceps💔")
st.write("You have to answer all the questions")

questions = [
   {"question" :"OKayy Allora, let's start with easy \n What is the date of our first date",
   "options" :["March 5", "March 6", "March 7"],
   "answer" : "March 5"},
   {"question" : "Hmm.. what underwear color am i wearing now",
   "options" : ["lacey thong", "nothing at all", "boring one"],
   "answer" :"boring one"},
   {"question" : "What's the very first song that i send you?",
   "options" : ["You're In Love","Love Song","Dreams"],
   "answer" : "Love Song"},
   {"question" : "ANd the very first meal we cooked together?",
   "options" : ["Carbonara","Kbbq Pork","those seafood rice and eggs"],
   "answer" : "Kbbq Pork"}]

user_answers = []

for i, q in enumerate(questions):
   st.subheader(q["questions"])

   choices = st.radio("Pick one", q[options], key=f"q_{i}", index= None)
   user_answers.append(choice)
   st.write("------")

if st.button("Submit answers🎰"):
   
   score = 0
   for i,q in enumerate (questions):
      if user_anser[i]== q["answers"]:
         score +=1
   
   total = len(questions)
   st.header(f"You sccore {score} out of {total}")

   if score==total:
      st.balloons()
      st.success("Someone's obviously obessed. You gonna get reward for that full mark👅")
   elif score >= total//2:
      st.info ("Awwn babyboo what did you get wrong")
   else:
      st.warning("bro i knew it you gor distracted with other sidedish")
