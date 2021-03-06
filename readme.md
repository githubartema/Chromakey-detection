# Green chromakey detection

Abstract: this repo includes a pipeline for green chromakey detection and masking.

## Description
The main idea is to use computationally efficient OpenCV methods. (yeah, C++ is so goodð)

Also, in some cases it can be fruitful to use some of YOLOs models in order to bound laptop zone and then to find the chromakey zone. 

However, in this case we do not really need as there are no other green zones and it requires more computations.

Additionally, I believe we can compute running average for coordinates to make the masking smoother.

## Installation

OpenCV library is required.

Installation:

```sh
pip install opencv-python
```
# Usage

**The directory tree should be:**

<pre>
.
âââ main.py
âââ person
âÂ Â  âââ person.jpeg
âââ readme.md
âââ result
âÂ Â  âââ result_video.mp4
âââ utils
âÂ Â  âââ utils.py
âââ video
    âââ green.mp4
</pre>

Usage example:

```sh
python3 main.py
```
[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
