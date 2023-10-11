from langchain.llms import OpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

chat = OpenAI(temperature=0)

conversation = ConversationChain(
    llm=chat,
    verbose=True,
    memory=ConversationBufferWindowMemory()
)