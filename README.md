# ManifestDownloader

MLTD manifest downloader

## Transfer type

The requested file type was "bytes",  
using .decode("utf-8") may convert data type to str

## invalid start byte

And the fetched filetype is "MSGPACK" originally,  
to prevent the bug is to avoid using .decode("UTF-8").
