import replicate
from dotenv import load_dotenv
load_dotenv()

'''
Дополнительно необходимо в терминале прописать:
    1) pip install replicate
    2) pip install python-dotenv
Далее создать файл в этом же каталоге .env и в него поместить следующее:
REPLICATE_API_TOKEN=r8_CHD********************************** (ваш API, созданный на сайте https://replicate.com/)
'''



output = replicate.run(
    "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
    input={
        "width": 768,
        "height": 768,
        "prompt": "Lexus IS 250 on the seashore under the rays of the setting sun, hd",
        "scheduler": "K_EULER",
        "num_outputs": 1,
        "guidance_scale": 7.5,
        "num_inference_steps": 50
    }
)
print(output)

