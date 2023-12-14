import os
import ffmpeg
import math

def split_video(input_file, output_directory, max_size_mb=30):
    # 获取输入视频的信息
    input_info = ffmpeg.probe(input_file)

    # 获取视频流的信息
    video_stream = next((stream for stream in input_info['streams'] if stream['codec_type'] == 'video'), None)

    if video_stream is None:
        print("No video stream found in the input file.")
        return

    # 计算每个小视频的目标时长，以便达到每个小视频的大小不超过指定的大小
    target_size_mb = max_size_mb
    input_duration = float(video_stream['duration'])
    input_size_mb = os.path.getsize(input_file) / (1024 * 1024)
    target_duration = input_duration * (target_size_mb / input_size_mb)

    # 计算要拆分的小视频的数量
    num_segments = math.ceil(input_duration / target_duration)

    # 使用ffmpeg进行拆分
    for i in range(num_segments):
        start_time = i * target_duration
        end_time = min((i + 1) * target_duration, input_duration)

        output_file = os.path.join(output_directory, f"{input_file[:-4]}_{i+1}.mp4")

        ffmpeg.input(input_file, ss=start_time).output(output_file, t=end_time - start_time).run()

        print(f"Segment {i+1} created: {output_file}")

def run(output_direct):
    output_directory = output_direct
    input_video = f"{output_directory}.mp4"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    split_video(input_video, output_directory)


def read_mp4_files(folder_path):
    mp4_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.mp4')]
    mp4_files = [os.path.join(folder_path, f) for f in mp4_files]
    return mp4_files

def result(folder_path = '/Users/Ted/Desktop/input_mp4'):
    mp4_files = read_mp4_files(folder_path)
    file_list = []
    if not mp4_files:
        print(f"No .mp4 files found in the '{folder_path}' folder.")
    else:
        print(f"Found the following .mp4 files in the '{folder_path}' folder:")
        for mp4_file in mp4_files:
            file_name = os.path.splitext(os.path.basename(mp4_file))[0]
            file_list.append(file_name)

    for file_each in file_list:
        run(file_each)


folder_path = '/Users/Ted/Desktop/week_10'
result(folder_path)

