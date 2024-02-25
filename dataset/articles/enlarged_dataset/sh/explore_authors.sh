# search author name in openalex using only first name 
cat article_complete_* | grep dc:creator | awk '{if($1 ~ /^<http*/){print($3,$4)}else{print($2,$3)}}' | sort | uniq -d | fzf |sed 's/"//' |cut -d " " -f 1 |xargs -ro echo https://api.openalex.org/authors?search= | sed 's/ //' | xargs -ro curl | jq
# search author name in openalex reverse substitute space with %20
cat article_complete_* | grep dc:creator | awk '{if($1 ~ /^<http*/){print($3,$4)}else{print($2,$3)}}' | sort | uniq -d | fzf |sed 's/"//g' | awk '{print($2, $1)}' | xargs -ro echo 'https://api.openalex.org/authors?search=' | sed 's/ //' | sed 's/ /%20/' | xargs -ro curl
# get author pubmed id  
cat article_complete_* | grep bibo:pmid | cut -d " " -f 2 | sed 's/"//g' | fzf --no-preview | xargs -ro echo https://api.openalex.org/works/pmid: | sed 's/ //g' | xargs -ro curl | jq -r .authorships[].author.id | cut -d"/" -f 4

# get id from name : 
cat w | jq -cr 'select(.name | length > 0 and contains("<name>")).id'

# get all authors from ttl à inclure : nom composés : contiennent "-"
cat ../article_complete_8.ttl  | sed -rn '/dc:creator/ {/\"[A-Za-z]+\s[A-Za-z]+\"\s;/p}'
