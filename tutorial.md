Follow some step:

1. Clone data from hugging face:
- `*.mp4` file: store in dir `data/vid_promp_videos/`
- `.csv` file: store in dir `data/`

1. Compressing Videos and Images, the new file video will store in `data/processed_vid_promp_videos`

```bash
fps=2
size=224
file_type=video
input_root=data/vid_promp_videos
input_file_list_path=data/video_filenames.txt
# you may use `ls -U ${input_root} > ${input_file_list_path}` to efficiently generate the file above.
output_root=data/processed_vid_promp_videos

python preprocess/compress.py \
--input_root=data/vid_promp_videos --output_root=data/processed_vid_promp_videos \
--input_file_list_path=data/video_filenames.txt \
--fps=4 --size=224 --file_type=video --num_workers 24 
```

This command will process file in dir `input_root` and store in `output_root`

3. Prepare annotation for train and test set
- Prepare 2 file:
  - `data/video_filenames.txt`: for training phase
  - `data/video_filenames_test.txt`: for test phase
- Run command convert file name from `ms-` + file_name to file_name:

```bash
python data/transfer.py --type=test # for video_filenames_test.txt

python data/transfer.py --type=train # for video_filenames.txt
```

Output will generate file to `data/anno_*/` dir

4. Run command in file `DATA.md` to execute model