from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
async def factorial(starting_number: int):

    if starting_number == 0:
        return {"result": False}
    
    result = 1
    current = starting_number
    
    while current > 1:
        result *= current
        current -= 1
    
    return {"result": result}
