# Here the JSON module is imported into Python.
import json
# Here the get_close_matches funtion is imported from the difflib module into Python. 
from difflib import get_close_matches

# This is the function 'load_knowledge_base' which loads the JSON file 'knowledge_base.json' which contains all the chat bots knowledge on questions and answers.
def load_knowledge_base(file_path: str):
    # Here the file path is opened in read mode (r) as a file.
    with open(file_path, 'r') as file:
        # Here the file is loaded and stored as the data type dictionary.
        data: dict = json.load(file)
    # Here the loaded data is returned.
    return data

# This is the function 'save_knowledge_base' which saves any information the chat bot has been taught by the user into the JSON file 'knowledge_base.json'. 
# This updates the file to contains all the new knowledge the chat bot has learned along with any previous knowledge.
def save_knowledge_base(file_path: str, data: dict):
    # Here the file path is opened in write mode (w) as a file.
    with open(file_path, 'w') as file:
        # Here 'json.dump' is used to insert any additonal data into the 'knowledge_base.json' file indented twice.  
        json.dump(data, file, indent=2)

# This is the function 'find_best_match' which searches the knowledge base stored as the data type dictionary for the question that best matches the user input.
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    # Here the imported function 'get_close_matches' is used to match the users question with the questions stored in the data type dictionary. 
    # 'n' is used to limit the result to only 1 and cutoff is used to dermine the accuracy of the matching algorithm.
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.9)
    # Here the matches starting at index zero are returned, if there are no matches return nothing. 
    return matches[0] if matches else None

# This is the function 'get_answer_for_question' which returns the answer to the users question stored in the knowledge base.
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    # Here a 'for' loop loops through all the questions stored in the knowledge base.
    for q in knowledge_base["questions"]:
        # This is an 'if' statement where if the value of 'question' stored in the data dictionary q is equal to the value of the variable question execute the code within the if statement code block.
        if q["question"] == question:
            # This returns the value of the 'answer' tored in the data dictionary q.
            return q["answer"]
    # This returns nothing.
    return None

# This is the main function 'chatbot' which handles the users input and generates a response based on matching values stored in the knowledge base.
def chatbot():
    # Here the data type dictionary variable 'knowledge_base' is declared and set to equal the function 'load_knowledge_base' which is then passed the directory path to the file 'knowledge_base.json'
    knowledge_base: dict = load_knowledge_base('E:/BSc Computing/Year 2/Semester 2/Emerging Technologies/Assignment 2/Chat Bot/knowledge_base.json')
    # This is the start of an infinite loop.
    while True:
        # Here the string variable 'user_input' is declared and set to equal the value of the users actual input.
        user_input: str = input("You: ")
        # Here the string stored in the variable 'user_input' is transformed into all lower case and has all sepcial characters removed excluding spaces.
        user_input = ''.join([char.lower() for char in user_input if char.isalpha() or char.isspace()])
        # Here the user input is transformed into all lower case, then using an 'if' statement if the user input matches the string value 'exit' execute the code within the if statement code block.
        if user_input.lower() == 'exit':
            # Here the 'break' statement is used to exit out of the infinite loop stopping the chat bot script from running. 
            break

        # Here the string variable 'best_match' is declared and set to equal the result of the function 'find_best_match', otherwise return nothing.
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        # Here an 'if' statement uses the variable 'best_match' as a condition
        if best_match:
            # Here if there is a value stored in the string variable 'best_match' the string variable 'answer' is declared and set to equal the result of the function 'get_answer_for_question' which returns that answer from the knowledge base.
            answer: str = get_answer_for_question(best_match, knowledge_base)
            # Here the value of the string variable 'answer' in printed along with the string 'Animus: '.
            print(f"Animus: {answer}")
        else:
            # Here if there is not a value stored in the string variable 'best_match' the string 'Animus: Hmmm I don't know the answer. Can you teach me it?' is printed.
            print("Animus: Hmmm I don't know the answer. Can you teach me it?")
            # Here the string 'Type the answer or type 'skip' to skip: ' is printed and the string variable 'new_answer' is declared and set to equal the value of the users response.
            new_answer: str = input("Type the answer or type 'skip' to skip: ")
            # Here an 'if' statement is used where if the users input after being transformed into lower case does not equal 'skip' execute the code within the if statement code block.
            if new_answer.lower() != 'skip':
                # Here using '.append' the users question (that the bot didn't know the answer to) and the answer to the question the user provided are added to the knowledge base dictionary list.
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                # Here the 'save_knowledge_base' function is called and passed the directory path to the file 'knowledge_base.json' saving the the question the bot didn't know the answer to along with the answer, effectively teaching the chat bot.
                save_knowledge_base('E:/BSc Computing/Year 2/Semester 2/Emerging Technologies/Assignment 2/Chat Bot/knowledge_base.json', knowledge_base)
                # Here the string 'Animus: Thank you! I've learned something new.' is printed.
                print("Animus: Thank you! I've learned something new.")

#if __name__ == "__main__":
chatbot()