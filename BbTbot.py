import requests
import re


def search(query):
    # Replace API_KEY with your own API key
    # Replace SEARCH_ENGINE_ID with your own search engine ID

    url = "https://www.googleapis.com/customsearch/v1?key=APIKEY&cx=ENGINEID&q=" + query
    response = requests.get(url)
    data = response.json()

    # Check if there are any results
    if "items" in data:
        # Get the first result
        result = data["items"][0]
        # Return the link and snippet of the result
        return result["link"] + "\n\n" + result["snippet"]
    else:
        # No results were found
        return "Sorry, I could not find any results for your query."


def changed():
    print(
        f"Our range of services includes: \n 1. Cybersecurity \n 2. Web development \n 3. Data analytics \n Which service are you interested in?")
    service = input("Enter the number of the service you are interested in: ")
    if service == "1":
        service_name = "cybersecurity"
    elif service == "2":
        service_name = "web development"
    elif service == "3":
        service_name = "data analytics"
    else:
        print("Sorry, that is not a valid option.")
        return
        # Continuously prompt the user for input
    while True:
        user_input = input("Please enter your question about " + service_name + ": ")
        # Use a regular expression to ensure that the user's input includes details of a question
        if not re.search(r"what|why|how|where|when|define|who|if|describe", user_input, re.IGNORECASE):
            print(
                "Please include details of a question in your input, such as 'what', 'why', 'how', 'define', 'where', or 'when'.")
        elif user_input.lower() == "change":
            changed()
        # Quit the chatbot if the user enters "quit"
        elif user_input.lower() == "quit":
            break

            # Search the internet for the user's query and print the result
        result = search(user_input)
        print(result)
        continue


def chatbot():
    user_name = input("Hi, what's your name?: ")
    print(
        f"Hello {user_name}, nice to meet you! We offer a range of services, including: \n 1. Cybersecurity \n 2. Web development \n 3. Data analytics \n Which service are you interested in?")
    service = input("Enter the number of the service you are interested in: ")
    if service == "1":
        service_name = "cybersecurity"
    elif service == "2":
        service_name = "web development"
    elif service == "3":
        service_name = "data analytics"
    else:
        print("Sorry, that is not a valid option.")
        return

    # Continuously prompt the user for input
    while True:

        user_input = input(
            "Please enter your question about " + service_name + " (or enter 'change' to change the service): ")
        # Quit the chatbot if the user enters "quit"
        if user_input.lower() == "change":
            changed()
        if user_input.lower() == "quit":
            break

        # Use a regular expression to ensure that the user's input includes details of a question
        if not re.search(r"what|why|how|where|when|define|who|if|describe", user_input, re.IGNORECASE):
            print(
                "Please include details of a question in your input, such as 'what', 'why', 'how', 'define', 'where', or 'when'.")
            continue

        # Search the internet for the user's query and print the result
        result = search(user_input)
        print(result)


# Start the chatbot
chatbot()