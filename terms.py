


def handleTermQuestion(user_id, convo_id, term):
    #get the conversation from the file system
    convo = 'convo'

    PROMPT = f"What does {term} mean? in the context of the following conversation: \n\n {convo}"

    #save the reponse the the user_id, convo_id, under the 'terms' table 