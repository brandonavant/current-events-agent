from agent import ThoughtAndActionModel
from agent.common import logger
from agent.processing import process_user_inquiry, invoke_action


def main():
    """
    The main function, which is the entry point of the program.
    """
    quit_indicator: str = 'q'

    try:
        user_inquiry: str = ""

        while user_inquiry != quit_indicator:
            user_inquiry: str = input("What would you like me to do? ('q' to quit)\n")

            if user_inquiry == quit_indicator:
                break

            thought_and_action: ThoughtAndActionModel = process_user_inquiry(user_inquiry)
            final_response: str = invoke_action(user_inquiry, thought_and_action)

            print(f'{final_response}\n')

        print("Have a nice day!")
    except Exception as e:
        logger.error("Unable to fulfill user inquiry.", exc_info=e)


if __name__ == "__main__":
    main()
