#! /bin/bash
cd `dirname $0`
mkdir -p requirements
pip install -r ./requirements.txt -t ./requirements