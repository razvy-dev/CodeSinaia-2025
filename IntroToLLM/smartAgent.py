import ollama
from index_notes import load_external_context

agent = 'gemma3:1b'

class Agent:
    context_window = []
    add_style = True
    def __init__(self, name, role, description):
        self.name = name
        self.role = role
        self.description = description

    def set_style(self, value):
        self.add_style = value


    def chat(self, prompt):
        # Create a chat message with the prompt
        message = {
            "role": "user",
            "content": prompt
        }
        
        # Add the message to the context window
        self.context_window.append(message)
        
        # Call the Ollama API to get a response
        response = ollama.chat(agent, messages=self.context_window)
        
        # Add the response to the context window
        self.context_window.append({
            "role": "assistant",
            "content": response['message']['content']
        })

        if self.add_style:
            response['message']['content'] += self.add_smiley_face()
        
        return response['message']['content']
    
    def add_context(self, context_path):

        loaded_context = load_external_context(context_path)

        self.context_window.append({
            "role": "system",
            "context": loaded_context
        })

    def add_smiley_face(self):
        # Add a smiley face to the response
        if "Sinaia" in self.context_window[-2]['content']:
            return " ̿̿’̿’\̵͇̿̿\=(•̪●)=/̵͇̿̿/’̿̿ ̿ ̿ ̿"
        elif "Hotel Transilvania" in self.context_window[-2]['content']:
            return "( ͡ಠ ͜ʖ ͡ಠ)"
        else:
            return " ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)"
    

