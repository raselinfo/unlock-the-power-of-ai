from langchain.llms import OpenAI
import os
os.environ['OPENAI_API_KEY']='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'
llm = OpenAI(temperature=0.9,stop=["rasel"])

# print(llm("hello how are you?"))
# def generate_serially():
#     for _ in range(10):
#         res=llm.generate(["Hello, how are you?"])
#         print(res.generations)
# generate_serially()

print(llm("Hello, how are you?"))