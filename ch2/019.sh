cut -f 1 ./data/popular-names.txt | sort | uniq -c | sort -r -n
# uniqは連続した重複を消すため、sortで同じ名前を並べる必要がある