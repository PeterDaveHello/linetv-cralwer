# linetv-cralwer
> A simple tool for downloading video from LINE TV

## Requirements
- python3

## Introduction
LINE TV provides high resolution video streaming with '.ts' format. ```linetv-crawler``` enables user to download whole video with single command.

## Usage
LINE TV divides single episode into several parts. Therefore, we need to find out the video's urls for each part.

The video's url can be found by using the develope mode of browser (Google Chrome). For example ```https:/tv-line.../x.ts?__gda__=...```

```
python3 linetv-crawler.py "url of part1" "url of part2" -p <storage folder> -o <outfile name>
```

## Others
- Fix duration error [tsMuxeR](https://www.videohelp.com/software/tsMuxeR)
- Convert ```.ts``` to ```.mkv```: ffmpeg
  ```
  ffmpeg -i input.ts -c:v copy output.mkv
  ```

## Version
v1.0
