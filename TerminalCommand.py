from subprocess import getoutput

class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

  def __ne__(self, __value: object) -> bool:
    return False


any = AnyType("*")

class Terminal:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"input": (any, {}), "text": ("STRING", {"multiline": True})}}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    def execute(self, input, text):
        out = getoutput(f"{text}")
        print("Output from terminal command: " + out)
        return (out, )

    CATEGORY = "utils"
