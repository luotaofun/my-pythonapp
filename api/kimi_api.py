from openai import OpenAI

client = OpenAI(
    api_key="sk-X1tNQT7A0zxuc6UkJwHp3kBoi0vYk0HHWLIJhQ1P7tcdJ1Rr",
    base_url="https://api.moonshot.cn/v1",
)

history = [
    {"role": "system",
     "content": "你是一名资深python爬虫工程师，擅长网络爬虫。"}
]


def chat(query, history):
    history.append({
        "role": "user",
        "content": query
    })
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
        temperature=0.3,
    )
    result = completion.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": result
    })
    return result


print(chat(input("Enter a prompt:"), history))