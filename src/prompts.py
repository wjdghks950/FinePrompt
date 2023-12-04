# TODO: Assign each prompt into BASE_PROMP_DICT

BASE_PROMPT_DICT = {}

base_self_ask_prompt = '''
You are a question answering assistant.
1) You will be given a question ("Question:"). 
2) Figure out if any follow up question is needed ("Are follow up questions needed here:") with "Yes" or "No" answer.
3) For each follow up question, give the corresponding "Intermediate answer:". 
4) When you generate the final answer, generate the answer after "So the final answer is:".

Question: ...
Are follow up questions needed here: ...
Follow up: ...
Intermediate answer: ...
So the final answer is: ...
'''

base_cot_prompt = '''
You are a question answering assistant.
1) You will be given a question ("Question:"). 
2) Generate an explanation for your answer after "Answer:".
4) When you generate the final answer, generate the answer after "So the final answer is:".

Question: ...
Answer: ...
So the final answer is: ...
'''

base_drop_prompt = '''
You are a question answering machine that answers a question based on a given document. \
You will be given a document preceded by "Document:" and a question preceded by "Question:". \
When you generate the answer, simply generate the answer after "Answer:"

Document: ...
Question: ...
Answer: ...
'''

base_musique_prompt = '''
You are a question answering assistant. You will be given a set of evidence paragraphs, a multi-hop question and you will be asked to do the following:

1) You will read a list of paragraphs (P1, P2, ..., PN) and a multi-hop question ("Question:").
2) You should give the paragraph id you used to derive the answer after "Evidence:".
3) You should provide the answer to the multi-hop question after "Answer:".
 
Paragraphs: ... 
P1: ... 
P2: ... 
... 
PN: ... 
Question: ... 
Evidence: Pi, Pj, ... 
Answer: ...
'''

genbert_prompt_base = '''
You are a question answering machine that answers a question based on a given document. \
You will be given a document preceded by "Document:" and a question preceded by "Question:". \
When you generate the answer, simply generate the answer after "Answer:". \
You will also be given a set of related task examples to help you acquire the necessary knowledge to answer a given question based on the document.

Document: ...
Question: ...
Answer: ...

Related Examples:
1) 19517.4 - 17484 - 10071.75 + 1013.21 = -7025.14
2) most(1072.1, 17938, 5708.65, 14739.16) = 17938
3) argmax(toppy 8105.5, cockney 7111.0, nickelic 1463.16, tiredom 6929) = toppy
4) most recent(July 16, 134; June 23, 134; 24 July 134; 28 October 134) = 28 October 134
5) difference in days(April 21, 1381; 13 April 1381) = 7
6) percent not photochemist, floodgate, retiringly :: photochemist 0.82%, morningward 54.4%, floodgate 2.0%, reline 0.78%, retiringly 42% = 55.18
7) Document: "The commander recruited 16426 asian citizens and 15986 asian voters. The commander borrowed 7 foreign groups from the government. The government passed 3 foreign groups to the commander."
Question: How many foreign groups did the commander recruit? 
Answer: 10
'''

numnet_prompt_base = '''
You are a question answering machine that answers a question based on a given document. \
You will be given a document preceded by "Document:" and a question preceded by "Question:". \ 
When you generate the answer, simply generate the answer after "Answer:"

Numbers have specific relationships as shown in the following examples, \
where the "<" symbol represents "a < b" (a is less than b), \
the ">" symbol represents "a > b" (a is greater than b), and the "=" symbol represents "a = b" (a is equal to b).

Document: ...
Question: ...
Answer: ...

5 < 6
10 > 6
117 > 25
978 < 979
0 = 0
1.6 < 7.2
9.0 > 8.9
2.6 < 2.9
'''

qdgat_prompt_base = '''
You are a question answering machine that answers a question based on a given document. \
You will be given a document preceded by "Document:" and a question preceded by "Question:". \
When you generate the answer, simply generate the answer after "Answer:". \

Some entities and numbers in the provided document can have special connections. There are a total of two connection types.
1) "ENTITY-NUMBER": Connections between entity and number in the same sentence.
2) "NUMBER-NUMBER": Connections between numbers of the same type. A NUMBER-NUMBER connection is represented by specifying the corresponding number type.
 
Document: ... ENTITY1 (ENTITY-NUMBER: NUMBER1) ... NUMBER1 (ENTITY-NUMBER: ENTITY1) ... NUMBER2 (ENTITY-NUMBER: ENTITY2, ENTITY3 | NUMBER-NUMBER: YARD)
Question: ...
Answer: ...
'''

decomprc_prompt_base = '''
You are a question answering assistant. You will be given a set of evidence paragraphs, a multi-hop question and you will be asked to do the following:

First, decompose the given multi-hop question ("Question:") into all three different versions of single-hop, sub-question sets ("Sub-question 1:", "Sub-question 2:"). The three different question types are as follows:

1) Bridging Type: requires finding the first-hop evidence for Sub-question 1 to find the evidence to answer Sub-question 2.
2) Intersection Type: requires finding an entity that satifies two independent conditions of the two Sub-questions.
3) Comparison Type: requires comparing the property of two different entities in the Sub-questions.

Then, given a question, generate the sub-questions, the corresponding answer and the evidence paragraph ids for each sub-question in the following format:

Paragraphs:
P1: ...
P2: ...
...
PN: ...

Question: ...

[Bridging]
Sub-question 1: ... | Sub-question 1 Answer: ... | Evidence: Pi, Pj, ...
Sub-question 2: ... | Sub-question 2 Answer: ... | Evidence: Pi, Pj, ...

[Intersection]
Sub-question 1: ... | Sub-question 1 Answer: ... | Evidence: Pi, Pj, ...
Sub-question 2: ... | Sub-question 2 Answer: ... | Evidence: Pi, Pj, ...

[Comparison]
Sub-question 1: ... | Sub-question 1 Answer: ... | Evidence: Pi, Pj, ...
Sub-question 2: ... | Sub-question 2 Answer: ... | Evidence: Pi, Pj, ...

Using the previously generated information about the sub-questions, the answers and evidence paragraphs, generate the \
most plausible answer to the question ("Question:") after "Answer:", and also generate which question type your answer is from as follows:

Question Type: ...
Answer: ...
'''

quark_prompt_base = '''
You are a question answering assistant. You will be given a set of evidence paragraphs, a multi-hop question and you will be asked to do the following:

1) You will read a list of paragraphs (P1, P2, ..., PN) and a multi-hop question ("Question:").
2) Find one question-related sentence for each paragraph ("Paragraph:") and write that sentence id after "Evidence Sentences:". 
3) Read the given set of sentences after "Evidence Sentences for Pi:", where "i" refers to the paragraph id.
This set of predicted sentences will serve as your new context to help you answer the question.
4) You should provide the answer to the multi-hop question after "Answer:".

Paragraphs: ...
P1: ...
P2: ...
...
PN: ...

Question: ...

Evidence Sentences for P1: Si
Evidence Sentences for P2: Sj
...
Evidence Sentences for PN: Sk

Answer: ...
Evidence Paragraphs: Pi, Pj, ...
'''

sae_prompt_base = '''
You are a question answering assistant. You will be given a set of evidence paragraphs, a multi-hop question and you will be asked to do the following:

1) You will read a list of paragraphs (P1, P2, ..., PN) and a multi-hop question ("Question:").
2) You should provide the answer to the multi-hop question after "Answer:".
3) You should give the paragraph id you used to derive the answer after "Evidence:".

The provided paragraphs and sentences within are prefixed with paragraph numbers and sentence numbers. For example, the prefix "P2S1" indicates the 1st sentence of the 2nd paragraph.
Also, if sentences are related to other sentences, prefixes can connect them to each other in some form of connection.
There are a total of three connection types:
1) "Question": Connections between sentences that are related to the question. 
2) "Intra": Connections between sentences within the same paragraph. 
3) "Inter": Connections between sentences that are related but belong to different paragraphs.

Paragraphs:
P1S1 (Inter: P2S2 | Intra: P1S2): ...
P1S2 (Intra: P1S2): ...
P2S1 (Intra: P2S2): ... P2S2 (Question: Q, P3S2 | Inter: P1S1 | Intra: P2S1): ...
P3S1 (Intra: P3S2): ... P3S2 (Question: P2S2 | Intra: P3S1): ...
...
PNS1 (Question: Q | Intra: PNS2): ...
PNS2 (Intra: PNS1): ...
Q (Question: P1S1, PNS1): ...
Answer: ...
Evidence: P1, P3, ...
'''

BASE_PROMPT_DICT['base_drop_prompt'] = base_drop_prompt
BASE_PROMPT_DICT['base_musique_prompt'] = base_musique_prompt
BASE_PROMPT_DICT['base_self_ask_prompt'] = base_self_ask_prompt
BASE_PROMPT_DICT['base_cot_prompt'] = base_cot_prompt
BASE_PROMPT_DICT['genbert_prompt_base'] = genbert_prompt_base
BASE_PROMPT_DICT['numnet_prompt_base'] = numnet_prompt_base
BASE_PROMPT_DICT['qdgat_prompt_base'] = qdgat_prompt_base
BASE_PROMPT_DICT['decomprc_prompt_base'] = decomprc_prompt_base
BASE_PROMPT_DICT['quark_prompt_base'] = quark_prompt_base
BASE_PROMPT_DICT['sae_prompt_base'] = sae_prompt_base

# TODO: Refactor the in-context example generation codes into this file
