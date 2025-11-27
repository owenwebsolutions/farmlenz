from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Save file locally for now
    contents = await file.read()
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
