jq
----

URL: https://stedolan.github.io/jq/

Online demo: https://jqplay.org/

对于下述 issues.json

    {
        "success": true,
        "issues": [
            {
            "id": 1,
            "title": "card 1",
            "content": "content 1"
            },
            {
            "id": 2,
            "title": "card 2",
            "content": "content 2"
            },
            {
            "id": 3,
            "title": "card 3",
            "content": "content 3"
            }
        ]
    }

想获得success的值：

    cat issues.json | jq .success

想获得从第二个开始的全部issue，则可以：

    cat issues.json | jq .issues[1:]

如果想获得全部issue content，并去掉字符串的""，则：

    cat issues.json | jq -r .issues[].content

