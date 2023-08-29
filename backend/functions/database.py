import json
import random


# Get recent messages

def get_recent_messages():

    # Define the file name and learn instruction 
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are inteveriewng the user for a job as a Social Paid Ads Marketer. Ask short questions that are relevant to the juinior position. Your name is Rachel. The user is called Anthony. Keep your answers under 30 words. "
    }

    # Initialize messages
    messages = []

    # Add a random element 
    x = random.uniform(0,1)

    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include a light dry humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include a rather challenging question."
    
    # Append insturtion to message 
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass

    # Return 
    return messages    




# Store Messages 

def store_messages(resquest_message, response_message):
    
    # define the file name
    file_name = "stored_data.json"

    # Get recent messages
    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": response_message }
    assistant_message = {"role": "assistant", "content": resquest_message }
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the udpated file
    with open(file_name, "w") as f:
        json.dump(messages, f)

# Resest Messages
def reset_messages():

    # Overwrite the current file with nothing
    open("stored_data.json", "w")
    

