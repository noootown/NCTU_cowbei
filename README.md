# NCTU_cowbei
https://noootown.github.io/NCTU_cowbei

This is a site which crawls cowbei data from [靠北交大](https://www.facebook.com/CowBeiNCTU/).
Since posts from the page are not public, I have to crawl all them down instead of using Facebook API directly.
To make the page load faster, I only show 200 highest rank posts, but all posts that have likes >24 are crawled and stored in cowbei.csv.

Feel free to fork and have fun! I have to get my dinner LOL.

# Setup
## Environment
- python3
## Step
1. To crawl posts from Facebook, you need to edit ```config.json```. Please access [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/) and get your Facebook token and fanpage ID. There's no need to worry about the token being uploaded to Github pages, since the token will expire in two hours. Here's the picture:

![](./explorer.png)

2. Run ```python3 main.py``` and wait for the program to crawl all posts.

3. You may change the ```title```, ```showNum```, ```filename``` parameter in ```config.json``` if you want to.

4. Upload all these files and codes to gh-pages branch, and you're done.

5. Have fun!!

# RoadMap

I finished this project in only 3.5 hours. Since I may not have time to improve it, if you refine my code, add some cool features or improve the poor UI/UX, feel free to send me a pull request!!! TKS:)

# License

### MIT

