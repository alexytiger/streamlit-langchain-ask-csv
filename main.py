#based on https://www.youtube.com/watch?v=tjeti5vXWOU&t=15s
#
# pip install python-dotenv
# pip install streamlit
# pip install langchain
# pip install openai

#: Sure. LangChain is a framework that allows you to interact with data in a natural language way. It uses OpenAI's LLMs to generate Python code that can be used to query and manipulate data.
#:
#: One of the agents in LangChain is the CSV Agent. This agent can be used to interact with CSV files. You can use it to ask questions about the data in the CSV file, and the agent will generate Python code that can be used to answer your questions.
#:
#: For example, you could ask the CSV Agent "What is the average age of the people in this CSV file?" The agent would then generate Python code that could be used to calculate the average age of the people in the CSV file.
#:
#: The CSV Agent is a powerful tool that can be used to interact with CSV files in a natural language way. It can be used to answer questions about the data in the CSV file, and it can also be used to manipulate the data in the CSV file.
#:
#: Here are some other examples of what you can do with the CSV Agent:
#: Find the rows in a CSV file that match a certain criteria.
#: Calculate the sum, mean, or median of a column in a CSV file.
#: Merge two CSV files together.
#: Split a CSV file into multiple CSV files.
#:
#: The CSV Agent is a versatile tool that can be used to perform a variety of tasks with CSV files. If you need to interact with CSV files in a natural language way, then the CSV Agent is a great option.
#:
#: In the context of programming, natural language programming (NLP) is a way of programming that uses natural language sentences to express the desired behavior of a program. This is in contrast to traditional programming, where programs are written in a formal language such as Python or Java.
#:
#: There are several benefits to using NLP for programming. First, it makes programming more accessible to people who are not familiar with formal languages. Second, it can make programs more concise and easier to understand. Third, it can make programs more flexible and adaptable to change.
#:
#: The CSV Agent in LangChain is an example of an NLP tool that can be used to interact with CSV files in a natural language way. Instead of writing Python code to query or manipulate the data in a CSV file, you can simply ask the CSV Agent questions in natural language, and the agent will generate the Python code for you.
#:
#: For example, you could ask the CSV Agent "What is the average age of the people in this CSV file?" The agent would then generate Python code that could be used to calculate the average age of the people in the CSV file.
#:
#: This is just one example of how NLP can be used to make programming easier and more accessible. As NLP technology continues to develop, we can expect to see even more powerful and versatile NLP tools that can be used to program in a natural language way.
#:
#: Here are some other examples of natural language programming:
#: Using a voice assistant to control a smart home.
#: Asking a chatbot to book a flight.
#: Using a natural language interface to query a database.
#:
#: Natural language programming is still a relatively new field, but it has the potential to revolutionize the way we interact with computers. As the technology continues to develop, we can expect to see even more natural language programming applications in the future.

#: A LangChain agent is a program that uses an LLM to generate Python code that can be used to perform a task. The agent takes a natural language description of the task as input, and it generates Python code as output.

#: The agent works by decomposing the task into a series of smaller steps. For each step, the agent determines the best tool to use to perform the step. The tools that the agent can use include:
#: - Google Search
#: - Python REPL
#: - Math calculator
#: - Weather APIs
#: - CSV parsers
#: - And more

#: Once the agent has determined the best tool to use for each step,
# it generates Python code that uses the tool to perform the step. 
# The agent then combines the Python code for each step into a single Python program.

#: The Python program that the agent generates can then be run to perform the task. 
# The agent will also generate a human-readable explanation of the steps that the program takes to perform the task.

#: Here is an example of how a LangChain agent might work:

#: You ask the agent to "Find the average age of the people in this CSV file."
#: The agent decomposes the task into two steps:
#: - Find the rows in the CSV file that contain people's ages.
#: - Calculate the average age of the people in the rows.

#: The agent determines that the best tool to use for the first step is a CSV parser.
#: The agent determines that the best tool to use for the second step is a math calculator.

#: The agent generates Python code that uses the CSV parser to find the rows in the CSV file that contain people's ages.
#: The agent generates Python code that uses the math calculator to calculate the average age of the people in the rows.

#: The agent combines the Python code for each step into a single Python program.

#: The Python program is run, and it prints the average age of the people in the CSV file.


# https://python.langchain.com/docs/modules/agents/toolkits/csv

#: The OpenAI model from LangChain is a large language model (LLM) that is trained on a massive 
# dataset of text and code. This model can be used to generate Python code, answer questions, and perform a variety of other tasks.

#: To use the OpenAI model from LangChain, you will need to create a LangChain account 
# and obtain an API key. Once you have an API key, you can use it to interact with the OpenAI model.

#: Here is an example of how you can use the OpenAI model to generate Python code:

#: Python
#: ```python
#: import langchain
#:
#: # Create a LangChain client
#: client = langchain.Client(api_key="YOUR_API_KEY")
#:
#: # Create a prompt
#: prompt = "Write a Python function that calculates the factorial of a number."
#:
#: # Generate Python code
#: code = client.generate(prompt, model="OpenAI")
#:
#: # Print the Python code
#: print(code)
#: ```

#: Use code with caution. Learn more

#: This code will generate a Python function that calculates the factorial of a number. The function will be stored in the variable code.

#: You can also use the OpenAI model to answer questions. For example, you could ask the model "What is the capital of France?" 
# The model will then generate a response that includes the answer to the question.

#: The OpenAI model is a powerful tool that can be used to perform a variety of tasks. 
# If you are looking for a way to generate Python code, answer questions, 
# or perform other tasks, the OpenAI model from LangChain is a great option.

#: Here are some of the benefits of using the OpenAI model from LangChain:
#: - It is a powerful LLM that can be used to perform a variety of tasks.
#: - It is easy to use. You can interact with the model using a simple API.
#: - It is affordable. You only need to pay for the API calls that you make.


# based on https://python.langchain.com/docs/modules/agents/toolkits/csv
#: In the expression agent = create_csv_agent(OpenAI(temperature=0, model="gpt-4"), csv_file, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS,), the value of temperature is 0. This means that the OpenAI model will be used to generate Python code that is very deterministic and focused.

#: The temperature parameter controls the "creativity" or randomness of the text generated by the OpenAI model. A higher temperature (e.g., 0.7) results in more diverse and creative output, while a lower temperature (e.g., 0.2) makes the output more deterministic and focused.

#: In this case, we want the OpenAI model to generate Python code that is very specific and focused on the task of interacting with the CSV file. Therefore, we set the temperature parameter to 0. This will ensure that the model generates code that is very deterministic and focused on the task at hand.

#: If we were to set the temperature parameter to a higher value, the model would be more likely to generate code that is more creative and diverse. However, this could also result in code that is not as focused on the task at hand.

#: The temperature parameter is a powerful tool that can be used to control the output of the OpenAI model. By adjusting the value of the temperature parameter, you can fine-tune the output of the model to meet your specific needs.

# The choice of agent type depends on the specific task that you want to accomplish. Here are some examples of the different agent types and what they can be used for:

# ZERO_SHOT_REACT_DESCRIPTION : This agent type is used to generate text descriptions of CSV files. 
# This can be useful for tasks such as summarization and visualization. 
# For example, you could use this agent type to generate a text description of the Titanic dataset.

# SQL_AGENT : This agent type is used to execute SQL queries against CSV files. 
# This can be useful for tasks such as data analysis and machine learning. 
# For example, you could use this agent type to answer questions about the Titanic dataset, 
# such as "How many passengers survived?" or "What was the average age of the passengers?"

# PANDAS_AGENT : This agent type is used to interact with CSV files using the Pandas library. 
# This can be useful for tasks such as data manipulation and visualization. 
# For example, you could use this agent type to create a bar chart that shows the distribution of passenger ages on the Titanic.

# NLP_AGENT : This agent type is used to perform natural language processing tasks on CSV files. 
# This can be useful for tasks such as sentiment analysis and topic modeling. For example,
# you could use this agent type to determine the overall sentiment of the Titanic dataset, 
# or to identify the most common topics in the dataset.

# CUSTOM_AGENT : This agent type allows you to create your own agent that can interact 
# with a CSV file in any way that you want. This can be useful for tasks that are not covered 
# by the other agent types. For example, you could create a custom agent that can generate a text 
# description of the Titanic dataset in a specific format, or that can execute a specific SQL query against the dataset.

#
#
#
#
#


from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os
import streamlit as st
from htmlTemplates import css, bot_template
import base64

def get_csv_agent(csv_file):
    
    file_location = f"./{csv_file.name}"

    # Write out the file data
    #n Python, when you open a file with 'wb' mode (write binary), 
    # it opens the file for writing. 
    # If the file already exists, 
    # it gets truncated (i.e., its previous contents get deleted). 
    # Then, the new incoming data will be written to the file.
    with open(file_location, 'wb') as out_file:
        out_file.write(csv_file.getbuffer())
    
    llm = OpenAI(temperature=0)
    agent = create_csv_agent(llm, file_location)
    return agent
    


def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

image_path = 'img/chat-robot.png'  # replace with your actual image path
image_base64 = get_image_base64(image_path)

bot_message = bot_template.replace("{{IMAGE}}", f'data:image/png;base64,{image_base64}')


def main():
    # load our environment to read secrets
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

# This function sets the configuration options of the Streamlit's page.
# Here, page_title="Ask your CSV" changes the default page title from "Streamlit" to "Ask your CSV".
# The browser tab reflects this change.
# It's the first thing that runs when a Streamlit app starts up.
    st.set_page_config(page_title="Ask your CSV", page_icon="🐶")
    st.write(css, unsafe_allow_html=True)

    st.header("Ask your CSV 🐶")
    
    csv_file = st.file_uploader("Upload a CSV file", type="csv")


    if csv_file is not None:

        file_name = csv_file.name
        print('csv_file', file_name)

# important to understand that agent is generating a corresponding python code in memory and running this code by itself
# t get the answer for the question we are asking
# verbose=True is good as it will show in the terminal how our model is thinking       
        
       # Version 2 using ChatOpenAI model
        #llm = ChatOpenAI(temperature=0, model="gpt-4")
        #agent = create_csv_agent(
        #    llm,
        #    file_name,
        #    verbose=True,
        #    agent_type=AgentType.OPENAI_FUNCTIONS,)
       
       #Version 1 using OpenAI
        #llm = OpenAI(temperature=0)
        
        #If you don't specify an agent type, the default agent will be ZERO_SHOT_REACT_DESCRIPTION. 
        # This agent type is used to generate text descriptions of CSV file
        try:
            agent = get_csv_agent(csv_file)
        except Exception as e:
            st.error(f"An error occurred while trying to create CSV agent: {str(e)}")
            # The following line ends the execution of the function and avoids further errors.
            return
        
        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                if agent is not None:
                    try:
                        response = agent.run(user_question)
                        st.write(bot_message.replace(
                            "{{MSG}}", response), unsafe_allow_html=True)
                    except Exception as e:
                        st.error("An error occurred: {}".format(str(e)))
                else:
                    st.write("No corresponding agent!")
    else:
        st.write("No file uploaded!") 

# def main():
#     print("Hello world!")

# # Other function definitions
# def foo():
#     print("foo!")

# # ...

# if __name__ == "__main__":
#     main()  # This is called only when the script is run directly.

# In this case, if main.py is executed directly like so: python main.py,
# then Hello world! will be printed onto the console because the __name__ variable
# for the script will equal to "__main__", thus calling the main() function.

# But if you import main.py in another Python script using import main,
# no text is printed. However, the functions main() and foo() are now available for use in that script.



if __name__ == "__main__":
    main()
