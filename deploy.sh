#!/bin/bash

pelican pelican/content -s pelican.conf.py
#rm -fR deploy/*
cp -R output/* deploy/
make publish
./publish.sh
cd ..