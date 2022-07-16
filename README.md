# mltd-manifest-downloader

A python based mirishita manifest downloader.

## Issues

### Convert type

The requested file type was "bytes",  
using `.decode("utf-8")` for convert data type to str.

### Invalid start byte

And the fetched filetype is `MSGPACK` originally,  
using `.decode("UTF-8")` to prevent the bug.

## Build

Compile library:

```console
pyinstaller
```

Production release:

```console
pyinstaller -F main.py -i "icon.ico"
```

## License

Licensed under [MIT](LICENSE).

Informations provided by [api.matsurihi.me](https://api.matsurihi.me/docs/)  
The copyright of any data belongs to Bandai Namco Entertainment.  
