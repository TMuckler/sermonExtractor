
# Sermon Audio Extractor

This Python script downloads the latest sermon from a specified YouTube link, extracts the audio, converts it to MP3 format, and trims it to a specified section.

## Requirements

- Python 3.x
- `pytube` package
- `pydub` package
- `ffmpeg` installed on your system

## Installation

1. **Clone the repository or download the script:**

    ```bash
    git clone https://github.com/TMuckler/sermonExtractor.git
    cd sermonExtractor
    ```

2. **Install the required Python packages:**

    ```bash
    pip install pytube pydub
    ```

3. **Install ffmpeg:**

    Follow the instructions on [ffmpeg.org](https://ffmpeg.org/download.html) to install `ffmpeg` on your system.

## Usage

To run the script, use the following syntax:

```bash
python sermonExtractor.py <YouTube link> <Start Time HH:MM:SS> <Duration Time HH:MM:SS>
```

### Example

```bash
python sermonExtractor.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 00:15:00 00:45:00
```

In this example:
- `https://www.youtube.com/watch?v=dQw4w9WgXcQ` is the YouTube link to the sermon video.
- `00:15:00` is the start time of the audio you want to extract.
- `00:45:00` is the duration of the audio you want to extract starting from the start time.

## Script Details

The script performs the following steps:

1. Validates command line arguments.
2. Initializes a YouTube object with the provided link and retrieves metadata about the video.
3. Downloads the audio stream from the video.
4. Converts the downloaded audio file to MP3 format.
5. Extracts the desired section of the audio file.
6. Removes the original downloaded file.
7. Notifies the user that the script has finished executing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## Acknowledgments

- [pytube](https://pytube.io/)
- [pydub](https://github.com/jiaaro/pydub)
- [ffmpeg](https://ffmpeg.org/)
