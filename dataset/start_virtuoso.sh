#!/bin/bash
# To be executed as sudo

if [ -f "env.sh" ]; then
    echo "Running env.sh."
    . ./env.sh
fi

docker run --restart always --name virtuoso \
  -p 8892:8890 -it \
  -e DBA_PASSWORD=pass \
  -e SPARQL_UPDATE=true \
  -e DEFAULT_GRAPH=http://ns.inria.fr/d2kab/graph/wheatgenomicsslkg \
  -v /home/lucifer/Documents/WheatGenomicsSLKG/docker_volume/virtuosodb:/database \
  -v /home/lucifer/Documents/WheatGenomicsSLKG/dataset:/dataset_wheatgenomicsslkg \
  -d openlink/virtuoso-opensource-7:latest
