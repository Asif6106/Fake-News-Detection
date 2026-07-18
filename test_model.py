{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "37a049dc-fd57-41b7-8d40-fe5497286d6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a news article:\n",
      " WASHINGTON (Reuters) - The head of a conservative Republican faction in the U.S. Congress, who voted this month for a huge expansion of the national debt to pay for tax cuts, called himself a â€œfiscal conservativeâ€ on Sunday and urged budget restraint in 2018. In keeping with a sharp pivot under way among Republicans, U.S. Representative Mark Meadows, speaking on CBSâ€™ â€œFace the Nation,â€ drew a hard line on federal spending, which lawmakers are bracing to do battle over in January. When they return from the holidays on Wednesday, lawmakers will begin trying to pass a federal budget in a fight likely to be linked to other issues, such as immigration policy, even as the November congressional election campaigns approach in which Republicans will seek to keep control of Congress. President Donald Trump and his Republicans want a big budget increase in military spending, while Democrats also want proportional increases for non-defense â€œdiscretionaryâ€ spending on programs that support education, scientific research, infrastructure, public health and environmental protection. â€œThe (Trump) administration has already been willing to say: â€˜Weâ€™re going to increase non-defense discretionary spending ... by about 7 percent,â€™â€ Meadows, chairman of the small but influential House Freedom Caucus, said on the program. â€œNow, Democrats are saying thatâ€™s not enough, we need to give the government a pay raise of 10 to 11 percent. For a fiscal conservative, I donâ€™t see where the rationale is. ... Eventually you run out of other peopleâ€™s money,â€ he said. Meadows was among Republicans who voted in late December for their partyâ€™s debt-financed tax overhaul, which is expected to balloon the federal budget deficit and add about $1.5 trillion over 10 years to the $20 trillion national debt. â€œItâ€™s interesting to hear Mark talk about fiscal responsibility,â€ Democratic U.S. Representative Joseph Crowley said on CBS. Crowley said the Republican tax bill would require the  United States to borrow $1.5 trillion, to be paid off by future generations, to finance tax cuts for corporations and the rich. â€œThis is one of the least ... fiscally responsible bills weâ€™ve ever seen passed in the history of the House of Representatives. I think weâ€™re going to be paying for this for many, many years to come,â€ Crowley said. Republicans insist the tax package, the biggest U.S. tax overhaul in more than 30 years,  will boost the economy and job growth. House Speaker Paul Ryan, who also supported the tax bill, recently went further than Meadows, making clear in a radio interview that welfare or â€œentitlement reform,â€ as the party often calls it, would be a top Republican priority in 2018. In Republican parlance, â€œentitlementâ€ programs mean food stamps, housing assistance, Medicare and Medicaid health insurance for the elderly, poor and disabled, as well as other programs created by Washington to assist the needy. Democrats seized on Ryanâ€™s early December remarks, saying they showed Republicans would try to pay for their tax overhaul by seeking spending cuts for social programs. But the goals of House Republicans may have to take a back seat to the Senate, where the votes of some Democrats will be needed to approve a budget and prevent a government shutdown. Democrats will use their leverage in the Senate, which Republicans narrowly control, to defend both discretionary non-defense programs and social spending, while tackling the issue of the â€œDreamers,â€ people brought illegally to the country as children. Trump in September put a March 2018 expiration date on the Deferred Action for Childhood Arrivals, or DACA, program, which protects the young immigrants from deportation and provides them with work permits. The president has said in recent Twitter messages he wants funding for his proposed Mexican border wall and other immigration law changes in exchange for agreeing to help the Dreamers. Representative Debbie Dingell told CBS she did not favor linking that issue to other policy objectives, such as wall funding. â€œWe need to do DACA clean,â€ she said.  On Wednesday, Trump aides will meet with congressional leaders to discuss those issues. That will be followed by a weekend of strategy sessions for Trump and Republican leaders on Jan. 6 and 7, the White House said. Trump was also scheduled to meet on Sunday with Florida Republican Governor Rick Scott, who wants more emergency aid. The House has passed an $81 billion aid package after hurricanes in Florida, Texas and Puerto Rico, and wildfires in California. The package far exceeded the $44 billion requested by the Trump administration. The Senate has not yet voted on the aid. \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Prediction: Real News\n"
     ]
    }
   ],
   "source": [
    "import joblib\n",
    "import re\n",
    "import string\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import PorterStemmer\n",
    "\n",
    "# Load saved model and vectorizer\n",
    "model = joblib.load(\"fake_news_model.pkl\")\n",
    "vectorizer = joblib.load(\"tfidf_vectorizer.pkl\")\n",
    "\n",
    "# Initialize preprocessing tools\n",
    "stop_words = set(stopwords.words(\"english\"))\n",
    "stemmer = PorterStemmer()\n",
    "\n",
    "# Preprocessing function (same as training)\n",
    "def preprocess_text(text):\n",
    "    text = text.lower()\n",
    "    text = re.sub(r\"http\\S+|www\\S+\", \"\", text)\n",
    "    text = text.translate(str.maketrans(\"\", \"\", string.punctuation))\n",
    "    text = re.sub(r\"\\s+\", \" \", text).strip()\n",
    "\n",
    "    words = text.split()\n",
    "\n",
    "    filtered_words = []\n",
    "    for word in words:\n",
    "        if word not in stop_words:\n",
    "            filtered_words.append(stemmer.stem(word))\n",
    "\n",
    "    return \" \".join(filtered_words)\n",
    "\n",
    "# Take input from user\n",
    "news = input(\"Enter a news article:\\n\")\n",
    "\n",
    "# Preprocess\n",
    "clean_news = preprocess_text(news)\n",
    "\n",
    "# Convert to TF-IDF\n",
    "news_vector = vectorizer.transform([clean_news])\n",
    "\n",
    "# Predict\n",
    "prediction = model.predict(news_vector)\n",
    "\n",
    "# Display result\n",
    "if prediction[0] == 0:\n",
    "    print(\"\\nPrediction: Fake News\")\n",
    "else:\n",
    "    print(\"\\nPrediction: Real News\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
