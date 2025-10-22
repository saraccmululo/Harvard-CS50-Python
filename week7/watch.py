import re

def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern= r'<iframe[^>]*\s+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
        #Explanation=> [^>]* means any characters except ">” 0 or more times (allows other attributes before src)
        #  \s+ matches spaces before src (there's always sapces between the attributes)

    match=re.search(pattern, s)
        #get the video_id
    if match:
        video_id= match.group(1) #Output: xvFZjo5PgG0

        #insert video_id in short_url
        short_url = f"https://youtu.be/{video_id}"
        return short_url

if __name__ == "__main__":
    main()

