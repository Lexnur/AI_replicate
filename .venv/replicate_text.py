import replicate
from dotenv import load_dotenv
load_dotenv()


enter_text = input('Введите свой вопрос: ')
iterator = replicate.run(
  "mistralai/mixtral-8x7b-instruct-v0.1",
  input={"prompt": str(enter_text)},
)

with open('ai.txt', mode="w", encoding="utf-8") as file:
    for text in iterator:
        file.write(text)
        # print(text)
