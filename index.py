from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
os.environ['OPENAI_API_KEY']=os.getenv("OPEN_AI_API_KEY")
# llm = OpenAI(temperature=0.9,stop=["rasel"])

# # print(llm("hello how are you?"))
# # def generate_serially():
# #     for _ in range(10):
# #         res=llm.generate(["Hello, how are you?"])
# #         print(res.generations)
# # generate_serially()

# print(llm("Hello, how are you?"))

