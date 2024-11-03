import csv
import json
import argparse

IMAGE_DIR = 'data/processed_vid_promp_videos'

# Parse from args with --type
parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, choices=['train', 'test'], default='train')
args = parser.parse_args()

TRAIN_FILE = 'data/video_filenames.txt'
TEST_FILE = 'data/video_filenames_test.txt'
file_read = TRAIN_FILE if args.type == 'train' else TEST_FILE

OUTPUT_FILE_TRAIN = 'data/anno_pretrain/vid_promp.json'
OUTPUT_FILE_TEST = 'data/anno_downstream/vid_promp.json'
output_file = OUTPUT_FILE_TRAIN if args.type == 'train' else OUTPUT_FILE_TEST

def get_data_from_file():
    # Read video filenames
    with open(file_read, 'r') as file:
        video_filenames = [line.strip()[3:-4] for line in file.readlines()]

    # Read CSV and search for video filenames
    results = []
    with open('data/example_VidProM_unique_example.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['uuid'] in video_filenames:
                results.append({
                    "video": "ms-" + row['uuid'] + ".mp4",
                    "caption": row['prompt']
                })

    # Write results to JSON file
    with open(output_file, 'w') as jsonfile:
        json.dump(results, jsonfile, indent=4)

if __name__ == "__main__":
    get_data_from_file()