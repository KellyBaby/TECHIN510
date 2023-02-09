{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Milestone 1\n",
    "Building on previous exercises, build an interactive application that asks the user a series of questions and then stores the user's answers for later analysis."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Requirements\n",
    "Your submission should include the following:\n",
    "- A Chatbot that asks three users a series of at least three questions.\n",
    "- Your chatbot should store the user's responses in a data structure, preferably a Pandas DataFrame, so that it can present a graphical analysis of the responses.\n",
    "- Your chatbot should provide at least one visualization, such as a vertical bar chart, that provides a basic summary and analysis of the user input."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example Code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a Basic Chatbot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Simple interactive chatbot\n",
    "# user = input(\"What is your name? \")\n",
    "# print(\"Type 'end' or 'quit' to quit.\")\n",
    "# while True:\n",
    "#     msg = input(\"Hi how can I help you? \")\n",
    "#     if (\"end\" in msg) | (\"quit\" in msg):\n",
    "#         break\n",
    "#     print(\"you said {} words and {} letters\".format(len(msg.split(\" \")), len(msg)),\n",
    "#         end=\"\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Initialize a DataFrame to Store User Input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os.path\n",
    "\n",
    "path = './user_data.csv'\n",
    "\n",
    "data_store = pd.DataFrame()\n",
    "check_file = os.path.isfile(path)\n",
    "if check_file:\n",
    "  data_store = pd.read_csv(path, index_col=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Run the Chatbot and Save Each User's Answers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is your name? fanny\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Happy to meet you! fanny\n",
      "I will ask a few questions. Press \"QT\" to quit.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you a student? no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ok get it.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How was your day? bad\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I'm Sorry to hear that!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many interviews have you received? 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You will get it!\n",
      "Thanks for your response. I've made a note of it.\n"
     ]
    }
   ],
   "source": [
    "## Simple interactive chatbot\n",
    "import requests\n",
    "\n",
    "class Question:\n",
    "    def __init__(self, question, validator, answer_processor):\n",
    "        self.question = question\n",
    "        self.validator = validator\n",
    "        self.answer_processor = answer_processor\n",
    "    \n",
    "    def _update_user_response(self, user_response):\n",
    "        self.user_response = user_response\n",
    "\n",
    "    def _check_format(self, text):\n",
    "        if 'Bye' in text:\n",
    "            print(\"Bye!\")\n",
    "            return None\n",
    "        if self.validator == str:\n",
    "            return True \n",
    "        elif self.validator == int:\n",
    "            try:\n",
    "                text = int(text)\n",
    "                return True\n",
    "            except:\n",
    "                return False\n",
    "        elif type(self.validator) == list and text in self.validator:\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "    \n",
    "    def ask_and_record(self):\n",
    "        temp = input(self.question)\n",
    "        check = self._check_format(temp)\n",
    "        while check == False:\n",
    "            temp = input(\"Answer Not Supported! \" + self.question)\n",
    "        if check == None:\n",
    "            return None\n",
    "        self._update_user_response(temp)\n",
    "        self.bot_answer = self.answer_processor(temp)\n",
    "        print(self.bot_answer)\n",
    "        return True\n",
    "\n",
    "def positive_vs_negative(text):\n",
    "    positive_url = \"https://ptrckprry.com/course/ssd/data/positive-words.txt\"\n",
    "    negative_url = \"https://ptrckprry.com/course/ssd/data/negative-words.txt\"\n",
    "\n",
    "    payload={}\n",
    "    headers = {}\n",
    "\n",
    "    negative_response = requests.request(\"GET\", negative_url, headers=headers, data=payload)\n",
    "    positive_response = requests.request(\"GET\", positive_url, headers=headers, data=payload)\n",
    "\n",
    "    negative_list = negative_response.text.split('\\n')[35:-1]\n",
    "    positive_list = positive_response.text.split('\\n')[35:-1]\n",
    "\n",
    "    positive_count = 0\n",
    "    negative_count = 0\n",
    "    text = str(text)\n",
    "    for word in text.split(' '):\n",
    "        if word in negative_list:\n",
    "            negative_count = negative_count + 1\n",
    "        if word in positive_list:\n",
    "            positive_count = positive_count + 1\n",
    "    if positive_count > negative_count:\n",
    "        return 1\n",
    "    elif positive_count < negative_count:\n",
    "        return -1\n",
    "    else:\n",
    "        return 0\n",
    "    \n",
    "def check_nums(text):\n",
    "    nums = int(text)\n",
    "    return 0 if nums == 0 else 1\n",
    "\n",
    "q_and_a = [\n",
    "    Question(\n",
    "        \"Are you a student?\", \n",
    "        ['yes', 'no'], \n",
    "        lambda a: \"Ok get it.\"\n",
    "    ),\n",
    "    Question(\n",
    "        \"How was your day?\", \n",
    "        str, \n",
    "        lambda a: [\"Oh yeah!\", \"Great to Hear!\", \"I'm Sorry to hear that!\"][positive_vs_negative(a)]\n",
    "    ),\n",
    "    Question(\n",
    "        \"How many interviews have you received?\", \n",
    "        int, \n",
    "        lambda a: [\"You will get it!\", \"Congrats!\"][check_nums(a)]\n",
    "    )\n",
    "]\n",
    "\n",
    "user_info = Question(\"What is your name?\", str, lambda a : \"Happy to meet you! \" + a)\n",
    "if user_info.ask_and_record() != None:\n",
    "    print(f'I will ask a few questions. Press \"QT\" to quit.')\n",
    "\n",
    "    for qa in q_and_a:\n",
    "        if qa.ask_and_record() == None:\n",
    "            break\n",
    "        new_response = {'user_name': user_info.user_response, 'question': qa.question, 'user_answer': qa.user_response, 'bot_answer': qa.bot_answer}\n",
    "        new_data = pd.DataFrame(new_response, index=[0])\n",
    "        data_store = pd.concat([data_store, new_data]) if data_store.empty == False else new_data\n",
    "\n",
    "    print(\"Thanks for your response. I've made a note of it.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### View Cumulative Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_store.to_csv(path)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Analyze Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 6, 3]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7fd011926d30>"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAQUAAADnCAYAAAAXbUOsAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAAjY0lEQVR4nO3de1xUZf4H8M8zMwwXwcNFBO94YYQBRKW8pdtmmnndVCwvJbtledtbVka1P/dUW+kWtmu/n61mrZZuq9aWJm66m3bTLqICBxDFikQFFZHhDnN5fn+cwRgEGWDgHGa+79eLF3Jm5pzvjGc+8zxnznkexjkHIYTU0yhdACFEXSgUCCEOKBQIIQ4oFAghDigUCCEOKBQIIQ4oFAghDigUCCEOKBQIIQ4oFAghDnRKF0BIQ8ePH++p0+m2AIgFfWi1lg1AlsViWZKQkHC5rSuhUCCqotPptoSHh0eHhoZe02g0dGFOK9hsNnblyhVjUVHRFgCz2roeSmKiNrGhoaFlFAitp9FoeGhoqAlyK6vt63FRPYS4ioYCoe3sr1273tcUCoQQBxQKpEs6ffq0PjIyMqbhslWrVvVes2ZNmCvWPWrUqKHO3r9Pnz5xCQkJDvePiooyNq6vrUaNGjX0888/93PFupxBoUBIA2azuU2Pq6ys1J49e9YLAE6cOOHj0qI6GYUCcUt/+tOfeg4ePDjGYDAYZ8yYMQgAysrKNPPmzYuIjY2Njo6ONm7fvj0QADZs2BAyderUQRMnThwyYcIEg1ar5YGBgRYASEtL84mLi4uOiooyGgwGoyRJ3k1t75577il5++23gwHg7bffDp47d25J/W1VVVUsMTExwmAwGKOjo40fffRRwM2WV1RUsBkzZgwyGAzG6dOnD6qpqWEd+mI1Ql9JEre0YcOG8B9//FHy9fXlxcXFWgB4+umne91xxx1lu3fvzi8uLtbecsst0bNmzSoDgBMnTvhnZmZmh4WFWQHg4MGD3wHAa6+9FrpixYpLy5cvL6mpqWEWi6XJ7S1cuPBaUlLSwOeee+7SgQMHArdv3/79rl27QgBg3bp1PQHgzJkzOSdPnvSZNm1a5HfffZfV3PJXXnmlp6+vr+3MmTM533zzje9tt91m7PAXrAFqKZAuibGmPzzrlw8dOrR69uzZAzdu3Bjs5eXFAeDTTz/t/uqrr/aKiooyjh8/fmhtbS07e/asHgAmTJhQVh8IDY0dO7YyJSWl1zPPPBOel5en9/f3b/KbkdDQUKsgCJbNmzcHDRkypNrf399Wf9vRo0f9Fy9efBUARowYUdO7d+86SZJ8mlv+5Zdf+j/wwANXAWD06NHVBoOhqj2vVWtRKJAuKSwszGIymbQNl5WUlGh79OhhAYDDhw/nrVy58srx48e7xcfHG81mMzjneO+9987m5ubm5Obm5hQWFkojR46sAQA/Pz9bU9tZtmxZyZ49e876+vrapk6dati7d29AczUlJiZeW7169YAFCxaUNFze3ODINxs0ubnQ6wwUCqRLEgTB1rNnT/OePXsCAODSpUvaTz/9VJg4cWKF1WrFd999p585c2b5xo0bz5eXl2tNJpP2jjvuKEtJSQmz2eT3/5EjR3xb2k5OTo4+Ojq69g9/+MPlu+66qzQ9Pb3ZxyxatOjaypUri+bMmVPWcPn48eMrtm/fHgwAmZmZ3oWFhfphw4bVOLP82LFjPmfOnOm0bx4AOqZAurBt27b9sGLFiv5PPvlkPwB48sknL8bExNTW1tayhQsXDiwvL9dyztnSpUsv9ejRw7p27dqLjzzySP+oqCgj55z17du39vDhw2dvto133nknePfu3SE6nY6HhoaaX3rppYvN3TcoKMj2wgsvFDVevnr16ssPPPDAAIPBYNRqtdi0aVO+r68vb275448/fnn+/PkDDQaDMSYmpiouLq6y/a+W8xjN+0DUJCMjIz8+Pr5Y6Tq6soyMjB7x8fERbX08dR8IIQ4oFAghDigUCCEO6EAjAUQhBEAvAL2b+S0A8LL/6NaZ78t43fqLYQAsAMwA6gBcBXARQGFTv/PXTq/ozKdE2o5CwZOIghZANICEBj/DAbTqKy8drOcA9G/NYyKSU4sBnACQBuA4gOP5a6f/2Jp1kM5BoeDORKEPgDsB3II2BoAL9QBwl/0HwA1BcQzAJ3sW9FWmOnIdhYK7EYURkIfimgVgpMLVtKRxUNSV1lhtl8tqmODnVeqt05ojklMTXLnB/LXTj7d0H8ZYwpIlSy698cYb5wFgzZo1YRUVFdr169c3e45Cc4qLi7VbtmwJTk5OvtLax/bp0ycuLS3tVK9evZq+4KKDUCh0daKgB3AH5BCYCaCfsgW1i77OChSV1fQvKqvp763TVitShF7P9+/fH1RYWFjU3jfk1atXtW+++WbPpkLBYrFAp1PfW5C+feiqRGEkRGELgGIAHwNYga4dCDeotVhbPA25I2i1Wr548eIrL7744g0Dtly8eFE3ZcqUwbGxsdGxsbHRBw8e7AbcOMBLZGRkzOnTp/WPPfZY34KCAu+oqCjj0qVL++7bty9g9OjRhpkzZw4cOnRoDABMmjRpcExMTPSQIUNiXnnllR6d90ybpr6YIs0TBR8A90EOgFEKV+PWnnjiictxcXExoig6nLa8dOnSfqtWrbo0ZcqUiry8PP2UKVMiv//+++zm1pOSknJ+xowZvrm5uTkAsG/fvoDMzMxuJ0+ezI6KiqoDgB07duSHhYVZKyoq2IgRI4z333//tfDw8Buu2OwsFApdgSgMArAcwK8AhChcjUcIDg62zZs37+ratWt7+vr6Xr+C8siRI93z8vKut2AqKiq0165da1WLe9iwYZX1gQAA69atC0tNTQ0EgKKiIq/s7Gyf8PDwTr3eoSEKBTUThTEA1gC4G4By19J6qKeeeurSyJEjjfPnz79+LQbnHGlpaacaj6ug0+l4/dWXAFBbW9vs/1fDy7T37dsX8NlnnwWkpaXlBgQE2EaNGjW0urpa0W49HVNQI1GIhih8AOArAFNBgaCIsLAw68yZM6/94x//uN7PHz9+fFn9iEkAcPToUV8AiIiIqE1PT+8GAF9++aXfhQsXvAFAEARrZWVls++z0tJSrSAI1oCAANvJkyd9MjIyunXcM3IOtRTURBT6AXgWwGIA2hbu7RH2/vq2Vj9Gw5g1xF9f1DPA57JWw5ocPMVZzzzzTNG2bdtC6//evHlzwZIlS/obDAaj1Wplo0ePLh83bty5xYsXX9uxY0dIVFSUcfjw4ZUDBgyoAYDw8HBrQkJCRWRkZMzEiRNNM2fONDVc/9y5c02bN28ONRgMxsGDB9fEx8cr1m2oR5dOq4EoBAN4GsBKAKofCTjFnHjkNeuc1r9bnfDGrF4I6z/IJevSaZi5R4B3Yai/9xUlRzLqbO29dJpaCkoSBQ2A30M+biAoW4z7sdi4V5Gppv/Virqw3oLPOcFPX9byowgdU1CKKAwF8CWAFFAgdCiz1eb9Y0lV5I9XKwdYrDbqlrWAWgqdTW4drALwPLpAV8GdmKrNPSprrUKfQJ98ajU0j1oKnemn1sHLoEBQhMVm8+qIVkNaWlpCfn7+9au5Lly4EFZQUNC7TTVaLNrCwsLQlu95o4yMjDibrX3Pi0KhM4iCBqLwOIB0AGMVroZAbjWcuVQRY6qq6+6K9THGuMlkCjKbze1ufVssFm1xcXHPpm7rjC8GqPvQ0UShB4DdAH6ucCWkkfpWQ3Ct5XKfQN+C9nxDwRjjISEhVwoLC8P69+9/oeFtdXV1uvz8/AFms1kPAH379j0nCEJlQUFBb41GY+3Tp88lAJAkKSYyMjKvoKCgb11dnXdWVpbR39+/LDAw0FRYWNhLp9OZa2pq/OLi4rJPnz492Gw26znnmtDQ0Evh4eEuG+yWQqEjiUIcgL0AIhSupMsatmWAS9eXueTGcV1KKut61phtPhEhft/rtBqrVqtNiIyMrLZarWzIkCHVu3btyg8ICGjxfIfw8PDL2dnZMWazuXjZsmUhb731VunRo0d9MzMz+y1YsOCiIAgV27Zt67Fp06YhGzZsyGhuPf369Tufl5fnGxsbmwMApaWlAVVVVd2MRmO2r69vHQAMGjQo38vLy2q1WllOTo4xJCTkmpeXl0uul6DuQ0cRhdkAjoICoUuoqrN0P3u5Irq6zurj7e1ty83NzcnLy8v28vLiKSkpTvXvdTqdLSgo6Kperw/eunXrVQBIS0vzO3ToULeCgoL+WVlZxoSEhJ4PPvggt1gsrXrv+fn5VdYHAgAUFRWFZWVlGU+dOhVtNpu9qqurXXaMikLB1USBQRTWAHgfgL/S5RDn1Vlt3t9dqYgCfupHjB8/vuLs2bPely5d0k6aNGmwwWAwxsfHR33zzTe+AJCamuofFRVlXLBggSY6Otro6+t7RZKkHrfffnt4XV0dXnrppd7/+c9/NImJifjqq68KDx06dGn9+vWlJpOJjR49uqfVKn+4l5eXayZPnuxTV1eH3Nxc/dKlS/UxMTHRCQkJQ7Ozs/UajeZ6S6W0tDSgvLw8IDo6Ojc2NjbH19e32mazuey9TKHgSqLgB2AX5FOVPecUOjdi41wLxliRqSbcbDbjwIED3ePi4qpXr17dOz4+vurMmTM5zz///IWkpKSBAJCSkhK+YcOGH999913b119/nRsYGGj29/cv45xr9Xo9nnrqqYtTpkyp+eSTT64+/PDD1wDAZrNpQ0JCrFFRUbWHDh0SAOCdd97pOWbMGOj1eixbtqxPcnKyNTs7+9TLL798ftWqVQ4HHa1Wq1ar1Vq1Wq2tqqrKp6qqyqXXS1AouIoo9AZwBECi0qWQ9qmtqcbPx93aJy5++PC+ffuaf/e73xV/++23AQ899NBVAJg1a1Z5aWmp7urVq9oxY8ZUPP744/3effddVlxcrPXy8kJwcPAVNPhQ0Ov1FVVVVd0kSTKWlpb2sVrlwWPmzZt3KTU11TsrK8v43nvvhd599911ZWVlmvT09G5PPPGEZujQoSOXL18+5MqVKw7H/oKCgkyccyZJkvH8+fO9/fz8XHq9BB1odAVR6A/gEIDBSpdC2s/bxxe7DnwBAFp/b51e7+3d5FeBjDH+4osvFt1zzz2mPXv2COPGjYv++OOPz/j5+Vk0Gk1Nv379LkIe/4JHRkZ+DwCHDx8O8fLy6gYACxcuLH3++ef7hIaGnj516pRxyZIlUllZmSYgIMBy+vTpzObq02g0PCoqKq+p2+Lj46WMjIx2jd5ELYX2EoXBAD4HBYJbqqi1CD9cqRwyZsyYir///e8hgDwGQlBQkCU4ONiWnZ3tPWrUqOoXXnihKC4urjIrK8vhgF/37t2tFRUVTb7PBEGwxcfHVy5durT/nXfeadLpdAgODrb17du37q233goCAJvNhq+++qpTh6WjlkJ7iIIBcguhj9KluKumvkLsbJV1lu4rk58tT175kN5gMBh9fX1tW7du/QEA/vznP/c8evRod41Gww0GQ3ViYqLp3LlzXvWPnTp1avkrr7zSKyoqyvjYY48VNl73vffee+3BBx8ctG/fvtP1y959993vH3744QHr1q3rZbFY2OzZs0vGjh3baYPY0qXTbSUPkfY5PDAQusql067mp9eVD+rRLU+jYap+09Cs00qQB0OhFoKHqaqzBPxwtXKwjXO3/maJQqG1RCEMciC49lQ70iVU1lqE/OLKQe7cwqZQaA1R8AbwAYAhSpdClFNRawm8UFrttvPbUSi0zuugqxwJgJLKurCrFbXBStfRESgUnCUKj0Ked4EQAMBFU01ERY1F8dGXXY1CwRmicBfkgVEIuY5zzs6VVA2us9i8Wr5310HnKbREFCIB7AQNua6IRZ9McOn6dtz5RYv3ie8XhAceXonH1/wJALDtb6+hqqoSy1cl33Bfi83mlX+1csiQUP/c1n5VmZycHL527drr09KNGDEi6uTJk7mtWUdHoJbCzYhCd8jjIQQqXAnpRHpvb3zy8Ue4VnLVqfvXmK1+565VRbR2Oxs2bOjV8G81BAJAodCSrQCilC6CdC6tVofEhUnY/sbGG24ruVqMVY8sxsLpE7Fw+kScPPY1ACD/fGHwuPETYoxGY/TChQsH9O7dO66wsFAHND2r9IoVK/rU1tZqoqKijLNmzRoIAH5+fiMAYPr06YN27tx5fYTvuXPnRmzdujXQYrFg6dKlfWNjY6MNBoPx5Zdf7pAZqikUmiMKiwDMVroMooz7kpZg/4e7UV7mMKET/vzHZNy/ZDn+kXoIKZu34dnVvwMA/O3Vdbh1/B3eJzKk7+fMmXOtsLBQX/+YHTt25GdnZ59KT0/P2bRpU1hRUZF248aNF+oHc9m7d+8PDtu+776SnTt3BgFATU0NO3LkSPfExETTX/7ylx6CIFizsrJOZWRknNq2bVtobm6uHi5GxxSaIgrhADYoXQZRjn9Ad8yYOx//eGszfHx+usbp6y8/w/d51y9TQEV5OSorypF+7Gusf2M7Kyipipg7d+7p7t27Xx8arbWzSicmJppWr17dv7q6mr3//vvCqFGjyv39/fl///vf7rm5uX579+4NAoDy8nJtTk6OT8MZrF2BQqFpfwPglt9BE+fd/9ByzJ92O35x76Lry7jNhrc/PAgfX8cLF+vPcKw2W/0vl9deHxSlLbNK+/n58TFjxpT/61//6r5z586gBQsWlNi3wVJSUs7NnTu3Q+esoO5DY3K34RdKl0GUJwQF4a4Z9+CDf75zfdnYn92Bf2574/rfudkSAGDErWNwcN8HAIAP9+3vU1ZWpgVuPqu0TqfjzU1ZP3/+/JKtW7f2OHbsWMCcOXPKAGDy5Mmm119/PbT+MZmZmd5lZWUufw9TS6Eh6jaojjNfIXakxY/8Gv/cuuX6308+tw4vPvMEEiffBqvVipGjx+J/XnoVSx99Esm/XoIDH32AW0bfpgntGcYFQbDebFbpRYsWXYmOjjbGxsZWNT6uMHv27LJly5YNnDRpUqmPjw8HgEcffbQ4Pz/fOy4uLppzzoKDg8379+//ztXPmS6dbkgUPgS1ElrkqZdO30xdbS00Wi10Oh0yjn+LF55+DJ99dawgrLvP5c6uhWaddhVRmAcKBNJGhRfP44nlvwK32eDlpceadX/FlfLaPoF+XqXeOq1LDwR2NAoFABAFLwAvKV0G6boGDByMXR9/7rDMxrmmyFTTe0BIt3xlqmobOtAoWwIaY1EVOHinzJfYWcqqzSHVdZZOm0zYZrMxAC3OZnUzFAryXA1rlC6DyH4sNcNSVeY2wcABFJpqOmWELpvNxq5cuSIAyGrPeqj7APweQLjSRRDZa99cw28ADAgsBnOT+XQuAYElBZo+XlpW28GbsgHIslgsS9qzEs8OBVEIBrBa6TLIT8pqbXjhc+cuROpizuSvnX670kU4w9O7D08DEFq8FyHt97OI5NRpShfhDM8NBVHoC2Cl0mUQj/JiRHKq6vtEnhsKwO8AdNpRYUIAxAO4W+kiWuKZoSAKPqDxFokyVihdQEs8MxSA+yBP/ElIZ5sWkZyq6jlDPDUUVJ/WxG1pACxTuoib8bxQEIUEAKOULoN4tIciklNdPmKSq3heKFArgSgvFMA8pYtojmeFgigEAligdBmEQMUfTp4VCkASAN8W70VIxxsXkZw6TOkimuJpoXCv0gUQ0oAquxCeEwqiEApgjNJlENLALKULaIrnhAIwA571fIn6DVPjOQue9CZRZSoTj6e6/dIzQkE+rXmy0mUQ0gQKBYXcCaBbi/cipPPdHpGc2l3pIhrylFBQXRoTYucFYKrSRTTkKaEwQ+kCCLmJmUoX0JD7h4IoDAbQW+kyCLmJCUoX0JD7hwKQoHQBhLSgf0RyaqjSRdTzhFC4RekCCHGCaj68PCEUVPNiE3ITqtlPPSEURipdACFOoFDoFPJBxkClyyDECRQKnUQ1LzQhLVDNwUZ3DwU6yEi6ElV8iLl7KMQoXQAhraCK/dXdQ4FOWiJdiSr2VwoFQtRDFfur+4aCKOggj5pLSFfRS+kCAHcOBSAcgOon8ySkAWopdDBVpC4hraCKfdadQ0EVqUtIK/hHJKcGKF2EO4eCKlKXkFZSfL9151AIV7oAQtpA/aHAGLMyxtIZY1mMsd2MMb/WbIAx1psx9p7938MZY9Ma3DaLMZbc+rKdQmMykq6oVe+vjuBMS6Gacz6ccx4LoA6tnEabc36Rc55o/3M4gGkNbtvLOV/bmvW1glcHrZeQjqT4ftva7sMXAIYwxoIZYx8yxjIZY18zxoYBAGPsdnurIp0xdpIxFsAYi7C3MvQAngNwn/32+xhjv2SM/S9jTGCM5TPGNPb1+DHGChhjXoyxwYyxjxljxxljXzDGopysVdfK50aIGii+3zodCowxHeRRZyUAzwI4yTkfBuBpAG/b7/Y4gJWc8+GQx52rrn8857wOwBoAO+0tj50NbjMByABwu33RTAAHOOdmAJsB/IZznmBf/0YnS1b8xSWkDRTfb50pwJcxlm7/9xcA3gTwDYC5AMA5P8QYC2GMCQCOAFjPGNsB4F+c8/OMOX3+0E4A9wE4DGA+gI2MMX8A4wDsbrAeb2dXSDpGWv8jdf7e35YoXYdbsultwHRFS3AmFKrtn/zXsabf6ZxzvpYxlgr5uMHXjLFJAGqcrGUvgJcYY8GQLyE9BPlgYWnj7TvJ0obHECfUMa5nDMFK1+GWtHU2pUto61eSnwNYBACMsZ8DKOaclzHGBnPOJc75OgBpABr3/8sBNHlyBue8AsC3AP4KYB/n3Mo5LwPwA2Nsnn1bjDEW72SNFAqkK1J8v21rKIgAbmGMZQJYCyDJvvz39oOKGZCPJ/y70eMOAzDWH2hsYr07Adxv/11vEYCH7OvMBvALJ2tU/MUlpA0U329b7D5wzv2bWFaCJt6cnPPfNLGKfACxDR53a6PbtzZ4/HtodBET5/wHAHe3VGcTqlu+CyGq42x3u8O48xmNl5QugJA2KFK6AHcOhUKlCyCkDRTfb905FC4qXQAhrVQjJUnXlC7CnUNB8cQlpJVUsc9SKBCiHqpo3bpvKIimWgB01h3pSlTxQea+oSBTxYtMiJNUsb+6eyioojlGiJNUsb+6eyjkKl0AIa2giv3V3UPhuNIFENIKqthf3T0U0pQugBAnXZaSpAKliwDcPxRyAVQpXQQhTlBFKwFw91AQTVYA6UqXQYgTKBQ6kWpebEJuQjX7KYUCIeqgmv3UE0KBDjYStVPNQUbAM0IhF4DiV54RchNfKV1AQ+4fCvLBxsbDwhGiJh8pXUBD7h8Ksr1KF0BIM2ygUFDEvwGYlS6CkCZ8KyVJl5UuoiHPCAXRVAZ5WHpC1EZVrQTAU0JBRl0Iokaq2y8pFAhRzvdSkpSldBGNeU4oiKZ8yJPjEqIWqus6AJ4UCrL3lS6AkAZUuT96WihsgQqm5SIEQI6UJH2hdBFN8axQEE0XoNImG/E4rytdQHM8KxRkG5UugHi8CgBvK11EczwxFD4BcFrpIohH2yElSWVKF9EczwsF0cQB/E3pMohHU3Vr1fNCQbYVNEwbUcYRKUnKVLqIm/HMUBBNpQDeVboM4pFU3UoAPDUUZK9CvkKNkM5yDsB7ShfREs8NBdGUDWCH0mUQj/JHKUmqU7qIlnhuKMjWAFD9fxJxC9lQ8deQDXl2KMjXQ6j2JBLiVp6WkqQu0V317FCQvQCgXOkiiFs7KiVJXeYqXQoF0XQFQIrSZRC3lqx0Aa1BoSBLAaCqIbGI20hV64VPzaFQAADRVAHgeaXLIG7HCuBppYtoLQqFn7wO4BuliyBuZb3az15sCoVCPXl+iF8BqFW6FOIWciF/5d3lUCg0JJpOoYv+RxJVsQL4pZQk1ShdSFtQKNwoBdSNIO2zXkqSuuw+RKHQGHUjSPt02W5DPQqFplA3grRNl+421KNQaF4KgK+VLoJ0KSldudtQj0KhOXI34j7QSU3EOZ8B+IPSRbgChcLNiKZzAOaArqQkN5cPIFFKktxiEmMKhZaIpiMAVihdBlGtCgCzpCSpWOlCXIVCwRmi6U0AryldBlEdDmCxlCS51XSEFArOWwV5eHhC6j0rJUkfKF2Eq1EoOEs0WQDcC+A7pUshqvAegOeULqIjUCi0hmgqATALQInSpRBFpUE+H4ErXUhHoFBoLdGUA2AKAJPSpRBFZACYIiVJlUoX0lEoFNpCNKUBmAr5yDPxHDkAJktJklu3FCkU2ko0fQVgBgC3/cQgDs4AmCQlSVeULqSjUSi0h2j6DMDdAFQ7WShxiWwAt0tJUqHShXQGCoX2Ek1fApgM4JrSpZAOkQ7g51KSVKR0IZ2FQsEVRNO3ACYC8Jgdx0McBTDRmbMVGWOcMZbS4O/HGWOiqwtijD3d6O+jrt4GhYKriKZ0ALdA/rqKdH1/hxwIzrYAawHMYYz16MCagEYDwXLOx7l6AxQKriSaLgD4GWhG667MCmCVlCQ9KCVJrRloxwJgM4BHG9/AGAtljL3PGDtm/7mtwfL/MMZOMMY2McZ+rA8VxtiHjLHjjLFsxtgj9mVrAfgyxtIZYzvsyyrsv3cyxqY12OZWxthcxpiWMfayfbuZjLGlLT0RCgVXE03VEE0LATwFmtW6q7kGYJqUJL3axsf/H4BFjDGh0fK/AniVc34rgLkAttiX/xHAIc75SAAfAOjf4DEPcs4TILc+f8sYC+GcJwOo5pwP55wvarSNf0K+1B+MMT2AOwHsB/AQAJN927cCeJgxNvBmT4JCoaOIprUAfgGakq6ryAUwWkqSDrZ1BZzzMsiTyP620U2TAPwvYywdwF4A3RljAQDGQ34zg3P+MRwPVv+WMZYBeaCffgAiW9j8vwFMZIx5Qz6H5nPOeTWAuwAstm/7GwAhLa1L18KGSHuIpn0QhTEA9gAYonQ5pFn7ASyQkiRXfLX8FwAnIB+TqKcBMNb+Jr2OMcaaWgFj7OeQg2Qs57yKMfYpAJ+bbZRzXmO/3xTILYb6LiwD8BvO+QFnnwC1FDqafFp0AoA3lS6F3KAa8tWvM10UCOCclwDYBbnZXu8ggF/X/8EYG27/55eQL7IDY+wuAEH25QKAa/ZAiAIwpsG6zIwxr2Y2/0/Igw5PAFAfAgcALK9/DGPMwBjrdrPnQKHQGURTGUTTEsjNuvNKl0MAAEcAxEtJ0qsdMEV8CoCG30L8FsAt9gN9OQCW2Zc/C+AuxtgJyPtGIeTu5scAdIyxTMjTGTYcK3QzgMz6A42NHIR8oPu/nPP60cK2QD49+wRjLAvAJrTQQ2Ccu+WFXuolCgKA9QAeVLqUtprbO/zIGW/9bUrX0UbVAJ4B8NcOCINWsff/rZxzC2NsLIDXOefDlawJoGMKnU80mQA8BFHYDeANAH0VrsiTHAHwKylJylO6ELv+AHYxxjSQxwF9WOF6AFD3QTmi6WMAMZCbd/TVZceqgHzs4GcqCgRwzvM45yM45/Gc81s558eUrgmg7oM6iMIwAC8BmNbSXdWgC3Uf6gD8DcCfPOHqRleh7oMaiKZMANMhChMArAXg8lNXPYwNwA4Aa6QkKV/hWrocCgU1EU1fALgNojALwIuQuxekdVIBPOVuIyx3JjqmoEaiaS+AYQB+CRoo1lmfA5ggJUkzKBDah44pqJ0oMMgDuayAfMxB8SBX0TGFCsjdhI1SkpSpdDHugroPaieaOOTz2v8NURgA+cSXhwCEKlqXsnIAvA7gbVediUh+Qi2FrkgU9AASIbceOv0TW6GWghnAh5BbBZ928rY9CoVCVycKAyHPRTEL8imuHd7668RQKIN8yu9HAPa7+yjKakGh4E5EIRDyOfSz7L8bX9fvEh0cCj9CDoG9AD51l5mcuxIKBXclCl6Qr5abDPkqzQQAwa5YtYtD4RyA4wC+BfBvKUnKcNF6SRvRgUZ3JZrMAA7Zf+zLhIH4KSBcGhROqg+ANPvv4+40hbu7oFDwJKLpBwA/QJ4c1b5M6A95ZJ9eAHo38zsQN/8q1AKgGMBFyJf/Nv5dCOAHCoCugboPxDny+RJeAHTJoSFI9e/GIYeBxV0nWvVUFAqEEAeKnx1HCFEXCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIAwoFQogDCgVCiAMKBUKIg/8HgpDCjlggM7QAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q1 = data_store[data_store['question'] == 'Are you a student?']\n",
    "plt.figure(0)\n",
    "plt.pie(q1['user_answer'].value_counts(), labels=list(q1['user_answer'].value_counts().keys()))\n",
    "plt.legend(title = \"Are you a student?\")\n",
    "\n",
    "q2 = data_store[data_store['question'] == 'How was your day?']\n",
    "values = q2['user_answer'].values\n",
    "counter = [0, 0, 0]\n",
    "counter_label = [\"Neutral\", \"Positive\", \"Negative\"]\n",
    "for value in values:\n",
    "    index = positive_vs_negative(value)\n",
    "    counter[index] = counter[index] + 1\n",
    "plt.figure(1)\n",
    "print(counter)\n",
    "plt.pie(counter, labels=counter_label)\n",
    "plt.legend(title = \"User's Mood\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Be Creative!\n",
    "Don't limit yourself to a simple Q&A. Feel free to explore things like the sentiment analysis that we did in Lab 1 by determining whether a user's input is positive or negative (remember the positive and negative word lists)."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  },
  "vscode": {
   "interpreter": {
    "hash": "72c89bfd059e2267712ada51c88c396e1070a0d0c685545f7a398da337d403d6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
