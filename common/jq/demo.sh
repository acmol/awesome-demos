echo "first demo:"
cat issues.json | jq .success

echo "second demo:"
cat issues.json | jq .issues[1:]

echo "third demo:"
cat issues.json | jq -r .issues[].content
