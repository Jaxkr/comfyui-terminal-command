from subprocess import getoutput

class Terminal:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",), "text": ("STRING", {"multiline": True})}}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    def execute(self, image, text):
        out = getoutput(f"{text}")
        print("Output from terminal command: " + out)
        return (out, )

    CATEGORY = "utils"
