"""
cre | Malte Herrmann | 2024

----

This tool is a helper to generate regular expression patterns
using the help of an LLM.
"""

import os
from openai import OpenAI


# This prompt provides some context to the LLM for the
# desired regular expression derivation.
CONTEXT_PROMPT = """
You are an AI assistant, that can be used to generate
regular expression patterns, based on a given input.

If not specified otherwise, these patterns should be not case-sensitive,
and should generalize whitespace and other special characters.

Numbers should also be generalized and not be treated as literals.

Remember, that the purpose of your interactions is to generate
regex patterns, so the only required output is the generated pattern itself.
"""

INPUT_PROMPT = """cre | 2024

This helper builds regular expressions based on any text provided.
The resulting pattern will be generated with generalized whitespace,
special characters and numbers.
Additionally, the resulting pattern will be case-insensitive.

Please provide the input material to match:
"""


def run():
    """
    The main method to run the tool.
    """
    user_prompt = input(INPUT_PROMPT)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key or "sk-" not in api_key[:3]:
        print("OpenAI API key not found")
        return

    client = OpenAI(
        api_key=api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": CONTEXT_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model="gpt-4o-mini",
    )

    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    run()
