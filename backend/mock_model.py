# mock_model.py
class MockModel:
    def generate(self, prompt: str) -> str:
        return f"🩺 Based on '{prompt}', it might be a common illness. Consult a doctor for confirmation."
