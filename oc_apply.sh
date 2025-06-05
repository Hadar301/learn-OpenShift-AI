#!/bin/bash

## Optional - delete the pipeline
# oc delete pipelinerun train-pipeline-run -n rh-ee-hacohen-dev  

## relese the resources that were captured by previous pipelineruns:
oc get pipelinerun -o name | grep '^pipelinerun.train-pipeline-run' | xargs oc delete

oc apply -f openshift/tasks/preprocess-task.yaml
oc apply -f openshift/tasks/train-task.yaml
oc apply -f openshift/tasks/build-task.yaml     
oc apply -f openshift/tasks/deploy-task.yaml 

oc apply -f openshift/tasks/pipeline.yaml
oc apply -f openshift/taskruns/pipelinerun.yaml

