import base64
# http://docs.python-requests.org/en/latest/api/#main-interface


def updatePath(url, commit_message, content_str, sha):
    content_byte = base64.b64encode(content_str.encode())
    print(content_byte.decode('utf-8'))

    data={}
    data['message'] = commit_message
    data['content'] = content_byte.decode('utf-8')
    data['sha'] = sha

    return data

if __name__ == '__main__':
   updatePath("test.txt", "test", "111", "9d239ff80782ef04598a120993de2cc0f9611708")