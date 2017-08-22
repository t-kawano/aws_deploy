#!/bin/bash
npm install -g serverless
cd ./src
pwd
npm prune --production
serverless deploy --region us-east-2
