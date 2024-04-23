# Asset-Tracker
Utility for tracking project assets not traditionally stored in git but that may require some VC.

Often when working with assets, especially during game development, you may have many large files that are not suitable for git such as image, sound, and video files. Ideally, these will be tracked, but not pushed to Git Hub. Also, you may want to quickly look at several versions of the same asset and looking through commits to view previous versions would be very tedious.
This tracking will keep track of defined file types inclusively, imagine a .gitinclude instead of .gitignore. There will be options for how files should be kept over time using versioning prefixes and suffixes.

# The Future
The initial utility will just focus on the basic backup and creation of a compressed archive of the version-tracked files.
Later versions may deal with setting up pipelines into popular file storage services.
