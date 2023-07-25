# AUTOSHORT

## Standard reaction
The standard reaction are described as json in the `asset_data.reactions`.  
Each reaction must have a `.gif` file for the visual and an optional `.mp3` file for the sound.  
Here are some specifications:  
1. The gif must be 1080x1080
2. The gif must last at least 5s
3. the sound should start at 0s

### How to create a standard reaction
1. download the reaction from a green screen meme website like: https://greenscreenmemes.com/
2. Extract the audio form the video using a tool like: https://clideo.com/cut-audio
3. Save the audio at `src/reactions/[reaction-name]/` as `[reaction-name].mp3`
4. Turn the video into a gif using: https://ezgif.com/video-to-gif  
At this step you should start by:  
4.1 converting the mp4 to a gif. (make sure to select the 25fps option)  
4.2 Then crop the gif into a square.  
4.3 The resize the gif to 1080x1080.
5. Save the gif at `src/reactions/[reaction-name]/` as `[reaction-name].gif`
6. finally create a json file at `src/reactions/[reaction-name]/` as `[reaction-name].json`
7. fil the json with the following format:  
7.1 `"color"`: Actual color of the green screen.  
7.2 `"has_audio"`: Set to true if the reactions has a sound `.mp3`.  
7.3 `"length"`: The length in seconds.
```
{
    "color": [0, 255, 15],
    "has_audio": true,
    "length": 12
}
```