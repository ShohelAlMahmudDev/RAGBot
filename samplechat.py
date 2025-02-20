from langchain.llms import OllamaLLM

# Initialize the LLM with the specified model
llm = OllamaLLM(model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free")

# Now you can use the llm object for your tasks
response = llm.run("Hello, world!")
print(response)
