from fastapi import FastAPI, HTTPException
import subprocess
from pathlib import Path

app = FastAPI()

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"


@app.get("/scripts")
def list_scripts():
    return [f.stem for f in SCRIPTS_DIR.glob("*.py")]


@app.post("/scripts/{script_name}/run")
def run_script(script_name: str):
    script_path = SCRIPTS_DIR / f"{script_name}.py"
    if not script_path.exists():
        raise HTTPException(status_code=404, detail="Script not found")

    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
