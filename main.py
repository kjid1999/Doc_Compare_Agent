from dotenv import load_dotenv
load_dotenv()

from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent
import tools

model = GeminiModel('gemini-2.0-flash')
agent = Agent(
    model,
    system_prompt='Your task is read two pdf files, compare and analyze them to answer the user. If you need to end the chat, just reply an empty string.',
    tools=[
        tools.list_pdf,
        tools.read_pdf,
        tools.pdf_pages,
        tools.get_pdf_outline
    ]
)

def main():
    history = []
    user_input = 'View the list of pdfs first.'

    while True:
        response = agent.run_sync(
            user_input,
            message_history=history,
        )
        if not response.output: break
        history = response.all_messages()
        print('\nAgent:\n'+response.output)
        # print(response.usage())
        user_input = input('User: ')

if __name__ == '__main__':
    main()
