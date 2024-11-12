import openai

Prompt = str(input("Ask questions about traveling: "))
base_url = "https://api.aimlapi.com/v1"
api_key = "1f9ed41758e14566a1e1cb806ea84de3"
system_prompt = "You are a travel agent. Be descriptive and helpful."
user_prompt = Prompt

api = openai.OpenAI(api_key=api_key, base_url=base_url)

def main():
    try:
        completion = api.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=256,
        )

        response = completion.choices[0].message.content
        print(response)

    except openai.error.OpenAIError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
