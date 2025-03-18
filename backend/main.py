from fastapi import FastAPI
from agents.agent import LeaderAgent

### Le backend n'est pas clean et ne fonctionne pas à merveille.
app = FastAPI()

@app.get("/query/")
def query_ai(query: str):
    
    leader = LeaderAgent()
    return {"response": leader.assign_tasks(query)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)