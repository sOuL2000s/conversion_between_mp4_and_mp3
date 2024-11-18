import os
import subprocess

def convert_mp4_to_mp3(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mp4_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith(".mp4")]

    if not mp4_files:
        print("No .mp4 files found in the folder.")
        return

    for mp4_file in mp4_files:
        base_name = os.path.splitext(os.path.basename(mp4_file))[0]
        output_file = os.path.join(output_folder, f"{base_name}.mp3")

        try:
            subprocess.run(
                ['ffmpeg', '-i', mp4_file, '-q:a', '0', '-map', 'a', output_file],
                check=True
            )
            print(f"Converted: {mp4_file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {mp4_file}: {e}")
        except FileNotFoundError:
            print("ffmpeg is not installed or not found in PATH.")
            return


def convert_mp3_to_mp4(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mp3_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith(".mp3")]

    if not mp3_files:
        print("No .mp3 files found in the folder.")
        return

    for mp3_file in mp3_files:
        base_name = os.path.splitext(os.path.basename(mp3_file))[0]
        output_file = os.path.join(output_folder, f"{base_name}.mp4")

        try:
            subprocess.run(
                ['ffmpeg', '-i', mp3_file, '-c:v', 'libx264', '-preset', 'fast', '-crf', '23', '-c:a', 'aac', output_file],
                check=True
            )
            print(f"Converted: {mp3_file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {mp3_file}: {e}")
        except FileNotFoundError:
            print("ffmpeg is not installed or not found in PATH.")
            return


# Example usage:
input_folder = "path/to/input/folder"  # Replace with the path to your input folder
output_folder_mp3 = "path/to/output/mp3_files"  # Replace with the folder to save .mp3 files
output_folder_mp4 = "path/to/output/mp4_files"  # Replace with the folder to save .mp4 files

# Convert MP4 to MP3
convert_mp4_to_mp3(input_folder, output_folder_mp3)

# Convert MP3 to MP4
convert_mp3_to_mp4(input_folder, output_folder_mp4)
