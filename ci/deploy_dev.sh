#!/bin/bash
npm install -g serverless
cd ~/${CIRCLE_PROJECT_REPONAME}
npm prune --production
serverless deploy --region us-east-2

