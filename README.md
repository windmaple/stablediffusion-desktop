# Stable Diffusion Desktop

## Overview
Stable diffusion model has been made available on [Hugging Face spaces](https://huggingface.co/spaces/stabilityai/stable-diffusion), which is nice. But sometimes the queue is long and you are in a hurry, so this desktop app is built. You can use it to run stable diffusion using your own GPU (or even just CPU) without writing any code. Obviously, if you are a developer, you really don't need this since the Hugging Face Diffuser library is so simple to use.

## Setup
You will need to provide a valid [Hugging Face token with WRITE access](https://huggingface.co/docs/hub/security-tokens). This is required by Hugging Face and the token will not be shared with any one. 

## Implementation
The app is written with [Flet](https://flet.dev/) for simplicity and packaged with PyInstaller.

![SCREENSHOT](assets/screenshot.png)


## FAQ
1. Why is it so slow when I run it the first time?
This is because Stable Diffusion needs to download a bunch of large model files. Once that is done, it's much faster.

2. Why is the executable so large?
This is because PyInstaller has to bundle everything into a single executable. There are a lot of dependencies.