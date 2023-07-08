from moviepy.editor import VideoFileClip, ImageClip, concatenate

LEN_1 = 3.3
LEN_2 = 2.5
AUDIO = "PATH_AUDIO"

def create_fma(image1, image2, out_name):
    clip1 = ImageClip(image1, duration=LEN_1)
    clip2 = ImageClip(image2, duration=LEN_2)
    video = clip1.set_audio(AUDIO)
    video_final = concatenate([video, clip2])
    video_final.write_videofile(out_name, fps=24)

image1 = "PATH_IMAGE_1"
image2 = "PATH_IMAGE_2"

out_name = "PATH_OUT"

create_fma(image1, image2, out_name)

