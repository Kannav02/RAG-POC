# Idea

Load Documents,chunk them ,Index them , embed and store in vector Db, then work on the retrieval part and the agent workflow, this is gonna take a long tim  
Still a work in progress
``

# Guide Reference


## Components

Prompt Templates are responsible for formatting user input into a format that can be passed to a language model.

This can be used to guide a model's response
- Input : Dictionary, where each key represents a variable in the prompt template
- Output : Outputs a PromptValue, this value can be can be passed to a LLM

Basic PromptTemplate- static prompts
ChatPromptTemplate - for user and the system,chat oriented
FewShotTemplate - for examples and concise answers, example based guidance
