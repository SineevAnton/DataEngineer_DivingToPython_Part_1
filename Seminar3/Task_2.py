# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

from collections import Counter

# Текст английской статьи из википедии про Искуственный Интеллект
# С русским текстом проблемы с кодировками
# Сразу преобразуем в нижний регистр
text = """
Planning and decision making
An "agent" is anything that perceives and takes actions in the world. A rational agent has goals or preferences and takes actions to make them happen.[d][30] In automated planning, the agent has a specific goal.[31] In automated decision making, the agent has preferences – there are some situations it would prefer to be in, and some situations it is trying to avoid. The decision making agent assigns a number to each situation (called the "utility") that measures how much the agent prefers it. For each possible action, it can calculate the "expected utility": the utility of all possible outcomes of the action, weighted by the probability that the outcome will occur. It can then choose the action with the maximum expected utility.[32]

In classical planning, the agent knows exactly what the effect of any action will be.[33] In most real-world problems, however, the agent may not be certain about the situation they are in (it is "unknown" or "unobservable") and it may not know for certain what will happen after each possible action (it is not "deterministic"). It must choose an action by making a probabilistic guess and then reassess the situation to see if the action worked.[34] In some problems, the agent's preferences may be uncertain, especially if there are other agents or humans involved. These can be learned (e.g., with inverse reinforcement learning) or the agent can seek information to improve its preferences.[35] Information value theory can be used to weigh the value of exploratory or experimental actions.[36] The space of possible future actions and situations is typically intractably large, so the agents must take actions and evaluate situations while being uncertain what the final outcome will be.

A Markov decision process has a transition model that describes the probability that a particular action will change the state in a particular way, and a reward function that supplies the utility of each state and the cost of each action. A policy associates a decision with each possible state. The policy could be calculated (e.g. by iteration), be heuristic, or it can be learned.[37]

Game theory describes rational behavior of multiple interacting agents, and is used in AI programs that make decisions that involve other agents.[38]

Learning
Machine learning is the study of programs that can improve their performance on a given task automatically.[39] It has been a part of AI from the beginning.[e]

There are several kinds of machine learning. Unsupervised learning analyzes a stream of data and finds patterns and makes predictions without any other guidance.[42] Supervised learning requires a human to label the input data first, and comes in two main varieties: classification (where the program must learn to predict what category the input belongs in) and regression (where the program must deduce a numeric function based on numeric input).[43] In reinforcement learning the agent is rewarded for good responses and punished for bad ones. The agent learns to choose responses that are classified as "good".[44] Transfer learning is when the knowledge gained from one problem is applied to a new problem.[45] Deep learning uses artificial neural networks for all of these types of learning.

Computational learning theory can assess learners by computational complexity, by sample complexity (how much data is required), or by other notions of optimization.[46]

Natural language processing
Natural language processing (NLP)[47] allows programs to read, write and communicate in human languages such as English. Specific problems include speech recognition, speech synthesis, machine translation, information extraction, information retrieval and question answering.[48]

Early work, based on Noam Chomsky's generative grammar and semantic networks, had difficulty with word-sense disambiguation[f] unless restricted to small domains called "micro-worlds" (due to the common sense knowledge problem[26]).

Modern deep learning techniques for NLP include word embedding (how often one word appears near another),[49] transformers (which finds patterns in text),[50] and others.[51] In 2019, generative pre-trained transformer (or "GPT") language models began to generate coherent text,[52][53] and by 2023 these models were able to get human-level scores on the bar exam, SAT, GRE, and many other real-world applications.[54]
""".lower()

# Избавляемся от символов пунктуации и цифр
puncuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
for element in text:
    if element in puncuations:
        text = text.replace(element, "")

# Разбили текст по пробелам в список, посчитали вхождения каждого слова, вывели 10 наиболее частых с
text_list = text.split()
result = Counter(text_list)
print(*result.most_common(10))


# ___________________________________
# Дальше можно не смотреть, я оставил это себе для дальнейших тестов, так как пока красоты не получилось(
# Идея в том, чтобы не копировать текст с сайта, а получить html-код страницы, убрать оттуда все лишнее
# и с этим уже работать
# ___________________________________

# import requests
# import re
# import string

# CLEANER = re.compile('<.*?>') # Шаблон для html-тегов, чтобы далее убрать их из текста
#
#
# def mr_propper(raw_html):
#     """
#     Функция для избавления html-строки от html-тегов
#     :param raw_html: Строка для чистки
#     :return: Очещенная строка
#     """
#     cleantext = re.sub(CLEANER, ' ', raw_html)
#     return cleantext
#
#
# url = "https://ru.wikipedia.org/wiki/Искусственный_интеллект"
# r = requests.get(url)
# print(r.headers['content-type'])
# if (r.headers['content-type'].lower() == 'text/html; charset=utf-8'):
#     html = r.text
#     print(mr_propper(html))