#### To find files with the `.mp4` extension in Linux using the following shell command:

```bash
find /path/to/search -type f -name "*.mp4"
```

- **`/path/to/search`**: Replace this with the directory you want to search. If you want to search the entire file system, use `/`.
- **`-type f`**: Ensures that only files are found, not directories.
- **`-name "*.mp4"`**: Searches for files with the `.mp4` extension.

### Example:
To find all `.mp4` files in the `/home/user/videos` directory, you would run:

```bash
find /home/user/videos -type f -name "*.mp4"
```

If you want to search for `.mp4` files in the current directory, you can use the following command:

```bash
find . -type f -name "*.mp4"
```

- **`.`**: Refers to the current directory.
- The rest of the command functions the same, searching for files with the `.mp4` extension within the current directory and all its subdirectories.
