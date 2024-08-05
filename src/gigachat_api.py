from langchain_community.chat_models import GigaChat
from langchain.schema import HumanMessage, SystemMessage
import json

with open("config.json") as json_file:
    auth_data = json.load(json_file)["auth"]["gigachat"][0]["auth_data"]

with open("config.json") as json_file:
    scope_data = json.load(json_file)["auth"]["gigachat"][1]["scope"]

chat = GigaChat(credentials=auth_data, scope=scope_data, verify_ssl_certs=False)


def get_answer_from_gigachat(context, request) -> str:
    messages = [SystemMessage(content=context), HumanMessage(content=request)]
    answer = chat(messages)
    return answer.content


def resume_check(job_title, resume_text) -> str:
    context = (f"Представь, что ты HR специалист, анализирующий резюме по специальности {job_title}. Если ты видишь "
               f"ошибки,"
               f" то ты указываешь на них. Если ты видишь, как можно сделать резюме лучше, то ты даешь совет по "
               f"улучшению.")
    request = f'Проанализируй следующее резюме и дай советы по его улучшению или укажи на ошибки: "{resume_text}"'
    return get_answer_from_gigachat(context, request)
