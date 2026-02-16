# Folder Structure Preserver
Nicotine+ plugin that keeps original file paths.

Downloading a folder will keep the original folder structure of the downloded files, but what if you want to only download individual files?
By default, Nicotine+ will place those files into the root download directory, disregarding their original path.

This plugin solves that problem by moving any downloaded files into a folder structure that matches their original path.

# How to install:
Place the folder _folder_structure_preserver_ into your _nicotine/plugins_ folder, then enable it in Nicotine+ (Preferences -> Plugins).

# Known issues:
Because the files are moved _after_ being downloaded, the files listed in the _Downloads_ tab in the Nicotine+ UI will still show their old paths, which prevents them from being opened from there.
