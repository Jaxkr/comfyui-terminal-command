from subprocess import getoutput


class Terminal:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "cachebuster": (
                    "INT",
                    {
                        "default": 0,
                        "display": "number",
                    },
                ),
                "text": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    def execute(self, image, cachebuster, text):
        out = getoutput(f"{text}")
        print("Output from terminal command: " + out)
        return (image,)

    CATEGORY = "utils"
