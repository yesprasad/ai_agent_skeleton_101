# agent/reason.py

def generate_plan(intent: str, user_input: str) -> dict:
    if intent == "question":
        return {
            "action": "rag_query",
            "query": user_input
        }

    elif intent == "summarize":
        return {
            "action": "summarize",
            "section": user_input
        }

    elif intent == "quiz_me":
        return {
            "action": "generate_quiz",
            "topic": user_input
        }

    elif intent == "compare":
        return {
            "action": "compare_sections",
            "compare_input": user_input
        }

    elif intent == "suggest":
        return {
            "action": "suggest_wellness_options",
            "goal": user_input
        }

    else:
        return {
            "action": "unknown",
            "message": "Sorry, I couldn't understand that request."
        }
