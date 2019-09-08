# Zamzar Converter
Allows you to convert Files from Command Line by using Zamzar APIs
## :gear: Prerequisites
- **Zamzar API Key**
	You can get an API Key from [this link](https://developers.zamzar.com)
- **Python 3.7**

## :wine_glass:  Installation
1. Clone the Repository
	```
	git clone https://github.com/harshanas/ZamzarConverter.git
	```
3. Install the Requirements
	```
	pip install -r requirements.txt
	```
4. Open _config.json_ file and Insert your API Key


## :hammer: Usage
To convert a file from _epub_ format to _pdf_, use the below command
```
convert.py -s "book.epub" -f "pdf"
```

### :mag_right: Arguments that can be parsed
| Argument | Description | Example |
|--|--|--|
| -s  | The path of the file to be converted | `-s "hello.mp4"`  |
| -f  | The format that files needs to get converted |` -f "avi"`  |

## :pray: Huge Thanks 
- To Zamzar devs
- To the people who view, star, fork clone and contribute to this repository