import random

class NakliLLM:

  def __init__(self):
    print('LLM created')

  def predict(self, prompt):

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}
  
llm = NakliLLM()
llm.predict('What is the capital of India?')


class NakliPromptTemplate:

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def format(self, input_dict):
    return self.template.format(**input_dict)
  
template = NakliPromptTemplate(
  template='Write a poem about {topic}',
  input_variables=['topic']
)

prompt = template.format({'topic':'india'})

print(llm.predict(prompt))



class NakliLLMChain:
  

  def __init__(self, llm, prompt):
    self.llm = llm
    self.prompt = prompt

  def run(self, input_dict):

    final_prompt = self.prompt.format(input_dict)
    result = self.llm.predict(final_prompt)

    return result['response']
  

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)
chain = NakliLLMChain(llm, template)
chain.run({'length':'short', 'topic': 'india'})
