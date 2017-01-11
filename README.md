# linetv-cralwer

## Install
```
git clone https://github.com/noname0930/linetv-cralwer.git
```

## Usage
- line.py

| index | var |
| ----- | ----- |
| 1 | one url of .ts from line_tv |
| 2 | storage folder |
| 3 | part of episode |
    
- merge.py

| index | var |
| ----- | ----- |
| 1 | store path |
| 2 | file name |

## Others
- Fix duration: tsMuxeR
- Convert to mkv: ffmpeg
    - [my-script](http://github.com/noname0930/my-scripts/) here
	    ```
	    ffmpeg -i input.ts -c:v copy output.mkv
	    ```