from core.retriever import retrieve_top_chunks
from core.llm_interface import query_llm

def execute_plan(plan:dict) -> str:
    print('plan is: ', plan)

