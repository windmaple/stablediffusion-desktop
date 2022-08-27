from flet import *
from diffusers import StableDiffusionPipeline
import threading
import random

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "1"


class EmptyHFTokenError(Exception):
    pass


model_id = "CompVis/stable-diffusion-v1-4"

pipeline = None


def main(page: Page):
    page.title = "Stable Diffusion Desktop v0.1"
    page.vertical_alignment = "center"

    def run_defusion(prompt):
        global pipeline
        device = "cpu" if gpu_switch.value == False else "cuda"

        try:
            if HF_token.value == "":
                raise EmptyHFTokenError("Empty Hugging Face token")

            if HF_token.value == "True":
                token = True
            else:
                token = HF_token.value

            if pipeline == None:
                pipeline = StableDiffusionPipeline.from_pretrained(
                    model_id, use_auth_token=token
                )

            pipeline = pipeline.to(device)
            image = pipeline(prompt)["sample"][0]
        except EmptyHFTokenError:
            page.snack_bar = SnackBar(
                content=Text(
                    "Make sure you have put in your Hugging Face access token"
                ),
            )
            page.snack_bar.open = True
            page.update()
        except RuntimeError:
            if device == "cuda":
                print("Most likely GPU OOM; switch to CPU to proceed")
                page.snack_bar = SnackBar(
                    content=Text(
                        "Runtime error. Most likely GPU is Out of Memory; switch to CPU to proceed"
                    ),
                )
                page.snack_bar.open = True
                page.update()
            else:
                print("Runtime exception")
        else:
            # Stupid workaround because I have not figured out how to force refresh the image holder if the file name is the same
            img_name = str(random.randint(0, 100000000)) + ".png"
            image.save("assets/" + img_name)
            img_holder.src = img_name
        finally:
            diffuse_button.disabled = False
            progress_ring.visible = False
            page.update()

    def diffuse_button_clicked(e):
        prompt = prompt_text_field.value
        diffuse_button.disabled = True
        progress_ring.value = None
        progress_ring.visible = True
        x = threading.Thread(target=run_defusion, args=(prompt,))
        x.start()
        page.update()

    prompt_text_field = TextField(
        label="Type your prompt here", text_align="left", width=512
    )
    img_holder = Image(src=f"/stock.png")
    diffuse_button = ElevatedButton(text="Diffuse!", on_click=diffuse_button_clicked)
    progress_ring = ProgressRing(width=16, height=16, stroke_width=2, visible=False)
    gpu_switch = Switch(label="Use GPU", value=False)
    HF_token = TextField(label="Your Hugging Face token", text_align="left", width=350)

    page.add(
        Row(
            [
                Column(
                    [
                        img_holder,
                        prompt_text_field,
                        Row([diffuse_button, progress_ring]),
                    ],
                    alignment="center",
                ),
                Column(
                    [
                        Text(
                            "Mandatory Hugging Face WRITE access token\n(https://huggingface.co/docs/hub/security-tokens).\nIt will not be shared with anyone:",
                            size=18,
                            color="blue",
                        ),
                        HF_token,
                        gpu_switch,
                    ],
                    alignment="center",
                    spacing=20,
                ),
            ],
            alignment="center",
            spacing=35,
        ),
    )


flet.app(target=main, assets_dir="assets")
